# /// script
# dependencies = ["shapely", "fonttools", "uharfbuzz"]
# ///
"""Build the GitCommons logo SVGs (and PNGs when rsvg-convert is installed).

Run with: uv run build.py

Symbol: a Git branch graph drawn as a tree on shared ground. A trunk with a
commit at its top, two branches that each end in a commit, and a ground line.
Wordmark: "GitCommons" from Space Grotesk SemiBold outlines.
"""
from io import BytesIO
from pathlib import Path
import shutil
import subprocess

import uharfbuzz as hb
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from shapely.geometry import LineString, Point
from shapely.ops import unary_union

ROOT = Path(__file__).resolve().parent

FONT = ROOT / 'fonts' / 'SpaceGrotesk[wght].ttf'

MEADOW = '#1c7a4b'
IVORY = '#f7f5ec'
INK = '#141a26'       # wordmark on light backgrounds
FONT_WEIGHT = 600     # Space Grotesk SemiBold
FONT_SIZE = 80        # wordmark size on the symbol's 100-unit grid
TEXT_GAP = 20         # visible gap between the symbol and the G
LOGO_MARGIN = 12      # clear space around the full logo

STROKE = 8.0          # line weight on the 100-unit grid
COMMIT = 8.4          # commit radius
TRUNK = [(50, 86), (50, 24)]
GROUND = [(30, 86), (70, 86)]
BRANCHES = [  # cubic beziers: start, control 1, control 2, end
    ((50, 66), (50, 52), (25, 56), (25, 40)),
    ((50, 54), (50, 42), (75, 46), (75, 32)),
]
COMMITS = [(50, 19), (25, 34), (75, 26)]
TILE_SCALE = 0.9      # symbol size inside the 100-unit app tile
TILE_RADIUS = 23
MASKABLE_SCALE = 0.72  # keeps the symbol inside the 80% maskable safe zone
MARK_MARGIN = 6       # clear space around the symbol-only files


def bezier(p0, p1, p2, p3, samples=96):
    pts = []
    for i in range(samples + 1):
        t = i / samples
        u = 1 - t
        pts.append(tuple(u**3 * a + 3 * u * u * t * b + 3 * u * t * t * c + t**3 * d for a, b, c, d in zip(p0, p1, p2, p3)))
    return pts


def symbol():
    lines = [TRUNK, GROUND] + [bezier(*b) for b in BRANCHES]
    parts = [LineString(line).buffer(STROKE / 2, resolution=32) for line in lines]
    parts += [Point(c).buffer(COMMIT, resolution=48) for c in COMMITS]
    return unary_union(parts).simplify(0.004)


def path_data(shape):
    polygons = [shape] if shape.geom_type == 'Polygon' else list(shape.geoms)
    parts = []
    for polygon in polygons:
        for ring in [polygon.exterior, *polygon.interiors]:
            parts.append('M' + 'L'.join(f'{x:.3f} {y:.3f}' for x, y in list(ring.coords)[:-1]) + 'Z')
    return ''.join(parts)


def wordmark(left, centre_y):
    """Outlines of "GitCommons" starting at x = left, its capital height centred on centre_y."""
    semibold = instancer.instantiateVariableFont(TTFont(FONT), {'wght': FONT_WEIGHT})
    data = BytesIO()
    semibold.save(data)
    face = hb.Face(data.getvalue())
    buffer = hb.Buffer()
    buffer.add_str('GitCommons')
    buffer.guess_segment_properties()
    hb.shape(hb.Font(face), buffer)
    glyphs, order, k = semibold.getGlyphSet(), semibold.getGlyphOrder(), FONT_SIZE / face.upem
    baseline = centre_y + semibold['OS/2'].sCapHeight * k / 2

    def draw(pen, shift):
        x = 0
        for info, pos in zip(buffer.glyph_infos, buffer.glyph_positions):
            glyphs[order[info.codepoint]].draw(TransformPen(pen, (k, 0, 0, -k, shift + (x + pos.x_offset) * k, baseline - pos.y_offset * k)))
            x += pos.x_advance

    bounds = BoundsPen(glyphs)
    draw(bounds, 0)
    shift = left - bounds.bounds[0]
    pen = SVGPathPen(glyphs, ntos=lambda v: f'{v:.3f}'.rstrip('0').rstrip('.'))
    draw(pen, shift)
    x0, y0, x1, y1 = bounds.bounds
    return pen.getCommands(), (x0 + shift, y0, x1 + shift, y1)


def svg(view_box, body):
    x, y, w, h = view_box
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x:g} {y:g} {w:g} {h:g}" role="img" aria-label="GitCommons">\n'
            f'{body}\n</svg>\n')


def tile(d, scale, radius):
    k = f'translate(50 50) scale({scale}) translate(-50 -50)'
    return (f'  <rect width="100" height="100" rx="{radius}" fill="{MEADOW}"/>\n'
            f'  <path transform="{k}" fill="{IVORY}" fill-rule="evenodd" d="{d}"/>')


def main():
    shape = symbol()
    d = path_data(shape)
    x0, y0, x1, y1 = shape.bounds
    box = (round(x0 - MARK_MARGIN, 3), round(y0 - MARK_MARGIN, 3), round(x1 - x0 + 2 * MARK_MARGIN, 3), round(y1 - y0 + 2 * MARK_MARGIN, 3))
    files = {
        'gitcommons-mark-on-light.svg': svg(box, f'  <path fill="{MEADOW}" fill-rule="evenodd" d="{d}"/>'),
        'gitcommons-mark-on-dark.svg': svg(box, f'  <path fill="{IVORY}" fill-rule="evenodd" d="{d}"/>'),
        'gitcommons-app-icon.svg': svg((0, 0, 100, 100), tile(d, TILE_SCALE, TILE_RADIUS)),
        'gitcommons-app-icon-square.svg': svg((0, 0, 100, 100), tile(d, MASKABLE_SCALE, 0)),
        'gitcommons-favicon.svg': svg((0, 0, 100, 100), tile(d, TILE_SCALE, TILE_RADIUS)),
    }
    text_d, (tx0, ty0, tx1, ty1) = wordmark(x1 + TEXT_GAP, (y0 + y1) / 2)
    top, bottom = min(y0, ty0) - LOGO_MARGIN, max(y1, ty1) + LOGO_MARGIN
    logo_box = (round(x0 - LOGO_MARGIN, 3), round(top, 3), round(tx1 - x0 + 2 * LOGO_MARGIN, 3), round(bottom - top, 3))
    for ground, mark_fill, text_fill in (('light', MEADOW, INK), ('dark', IVORY, IVORY)):
        files[f'gitcommons-logo-on-{ground}.svg'] = svg(
            logo_box, f'  <path fill="{mark_fill}" fill-rule="evenodd" d="{d}"/>\n  <path fill="{text_fill}" d="{text_d}"/>')
    for name, text in files.items():
        (ROOT / name).write_text(text)
        print('wrote', name, f'({len(text)} bytes)')

    if not shutil.which('rsvg-convert'):
        print('rsvg-convert not found: skipped PNGs')
        return
    pngs = {
        'gitcommons-logo-on-light': ['-w', '2400'], 'gitcommons-logo-on-dark': ['-w', '2400'],
        'gitcommons-mark-on-light': ['-h', '1024'], 'gitcommons-mark-on-dark': ['-h', '1024'],
        'gitcommons-app-icon': ['-w', '1024'], 'gitcommons-app-icon-square': ['-w', '1024'], 'gitcommons-favicon': ['-w', '64'],
    }
    for stem, size in pngs.items():
        subprocess.run(['rsvg-convert', *size, str(ROOT / f'{stem}.svg'), '-o', str(ROOT / f'{stem}.png')], check=True)
        print('wrote', f'{stem}.png')


if __name__ == '__main__':
    main()
