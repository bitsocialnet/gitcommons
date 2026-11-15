<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="design/logo/gitcommons-mark-on-dark.png" />
  <img src="design/logo/gitcommons-mark-on-light.png" alt="GitCommons logo" width="90" />
</picture>

# GitCommons

Research into a decentralized alternative to GitHub, built on Bitsocial.

[Architecture brief](architecture-brief.md) · [Radicle research](radicle-research.md) · [Master plan context](master-plan-context.md) · [Logo](design/logo/README.md)

</div>

The likely architecture combines a Git-native peer-to-peer code layer with Bitsocial profiles, communities, discovery, reputation, funding and competing infrastructure services.

- **Profiles are nodes.** Each developer's profile is a Bitsocial full node, hosted over public RPC for most people and movable to their own machine at any time.
- **Discussions are communities.** Each repository's Discussions tab is a Bitsocial community, the peer-to-peer primitive 5chan and Seedit already ship.
- **CI is a market.** Any runner service can offer CI over public RPC, so providers compete on price, speed and trust.
- **Code stays Git.** Repositories replicate peer to peer, Radicle-style, and existing projects can start by mirroring from GitHub.

> [!NOTE]
> **Vision stage.** This is research, not a build specification. The project belongs in [Phase 5 of the Bitsocial master plan](https://bitsocial.net/#master-plan-phase-5) and depends on Phase 2 profile nodes plus practical public RPC infrastructure.

> [!IMPORTANT]
> GitCommons is a working name (see [Naming](#naming)). This project is independent and is not affiliated with or endorsed by GitHub, Inc. or the Git project.

## Documents

| Document | Contents |
| --- | --- |
| [architecture-brief.md](architecture-brief.md) | A second architecture synthesis covering project pages, identity, discussions, issues, CI and a minimal prototype |
| [radicle-research.md](radicle-research.md) | A deep dive on Radicle: its peer-to-peer architecture, Collaborative Objects, CI broker, social-layer gap and collaboration options |
| [master-plan-context.md](master-plan-context.md) | The relevant Bitsocial master plan phases and the protocol primitives this project depends on |
| [design/logo](design/logo/README.md) | The logo, its files and how it is built |

## The idea in one paragraph

GitHub is three products stacked together: a **code host** (git), a **collaboration layer** (issues, pull requests, discussions, reviews) and a **social network** (profiles, follows, stars, feeds, Explore, Sponsors). The social network is what makes open source thrive, through reputation, discovery and network effects, and it is the part nobody has decentralized well. [Radicle](https://radicle.dev/) decentralizes the code and collaboration layers (git replicated peer to peer, issues and PRs as signed git objects) but has almost no social layer, and its onboarding asks every user to run a node. Bitsocial has spent its entire existence building the decentralized social layer Radicle lacks: profiles, communities, feeds, discovery, anti-spam, and non-custodial RPC so that normal users never have to run a server. So the thesis is simple:

> **Decentralized GitHub = a code-collaboration layer (Radicle-style, git over p2p) plus Bitsocial's social, community, profile and discovery layer, running on profile nodes (Phase 2), served to most users via Forge RPC, with a competitive marketplace of CI runner services instead of one mandatory CI.**

Each developer's profile is a Bitsocial full node (a "profile node"). Most are hosted via public RPC (Forge RPC) so people don't have to self-host, and anyone can move to their own node at any time. Each repo's Discussions tab is a Bitsocial community. CI, GitHub's most important lock-in, becomes a set of competing runner services reachable over public RPC.

## The original vision

Tom, 2026-06-02:

> What if we could decentralize GitHub too? At Phase 5 of the master plan. Maybe it would be like Radicle but with the "Discussion" tab on GitHub being a Bitsocial community — so a pure p2p Bitsocial node. Also there would be profiles like on GitHub, so **profile nodes** (which we imagine we'll have during Phase 3 [now Phase 2]), so each profile is a Bitsocial full node, most of them via public RPC (**Forge RPC**).
>
> Also to decentralize CI — which is probably GitHub's most important feature — we'd probably use **centralized CI runner services via public RPC**, but the difference with GitHub is that on GitHub you're forced to use theirs, whereas on our GitHub-alternative Bitsocial client you'd be able to use **any CI runner service via public RPC, so there will be competition**.
>
> Most importantly, the social layer of GitHub is very good and valuable for open source to thrive, so Bitsocial can decentralize that fully. We could probably do a **hybrid, maybe even collab with Radicle**, who knows. It's not possible before Phase 3 [now Phase 2] at least, since it would require profile nodes as well as public RPC.

Everything below is research and structure built on top of that.

## Why GitHub's social layer is the real prize

You can already self-host git (Gitea, GitLab, cgit) and you can already replicate git peer to peer (Radicle). What has never been decentralized is the social graph of open source:

- **Profiles and reputation.** A developer's identity, contribution history and credibility.
- **Following, stars, feeds.** How people discover what to work on and whom to trust.
- **Explore, Trending, Topics.** How projects find contributors and users. The Bitsocial workspace already has a `github-explore-bitsocial-topic/` repo, a fork of GitHub's Explore and Topics data.
- **Discussions.** The open-ended community conversation around a project, separate from issues.
- **Sponsors.** Funding flowing to maintainers.

This is the layer Bitsocial is built to decentralize. Bitsocial communities, profiles, follows, feeds, discovery services, tipping, awards and anti-spam challenges map almost one-to-one onto GitHub's social surfaces. Code hosting is the solved problem: git is already content-addressed, and Radicle already did the p2p replication. The social part is where Bitsocial is uniquely positioned, and where a centralized incumbent is most vulnerable, because a captured social layer is what platform lock-in is made of.

## Where this fits in the master plan

The full text and dependency analysis are in [master-plan-context.md](master-plan-context.md).

| Phase | What it delivers | What it means here |
| --- | --- | --- |
| 1 | Decentralized imageboards and forums (5chan, Seedit) and the first non-custodial RPC service (Forge). In progress | Public RPC makes always-on p2p communities practical from mobile |
| 2 | The flagship profile-based app: profiles, follows, feeds, communities and profile nodes | **The unlock.** GitHub-style profiles are profile nodes; without them there is no decentralized GitHub |
| 3 | Bitsocial Network: appchain financial rails (`.bso` domains, tipping, awards, monetization) | Funds a Sponsors equivalent and grants |
| 4 | Infrastructure pluralism: competing RPCs, media hosts, discovery, moderation and profile-node hosting | The CI runner marketplace is this model applied to compute |
| 5 | The long tail of clients, including tools that make existing communities easier to run | A developer-collaboration client lives here |

So this is a Phase 5 client that is only possible because of Phase 2's profile nodes and RPC, and is economically shaped by Phase 4's service competition.

It is technically more than a social client. It is a collaboration client, but it is built entirely from primitives the first four phases already produce: profile nodes, communities, public RPC, competing services and financial rails. It needs no new protocol; it needs the protocol to exist.

## Radicle: the only existing pure-p2p forge

The full deep dive is in [radicle-research.md](radicle-research.md).

**Radicle is pure p2p, not federated.** Its current protocol, Heartwood, has "no clients or servers, only nodes", and every user runs one. Nodes are identified by public keys and replicate git repos via a gossip protocol plus git's own protocol. There are no instances or accounts as in ActivityPub. What looks federated is seed nodes: always-on nodes that keep repos available, the role Bitsocial calls a seeder or full node. That is structurally close to Bitsocial.

What Radicle does well, and should not be reinvented:

- **Git-over-p2p replication** that works. This is hard, and they have shipped it.
- **Collaborative Objects (COBs).** Issues, patches (their PRs) and reviews stored as signed git objects using CRDTs, offline-capable and independently verifiable.
- **Self-certifying repos** with per-repo delegates and a signature threshold, a built-in multisig-style governance for who can authorize changes.
- **A CI broker spec** (see [Decentralized CI](#decentralized-ci)).

Where Radicle is weak, and Bitsocial is strong:

- **Identity is bare.** A public key plus an optional, non-unique alias. No rich profile, social graph or reputation surface.
- **No consumer social layer.** COBs are great for code, but there is no following, feeds, Explore or Discussions-as-community experience for people.
- **High onboarding friction.** Every user runs a node. There is no mainstream non-custodial hosted path, which is what Bitsocial's Forge RPC provides.
- **Niche adoption.** Strong tech, small user base.

Radicle has a code layer and no social layer. Bitsocial has a social layer and no code layer.

## Proposed architecture

### The mapping

| GitHub feature | Centralized today | Decentralized on Bitsocial |
| --- | --- | --- |
| **Profile** (repos, followers, contribution graph) | GitHub account | A **profile node**: a Bitsocial full node (Phase 2). Identity is a keypair. Served via Forge RPC for people who don't self-host; movable to your own machine at any time |
| **Code and repo hosting** | GitHub servers | Git objects replicated p2p. Git is already a content-addressed Merkle DAG, so it fits either Radicle's Heartwood (gossip plus git) or Bitsocial's IPFS content-addressing. Seeded by profile nodes, Forge and competing seeders |
| **Discussions tab** | GitHub Discussions | **A Bitsocial community**: pure p2p, the primitive 5chan and Seedit already ship |
| **Issues** | GitHub Issues | Radicle COBs, or Bitsocial threads attached to the repo's community |
| **Pull requests** | GitHub PRs | Radicle patches (COBs) for merge mechanics; Bitsocial threads for review and discussion |
| **Stars, follows, feed, notifications** | GitHub social graph | Bitsocial's native social graph (flagship-app primitives, Phase 2) |
| **Explore, Trending, Topics** | GitHub Explore | Competing Bitsocial discovery and indexing services (Phase 4). The `github-explore-bitsocial-topic` data is a head start |
| **CI/CD (Actions)** | GitHub Actions: mandatory, theirs only | **Competing CI runner services over public RPC**: use any provider (see [Decentralized CI](#decentralized-ci)) |
| **Packages and releases** | GitHub Packages | Content-addressed artifacts seeded p2p, plus competing media hosts (Phase 4) |
| **Sponsors and funding** | GitHub Sponsors | Tipping and awards, Bitsocial Network rails (Phase 3) and decentralized grants (Phase 4 and 5) |
| **Org and governance** | GitHub org and permissions | Radicle per-repo delegates and threshold, plus Bitsocial community ownership (keypair-controlled) |

### The code layer

There are three options, and the choice is a real decision for build time.

| Option | How | Trade-off |
| --- | --- | --- |
| 1. Adopt Radicle for code | Use Heartwood (or a fork) for repo replication, patches and issues. Wrap it in a Bitsocial client that adds profiles, Discussions as communities, feeds, discovery and RPC onboarding. Bridge Radicle node keys to Bitsocial profile-node keys | Least reinvention, fastest to a real forge |
| 2. Build git-on-IPFS natively | Store git objects via IPFS content-addressing, discover via HTTP routers, seed like any community. Reimplement patches and issues as Bitsocial content types | Most cohesive with the existing stack, but it reinvents Radicle's git-over-p2p work. It is also the only option where Bitsocial's content-fade model would touch code, so a durable pinned-seeding tier would have to be built (see [Open questions](#open-questions)) |
| 3. Bridge and collaborate with Radicle | Treat Radicle as the code substrate and Bitsocial as the social substrate, with an explicit interop layer, and talk to Radworks | Potentially grant-fundable and mutually beneficial. Radworks ran an open RFP for CI integrations, so it wants integrators |

**Lean:** don't reinvent git over p2p (option 1 or 3), and own the social layer outright, since that is the differentiated and defensible part. Decide at build time, based on how Heartwood has evolved by then.

### Decentralized CI

This is the sharpest part of the idea.

| | How CI works |
| --- | --- |
| **GitHub** | CI (Actions) is bundled, and you are locked into GitHub's runners and billing. It is arguably GitHub's deepest lock-in |
| **Radicle** | CI is self-hosted per node. A broker listens for repo-change events on your node and launches adapters (Concourse, a generic webhook adapter, or the standalone "Ambient" adapter). Sovereign, but high-friction and with no marketplace |
| **GitCommons** | CI runner services compete via public RPC, like Bitsocial's non-custodial community-hosting RPC model. A repo, or its delegates, points at one or more runner services. Anyone can offer one, and they compete on price, speed, hardware (GPU, ARM, large runners), trust model and policy |

The hard part of someone else running your CI is trusting the result:

- Runners return **signed attestations** of build and test results.
- **Reproducible builds** let anyone independently re-verify a result.
- Delegates can require **N-of-M independent runners to agree** before a green check counts toward a merge. This generalizes Radicle's "delegates run CI to gain merge confidence" into a market of runners, and makes trust a tunable policy instead of a platform decree.
- Runners that want to sell stronger guarantees can offer hardened execution (TEEs).

This is Phase 4's infrastructure pluralism applied to compute. CI is one more service category beside RPCs, media hosts and discovery services.

### Identity and anti-spam

Bitsocial already solves both.

- **Identity.** One keypair is your profile node and your Radicle-style code identity. Bitsocial already treats identity as keypair-controlled and portable. Radicle already maps Node ID = Peer ID = Public Key and supports DID compatibility, so unification is plausible.
- **Spam on public repos.** Issue and PR spam is a real GitHub pain, and Bitsocial's per-community challenge model maps directly onto it. A repo can require a challenge (captcha, rate limit, token gate, allowlist, payment, custom code) before an outside identity can open an issue or submit a patch. Challenges are local and operator-defined, with no platform-level super-admin.

### GitHub mirroring as the onboarding path

Asking a project to migrate is the hardest sell. Asking it to mirror costs nothing: the repository stays on GitHub, a mirror keeps a p2p copy in sync, and the team keeps pushing where it already pushes. [open-git](https://open-git.com/home), a self-hosted (not decentralized) code host, leads its pitch with this, and the idea transfers directly.

- **No migration step.** It is plain git on both ends, so every commit, branch and tag is identical. Stopping the mirror loses nothing, because the repository is whole in both places.
- **The social layer arrives first.** A mirrored repo gets a project page, a Discussions community and profile links on day one, before anyone moves issues, pull requests or CI.
- **Mirrors are one more replaceable service.** A mirror can run on the maintainer's own node or be offered over public RPC by competing providers, like seeders and CI runners.
- **One side is canonical per ref.** Two-way sync needs a rule for diverging pushes. The simplest is fast-forward only, with GitHub canonical until the maintainers flip it. The flip is the actual migration, and by then it is a setting, not a project.
- **Code first.** Mirroring refs is easy. Mirroring issues and pull requests means two canonical states (see [Open questions](#open-questions)), so those stay on GitHub until a project switches.

### Agent session records that travel with the code

A growing share of commits is written by coding agents, and review then depends on what the agent was told as much as on the diff. open-git captures the agent session (prompts, transcript, tool calls) and stores it on a metadata branch inside the repository, in a format compatible with [Entire](https://entire.io), then shows it in the pull request timeline.

This fits a p2p forge better than a hosted one, because a metadata branch is ordinary git data:

- It replicates with the repository over the code layer, so no forge database holds the record and no provider can withhold it.
- It can be signed by the same key as the commits, so "this agent session produced this commit" is verifiable by anyone.
- Any client can render it. A client that ignores the branch still works.

Session transcripts can contain secrets and private context, so capture should be opt-in per repository and off by default for public ones, as open-git does.

## Collaborating with Radicle

There is a concrete hook for collaboration. **Radworks** (Radicle's funding DAO, formerly Radicle DAO, backed by the RAD token treasury) funds ecosystem work via grants and has issued open RFPs, including for CI integrations. A Bitsocial social and onboarding layer on top of Radicle's code substrate is:

- **Complementary, not competitive.** Bitsocial brings the social layer and mainstream RPC onboarding Radicle lacks; Radicle brings the git-over-p2p substrate and COBs Bitsocial would otherwise reinvent.
- **Potentially grant-fundable** through Radworks.
- **A way to bootstrap a network.** Existing Radicle repos could appear in the Bitsocial client on day one.

This is worth a conversation before committing to a fully native build. The decision can wait until Phase 2 to 5; the ecosystem will have moved by then.

## Open questions

These are the hard problems to settle at build time.

1. **Durability is the code layer's job, not Bitsocial's.** Bitsocial's "old content can fade" trade-off applies only to Bitsocial-hosted content, which is the social layer (discussions, profiles, feeds), where fade is normal social-media behavior. Code never lives in Bitsocial. It lives on the Radicle or git-over-p2p layer, which is built for durability: git keeps full history in every clone, and seed nodes keep it available. Durability only becomes this project's problem under [option 2](#the-code-layer), git-on-IPFS, which is an argument against that option. A rare long-lived discussion that deserves code-like permanence, such as a design rationale or an accepted answer, could be pinned with the same code-layer durability.
2. **CI result trust.** Signed attestations, reproducible builds, N-of-M runner consensus and optional TEEs (see [Decentralized CI](#decentralized-ci)). What is the default policy, and who sets it per repo?
3. **Code layer choice.** Adopt Radicle, build git-on-IPFS, or bridge (see [The code layer](#the-code-layer))?
4. **Identity unification.** One key across the Bitsocial profile node, the Radicle code identity and a DID? How do key rotation and recovery work for a developer identity people depend on?
5. **Code search at scale.** Search is heavy and centralizing by nature. It is likely a competing indexing-service category (Phase 4), not a protocol feature.
6. **Large binaries, LFS and release artifacts.** Content-addressed storage plus competing media hosts, but it needs a real design.
7. **Funding the commons.** Who pays for durable seeding and CI for unfunded open source? Candidates are Bitsocial Network rails, Sponsors and decentralized grants (Phase 3, 4 and 5).
8. **Scope of v1.** A read-only mirror plus Discussions first, or full collaboration from the start? (See [A staged path](#a-staged-path).)

## A staged path

Pieces can ship as the protocol matures, instead of waiting for everything.

| Stage | Needs | What ships |
| --- | --- | --- |
| **v0: Discussions** | Nothing new | A Bitsocial community attachable to any existing repo, even a GitHub or Radicle one, as its Discussions. The social layer is buildable earliest and is valuable on its own |
| **v1: Profiles** | Phase 2 | Profile nodes show a developer's repos and activity (mirrored, read-only), with follows and feeds |
| **v2: Real p2p repos** | A code-layer decision | Radicle or git-on-IPFS, with patches and issues. Existing projects arrive through [GitHub mirroring](#github-mirroring-as-the-onboarding-path) instead of a migration, and [agent session records](#agent-session-records-that-travel-with-the-code) ride along as a metadata branch |
| **v3: CI marketplace** | Phase 4 economics | Competing runner services over public RPC, with the trust model above |
| **v4: Sponsors and grants** | Phase 3 rails | Funding flows to maintainers, and to durable seeding and CI for the commons |

## Naming

The working name is **GitCommons**: the shared place for git that nobody owns. It is descriptive (git), it states the difference from GitHub (a commons has no owner, a hub has one), and it reads as the universal place for code, not as a niche alternative.

**Bitsocial Forge** already names the operator and RPC service, so "forge" stays out of the product name.

The name uses "Git", which is a trademark of the Git project. The project is fully decentralized and GPL-3.0-or-later free software, so the name is used for now, and it can change if the Git project ever objects.

## Prerequisites

Before this is buildable, the network needs:

- [ ] **Profile nodes** (Phase 2): the flagship profile-based client and profile-node infrastructure shipped.
- [ ] **Public and Forge RPC at scale** (Phase 2): non-custodial hosted nodes, so developers don't have to self-host.
- [ ] **A competing-services economy** (Phase 4): the marketplace pattern that makes the CI runner market real.
- [ ] **Bitsocial Network rails** (Phase 3): for Sponsors, grants and durable-seeding funding. Nice to have, not strictly blocking v0 to v2.
- [ ] **A code-layer decision**: adopt or bridge Radicle, or build git-on-IPFS natively.
- [ ] **A code-layer durability tier**: handled by the code layer (Radicle or git seed nodes), not by Bitsocial. It only needs solving under git-on-IPFS.

## License

[GPL-3.0-or-later](LICENSE)
