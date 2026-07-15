# Architecture Brief

Date: 2026-06-02

Status: parked Phase 5 research note. This is not a build spec yet. It depends on Phase 3 profile nodes and practical public RPC, and probably benefits from Phase 4 service-market infrastructure.

## Short thesis

Bitsocial could eventually support a decentralized GitHub alternative by treating developer collaboration as another social client category: code repositories, project pages, patches, issues, CI results, profiles, follows, reputation, and project discussions should be separable layers instead of one company-owned platform.

The strongest version is probably not "rewrite GitHub from scratch." It is a hybrid forge:

- use Git/Radicle-like infrastructure for repository replication, patches, signed code state, and code review primitives
- use Bitsocial for the social layer: profiles, project communities, discussions, follows, discovery, moderation, reputation, and service competition
- use public RPC and later service markets so CI runners, indexers, discovery providers, and hosted nodes can compete instead of becoming a GitHub-shaped monopoly again

The big insight is that GitHub's moat is not only Git hosting. Git is already decentralized. GitHub's moat is the social surface around Git: profiles, repos as social objects, issues, pull requests, discussions, notifications, discovery, stars, reputation, and CI. Bitsocial is well-positioned to decentralize that social surface.

## Availability boundary

Bitsocial's "no permanent availability by default" tradeoff is not a blocker for GitHub-style discussion tabs. Project discussions, announcements, support questions, and social replies are naturally community-shaped data: they benefit from p2p ownership, local moderation, and public RPC help, but they do not need to be the canonical durable object store for source code.

Git is different. Repositories, refs, release artifacts, patches, and CI inputs need repository-grade replication, integrity, and long-term retrievability. Bitsocial should not try to be the Git storage layer. That is why the forge should use Radicle or a similar Git-native p2p layer for code, while using Bitsocial for the attached social/community layer.

Put another way: Bitsocial can decentralize GitHub's social surface without pretending Bitsocial communities are a replacement for Git.

## Original idea captured

- Phase 5 could include a decentralized GitHub alternative as one of the "long tail" Bitsocial clients.
- The GitHub `Discussions` tab could be a Bitsocial community attached to a repo or project.
- Developer profiles could be Bitsocial profile nodes, matching the Phase 3 idea that each profile is a full p2p node, often accessed through non-custodial public RPC such as Bitsocial Forge RPC.
- CI could be decentralized as a market of centralized or self-hosted runner services. GitHub Actions is powerful, but GitHub forces projects into its integrated runner ecosystem by default. A Bitsocial forge client could let projects choose any runner service over public RPC, with multiple providers competing.
- The social graph matters: profiles, project feeds, follows, discussions, announcements, maintainership, reputations, sponsors, grants, and discovery are the parts that make open source thrive.
- Radicle is the closest existing project and may be worth collaborating with rather than competing against directly.

## Fit with the master plan

This belongs after Phase 3, not before it.

Local Bitsocial docs already describe Phase 3 as the first profile-based client with posts, replies, follows, real-time public conversation, communities, replaceable RPCs, optional feed algorithms, and self-hostable profile nodes. A developer forge needs exactly those primitives.

Local docs also describe Phase 5 as the point where Bitsocial expands into the long tail of social clients after core apps, public RPCs, profile nodes, discovery, and monetization exist. A GitHub alternative is a perfect Phase 5 client because it is partly social media for developers and partly service infrastructure.

Phase 4 also matters because the forge would need plural infrastructure: RPCs, CI runners, media/artifact hosts, indexers, discovery providers, package mirrors, and maybe code-search services.

## Radicle research summary

Radicle is currently the most relevant reference design. The project now presents itself at `radicle.dev` / `radicle.network` rather than only `radicle.xyz`.

What Radicle does well:

- It is an open-source, peer-to-peer code collaboration stack built on Git.
- Every user runs a Radicle node. Nodes are identified by Ed25519 public keys and DIDs.
- Repositories have stable repository IDs derived from an identity document.
- Repository ownership and permissions are handled through delegates and signature thresholds.
- The network uses gossip for peer/repository discovery and Git protocol replication for the actual repository data.
- Seed nodes exist for availability, but the docs frame them as interchangeable infrastructure rather than identity-owning instances.
- Social artifacts such as issues, patches, identities, reviews, and discussions are stored as Git-backed Collaborative Objects (COBs), signed and replicated between peers.
- Radicle's COB model is extensible, so new collaboration objects can be added without changing the whole protocol.
- Radicle CI listens for repository-change events from a node. A CI broker decides when to run CI and calls adapters. Adapters can run locally, in containers, or through external CI systems such as GitHub Actions, Woodpecker, and others.

Important nuance:

- Radicle is not federated in the Mastodon/Lemmy sense. It does have seed/bootstrap nodes and web frontends, but repository identity and social artifacts are not supposed to be owned by those servers.
- Radicle profiles are currently closer to node/DID/alias identities than polished GitHub-style social profiles. Their user guide also notes that multi-device identity linking is still being designed. Bitsocial profile nodes could be complementary here.
- Radicle's private repository model is based on selective replication and trusted peers; docs say private repo data is not encrypted at rest. That matters for any future private-code story.

## Recommended direction

The best initial direction is a hybrid with Radicle or Radicle-compatible concepts:

1. Let Git stay Git.
2. Let Radicle, or a similar Git-native p2p layer, handle repository replication, repository identity, signed refs, delegates, patches, and maybe issues.
3. Let Bitsocial handle the broader developer social network:
   - GitHub-style profiles
   - project communities
   - repo discussions
   - project announcements
   - follows and social graph
   - discovery and trending
   - reputation
   - grants, sponsors, bounties, tipping, and awards
   - moderation and anti-spam challenges
   - CI runner marketplaces
4. Bridge between Radicle identities and Bitsocial profiles instead of forcing one identity model too early.

This would position Bitsocial as the decentralized social/app/service layer around p2p code collaboration, rather than trying to beat Radicle at the Git-specific protocol layer where they already have deep work.

## Possible product model

### Project page

A project page could look familiar:

- README and code browser
- branches/tags/releases
- patches or pull requests
- issues
- discussions
- CI status
- maintainers/delegates
- sponsors/grants/bounties
- package/artifact links

Under the hood, these do not need to share one backend:

- code and patches can come from Radicle or a Git p2p layer
- discussions can be a Bitsocial community
- profile cards can come from Bitsocial profile nodes
- CI state can come from signed runner results
- discovery can come from swappable indexers or feed algorithms

### Discussions as Bitsocial communities

GitHub Discussions is the cleanest first target. Each repository can have an attached Bitsocial community:

- community address linked from the project metadata
- maintainers/delegates are default mods
- contributors and users discuss roadmap, questions, support, governance, and announcements
- posts remain portable and readable from any compatible Bitsocial client
- moderation is local to the project community

This avoids forcing all discussion state into Git while still keeping it p2p and community-owned.

The availability expectations are different from code. If a discussion community temporarily has fewer peers online, that is a social availability problem public RPCs and seeders can improve. If repository data disappears, the project itself is at risk. This is why code should stay in Git/Radicle-like infrastructure and discussions can live in Bitsocial.

### Issues and patches

Two options:

- Keep issues and patches in Radicle COBs, then render them in the Bitsocial forge UI.
- Mirror or bridge issue events into a Bitsocial community when the social/conversation benefits are worth it.

The first version should avoid two canonical issue states. Pick one canonical store and treat the other as a view or notification layer.

### Developer profiles

Bitsocial profile nodes can become richer than Radicle's current node aliases:

- identity and .bso name
- avatar, bio, links, keys, devices
- pinned repos and project memberships
- contribution feed
- follows
- grants/sponsor links
- reputation signals
- selected RPC/provider preferences

Most users could start on a hosted non-custodial public RPC, then move to a self-hosted profile node later.

### CI runner marketplace

CI is probably GitHub's most important non-social platform feature. A Bitsocial forge should make CI a service market:

- runner providers register capabilities: language/toolchain support, container isolation, hardware, cache behavior, cost, availability, privacy policy, attestation support
- project maintainers select one or more providers
- runners watch project changes through Radicle node events, Bitsocial public RPC, or a project-specific webhook bridge
- runners publish signed status results, logs, artifacts, and attestations
- clients display CI results in a standard format regardless of runner provider
- users can switch providers without moving the repo or community

Centralized CI runner services are acceptable as long as they are replaceable. The win is competition and exit, not pretending every build must run on a purely p2p substrate.

## Architecture sketch

```text
Developer client
  -> Bitsocial profile node or public RPC
  -> Project Bitsocial community for discussions
  -> Radicle/Git p2p node for code, patches, refs
  -> CI runner provider over public RPC or node event bridge
  -> Discovery/indexer/feed provider for search and trending

Project identity
  -> Radicle RID / Git identity document
  -> Bitsocial project community address
  -> maintainer/delegate mapping
  -> optional .bso project name
```

## What a minimal Phase 5 prototype could be

1. Directory of Radicle repositories backed by Bitsocial developer profiles.
2. A Bitsocial community attached to each repo as its Discussions tab.
3. A project page that renders Radicle repo metadata plus Bitsocial community activity.
4. A CI status bot/provider that posts signed build results to the project page or community.
5. Later: patch/issue rendering, identity mapping, runner marketplace, grants/sponsorships, code search, and package/release surfaces.

## Open questions and risks

- Canonical state split: avoid having "the real issue" live in both Radicle COBs and Bitsocial posts.
- Identity mapping: Radicle uses device/node DIDs today; Bitsocial profile nodes imply human or organization profiles. The bridge needs careful design.
- Multi-device identity: Radicle's own docs mention this is not fully solved yet. Bitsocial profiles may be able to help.
- CI security: untrusted runners, secrets, supply-chain attacks, artifact tampering, reproducible builds, and signed attestations need a real threat model.
- Legal and abuse pressure: seeders, RPCs, and code hosts may face malware, leaked secrets, copyright/DMCA, and harassment problems.
- Private repositories: Radicle private repos are selectively replicated and not encrypted at rest, so a private-code product may need a stronger privacy layer.
- Incentives: seeders, CI runners, artifact hosts, and indexers need sustainable payment or reputation models.
- Search and discovery: GitHub search/trending is a major value center. Bitsocial should make discovery replaceable, but there still needs to be a great default.
- UX: normal developers will not tolerate fragile p2p setup. Public RPC and default seed/rpc/runner bundles need to make the first experience feel simple.

## Why this is strategically interesting

GitHub is one of the most important social networks in open source. It is also where a lot of developer reputation, project governance, funding, discussion, and CI dependency now lives.

If Bitsocial can decentralize developer profiles, repo discussions, project communities, discovery, grants, and CI provider choice, it could attack GitHub's real lock-in while partnering with or reusing the strongest p2p Git work that already exists.

Radicle may be a collaborator, dependency, integration target, or design inspiration. The likely winning posture is: Radicle for sovereign Git collaboration, Bitsocial for the open social/service layer around it.

## Sources

External:

- Radicle homepage: https://radicle.dev/
- Radicle protocol guide: https://radicle.dev/guides/protocol/
- Radicle user guide: https://radicle.dev/guides/user/
- Radicle seeder guide: https://radicle.dev/guides/seeder
- Radicle CI development article: https://radicle.dev/2025/07/23/using-radicle-ci-for-development.html
- Radicle with GitHub Actions article: https://radicle.dev/2025/05/30/radicle-with-github-actions.html
- Bitsocial master plan, Phase 3: https://bitsocial.net/#master-plan-phase-3
- Bitsocial master plan, Phase 5: https://bitsocial.net/#master-plan-phase-5

Bitsocial context:

- [Master plan implementation](https://github.com/bitsocialnet/bitsocial-web/blob/master/about/src/components/master-plan.tsx)
- [Flagship Bitsocial app](https://github.com/bitsocialnet/bitsocial-web/blob/master/docs/flagship-bitsocial-app.md)
- [Decentralize all social media](https://github.com/bitsocialnet/bitsocial-web/blob/master/docs/decentralize-all-social-media.md)
- [Identity and ownership](https://github.com/bitsocialnet/bitsocial-web/blob/master/docs/identity-and-ownership.md)
- [Build your own client](https://github.com/bitsocialnet/bitsocial-web/blob/master/docs/build-your-own-client.md)
