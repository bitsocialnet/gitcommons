# Master plan context

Why a decentralized-GitHub client is a **Phase 5** project that depends on **Phase 2**, with the relevant Bitsocial master plan text and protocol primitives. Sourced from the Bitsocial Web repo (`bitsocial-web/docs/*` and `about/public/translations/en/default.json`) on 2026-06-02. Live version: <https://bitsocial.net/#master-plan>.

---

## The master plan (homepage version, verbatim)

> On 2026-11-14 the master plan swapped phases 2 and 3: the flagship Twitter/X alternative is now Phase 2 and Bitsocial Chain (formerly Bitsocial Network) is Phase 3. The phases below use the new numbers.

**Phase 1 — Ongoing: Decentralize imageboards and forums**
Imageboards are the simplest form of social media to decentralize: anonymous posting, few default boards, and no profile graph. 5chan proves Bitsocial can replace centralized imageboards while removing global admins from the equation. Bitsocial Forge will launch the first non-custodial RPC service for Bitsocial apps. Bitsocial RPC will let users manage nodes remotely, while preserving the option to self-host or run competing RPC infrastructure. Users will be able to create and manage unstoppable p2p communities from mobile. Forums add persistent identities, post history, and community management. Seedit is the first prototype Bitsocial app for Reddit-style discussion, and public RPC makes those always-on P2P communities practical from anywhere.

**Phase 2: Launch the flagship Bitsocial app**
The flagship Bitsocial app should be the first profile-based client: posts, replies, follows, real-time public conversation, and communities that can pull network effects from every Bitsocial client. By default, it can feel as familiar as a modern For You social app, while still letting users switch RPCs, feeds, instances, algorithms, ads, or remove ranking entirely. Through non-custodial RPC, each user can still act as a full p2p node without trusting the RPC with ownership. Anyone should be able to move to their own **profile node** on a low-spec machine, including a Raspberry Pi, whenever they want. Because Phase 3 gives the app an unstoppable crypto financial layer, the flagship client can potentially become an everything-app without turning into a custodial platform.

**Phase 3: Launch Bitsocial Network**
In order to decentralize all social media, Bitsocial apps will need killer features and strong network effects: unstoppable financial structures, decentralized Bitsocial domains (.bso), awards and tipping, common liquidity, and practical monetization. All of this will be powered by Bitsocial Network, a decentralized appchain solution for Bitsocial apps.

**Phase 4: Scale Bitsocial economies**
The next layer is ecosystem funding and infrastructure pluralism. Bitsocial Forge's RPC should not be the only successful RPC: many businesses, independent teams, anonymous operators, and community entities should build RPCs, media hosting, discovery, moderation, and other services on top of Bitsocial. Funding should push that decentralization forward, so developers and operators can compete to make the network faster, cheaper, more reliable, and harder to capture.

**Phase 5: Decentralize all social media**
With the core apps, public RPCs, profile nodes, discovery, and monetization in place, Bitsocial can fund and build the long tail of social clients: blogging, crowdfunding, creator video and a credible YouTube alternative, niche experiments, and every format too early for the first four phases. Bitsocial Forge can build some of them, centralized clients can compete too, they do not all have to be FOSS, and decentralized community grants can fund as many developers as possible. The end state is not one app. It is a market of clients, nodes, services, and communities that can replace platform ownership with protocol competition. Social media finally finds its equilibrium: a fully decentralized, peer-to-peer social network that nobody owns; Bitsocial.

---

## How a GitHub alternative maps onto the phases

| Phase | What it provides | What the GitHub client uses it for |
| --- | --- | --- |
| **1** | 5chan/Seedit communities, first non-custodial Forge RPC, mobile p2p communities | The **Discussions-tab-as-community** primitive already works here (v0 is buildable earliest). |
| **2** | **Flagship profile-based app + profile nodes + non-custodial RPC** | **THE UNLOCK.** GitHub profiles = profile nodes. Mainstream onboarding = Forge RPC. Without this, no decentralized GitHub. |
| **3** | Bitsocial Network: .bso names, tipping, awards, monetization | **Sponsors-equivalent**, durable-seeding funding, repo/profile naming. |
| **4** | Infrastructure pluralism: competing RPCs, hosts, discovery, moderation, profile-node hosting | **The CI-runner marketplace** + Explore/discovery services + repo seeding-as-a-service. |
| **5** | Fund the long tail of clients + "tools that make existing communities easier to run" | **Home of the GitHub-alternative client itself.** |

**Conclusion:** it's a **Phase 5 client**, only *possible* because of **Phase 2** (profile nodes + RPC), and economically shaped by **Phase 4** (service competition → CI marketplace). Phase 3 funds the commons. This matches the original instinct that "it's not possible before Phase 2."

---

## Relevant protocol primitives (from `bitsocial-web/docs/`)

These already-designed primitives are what the GitHub client would build on:

- **Public-key-based addressing** — the hash of a community's public key is its network address (like BitTorrent content-addressing, but for keys). *A repo could be addressed the same way.*
- **HTTP routers (not a DHT)** — thin indexes mapping a content address → provider peer addresses; they never store content. Cheap, swappable, browser/mobile-friendly. *Repo/profile discovery would use the same routers.*
- **Peer-to-peer pubsub (gossipsub)** — open publish/subscribe, no central broker. *Real-time repo events, CI notifications, issue/PR updates.*
- **Challenge-based anti-spam** — each community runs its own pluggable challenge (captcha, rate-limit, token-gate, payment, allowlist, custom code) before accepting a post. *Directly applicable to spam-resistant public issues/PRs.*
- **Communities as first-class cryptographic objects** — operator node validates posts and enforces policy; no protocol-level super-admin. *A repo's Discussions = exactly this.*
- **Non-custodial public RPC** — capability-scoped permissions, user isolation, ownership stays with the user; Forge runs the first one, others compete. *Profile-node hosting + CI runner services use this model.*
- **Browser P2P (Helia)** — a normal HTTPS site can open into a live p2p client; pkc-js browser stack. *A web GitHub-client that's genuinely p2p in-browser.*
- **Profile nodes / full nodes** — a user's node, runnable on a Raspberry Pi, hostable via RPC. *= a developer profile.*
- **Positioning:** explicitly **not** a blockchain, **not** federation, and distinct from Nostr's relay model. Tradeoff to remember: Bitsocial does **not** guarantee permanent availability of old content — but that only applies to the **social layer** (discussions/profiles/feeds), where fade is acceptable. **Code never goes on Bitsocial**; it lives on the Radicle / git-over-p2p layer, which is built for durability (see README §8).

---

## Bonus signal: Git is already entering Forge's stack

The Forge RPC notes already include a **"Git-Backed Community Challenge Editing Plan"** (`forge/forge-rpc/git-backed-community-challenge-editing-plan.md`, 2026-05-31). Forge RPC will use Git as the *versioning, review, audit, and rollback* layer for community challenge config and custom challenge code — with branches for proposed edits, signed commits, review gates, **"CI-style validation before apply,"** and rollback to known-good revisions (SQLite stays the runtime DB; Git is the change-history layer).

This matters for two reasons:
1. **Git is already in the team's infrastructure mental model** — including a notion of CI-style validation gates inside Forge RPC.
2. It's a small proof that **git + Bitsocial's non-custodial RPC compose naturally** — ordinary users never see git, but every meaningful change is a signed commit behind the scenes. That's a miniature of the whole GitHub-alternative thesis: git underneath, a friendly Bitsocial-native surface on top.

---

## Branding notes

- Protocol/org: **Bitsocial** (capital B). Operator: **Bitsocial Forge**. RPC service: **Forge RPC**.
- Existing clients: **5chan** (imageboard), **Seedit** (Reddit-style), **plebones**, flagship app (Phase 2, X/Twitter-style).
- Naming heritage worth noting: **Plebbit** is the predecessor protocol Bitsocial evolved from (subplebbit → community, plebbit-js lineage). Useful context, not something to surface to mainstream users.
- The GitHub-alternative client has **no name yet** — and doesn't need one until build time.
