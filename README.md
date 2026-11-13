# Decentralizing GitHub on Bitsocial

**This repository explores a truly decentralized alternative to GitHub built on Bitsocial.** The likely architecture combines a Git-native peer-to-peer code layer with Bitsocial profiles, communities, discovery, reputation, funding, and competing infrastructure services.

> **Status: vision stage.** This is research, not a build specification. The project belongs in [Phase 5 of the Bitsocial master plan](https://bitsocial.net/#master-plan-phase-5) and depends on Phase 3 profile nodes plus practical public RPC infrastructure.
>
> **Working name: GitCommons.** "Decentralized GitHub" describes the research topic; GitCommons is the working name for the product (see [§10](#10-naming)). This project is independent and is not affiliated with or endorsed by GitHub, Inc. or the Git project.

## Documents

- [`architecture-brief.md`](architecture-brief.md) — a second architecture synthesis covering project pages, identity, discussions, issues, CI, and a minimal prototype.
- [`radicle-research.md`](radicle-research.md) — a deep dive on Radicle, its peer-to-peer architecture, Collaborative Objects, CI broker, social-layer gap, and collaboration options.
- [`master-plan-context.md`](master-plan-context.md) — the relevant Bitsocial master plan phases and the protocol primitives this project depends on.

---

## 1. The idea in one paragraph

GitHub is three products stacked together: a **code host** (git), a **collaboration layer** (issues, pull requests, discussions, reviews), and a **social network** (profiles, follows, stars, feeds, Explore, Sponsors). The social network is the part that makes open source *thrive* — reputation, discovery, network effects — and it's the part nobody has decentralized well. [Radicle](https://radicle.dev/) decentralizes the code + collaboration layers beautifully (git replicated peer-to-peer, issues/PRs as signed git objects) but has almost no social layer and a high-friction "everyone runs a node" onboarding. **Bitsocial has spent its entire existence building exactly the decentralized social layer Radicle lacks** — profiles, communities, feeds, discovery, anti-spam, and non-custodial RPC so normal users never have to run a server. So the thesis is simple:

> **Decentralized GitHub = a code-collaboration layer (Radicle-style, git-over-p2p) ⊕ Bitsocial's social/community/profile/discovery layer, running on profile nodes (Phase 3), served to most users via Forge RPC, with a competitive marketplace of CI runner services instead of one mandatory CI.**

Each developer's **profile is a Bitsocial full node** (a "profile node"), most of them hosted via public RPC (Forge RPC) so people don't have to self-host — but anyone can move to their own node anytime. Each repo's **Discussions tab is literally a Bitsocial community** (pure p2p, the primitive Bitsocial already ships in 5chan/Seedit). And **CI** — GitHub's most important lock-in — becomes a set of competing runner services reachable over public RPC: unlike GitHub, where you're forced onto theirs, here any CI provider competes on price, speed, and trust.

---

## 2. The original vision (captured faithfully)

Tommaso, 2026-06-02:

> What if we could decentralize GitHub too? At Phase 5 of the master plan. Maybe it would be like Radicle but with the "Discussion" tab on GitHub being a Bitsocial community — so a pure p2p Bitsocial node. Also there would be profiles like on GitHub, so **profile nodes** (which we imagine we'll have during Phase 3), so each profile is a Bitsocial full node, most of them via public RPC (**Forge RPC**).
>
> Also to decentralize CI — which is probably GitHub's most important feature — we'd probably use **centralized CI runner services via public RPC**, but the difference with GitHub is that on GitHub you're forced to use theirs, whereas on our GitHub-alternative Bitsocial client you'd be able to use **any CI runner service via public RPC, so there will be competition**.
>
> Most importantly, the social layer of GitHub is very good and valuable for open source to thrive, so Bitsocial can decentralize that fully. We could probably do a **hybrid, maybe even collab with Radicle**, who knows. It's not possible before Phase 3 at least, since it would require profile nodes as well as public RPC.

Everything below is research and structure built on top of that.

---

## 3. Why GitHub's social layer is the real prize

You can already self-host git (Gitea, GitLab, cgit) and you can already replicate git peer-to-peer (Radicle). The thing that has *never* been decentralized is the **social graph of open source**:

- **Profiles & reputation** — a developer's identity, contribution history, and credibility.
- **Following, stars, feeds** — how people discover what to work on and who to trust.
- **Explore / Trending / Topics** — how projects find contributors and users. (Notably, there's already a `github-explore-bitsocial-topic/` repo in the Bitsocial workspace — a fork of GitHub's Explore/Topics data — so this surface has already been on the radar.)
- **Discussions** — the open-ended community conversation around a project, separate from issues.
- **Sponsors** — funding flowing to maintainers.

This is **precisely the layer Bitsocial is built to decentralize.** Bitsocial communities, profiles, follows, feeds, discovery services, tipping/awards, and anti-spam challenges map almost one-to-one onto GitHub's social surfaces. The code-hosting part is the *solved* problem (git is already content-addressed, and Radicle already did the p2p replication). The social part is where Bitsocial is uniquely positioned — and where a centralized incumbent is most vulnerable, because a captured social layer is exactly what platform lock-in is made of.

---

## 4. Where this fits in the master plan

Short version (full text + dependency analysis in [`master-plan-context.md`](master-plan-context.md)):

- **Phase 1** — decentralize imageboards/forums (5chan, Seedit), launch first non-custodial RPC service (Forge), public RPC makes always-on p2p communities practical from mobile. *In progress.*
- **Phase 2** — Bitsocial Network: appchain financial rails (.bso domains, tipping, awards, monetization). → funds **Sponsors-equivalent** and grants.
- **Phase 3** — flagship profile-based app: **profiles, follows, feeds, communities, and profile nodes.** Each user can be a full p2p node, hosted via non-custodial RPC, movable to a Raspberry Pi anytime. → **this is the unlock.** GitHub-style profiles = profile nodes. No profile nodes ⇒ no decentralized GitHub.
- **Phase 4** — scale economies: **infrastructure pluralism** — competing RPCs, media hosts, discovery, moderation, profile-node hosting, all fundable. → **this is exactly the CI-runner-marketplace model** ("competing services via public RPC"), applied to compute.
- **Phase 5** — decentralize all social media: fund the **long tail** of clients (blogging, crowdfunding, YouTube alt, "every format too early for the first four phases," and *"tools that make existing communities easier to run"*). → **a developer-collaboration client lives here.**

So it's a **Phase 5 client** that is *only possible because of Phase 3's profile nodes + RPC* and *economically shaped by Phase 4's service competition*. That matches Tommaso's instinct exactly.

A useful observation: this is technically more than a "social client." It's a **collaboration client** — but it's built entirely from primitives the first four phases already produce (profile nodes, communities, public RPC, competing services, financial rails). It doesn't need new protocol; it needs the protocol to exist.

---

## 5. Radicle: the only existing pure-p2p forge

Full deep-dive in [`radicle-research.md`](radicle-research.md). The essentials:

**Is Radicle federated or pure p2p?** → **Pure p2p.** Tommaso wasn't sure; the answer is clear. Radicle's current protocol (**Heartwood**) has *"no clients or servers, only nodes,"* and every user runs one. Nodes are identified by public keys and replicate git repos via a **gossip protocol** + git's own protocol. There are no instances/accounts like ActivityPub — so it is **not** federation. The thing that *looks* federated is **seed nodes**: always-on nodes that keep repos available (the same role Bitsocial calls a "seeder" / full node). So: p2p architecture, with optional always-on seeds for availability — structurally close to Bitsocial.

**What Radicle does well (and we should not reinvent):**
- **Git-over-p2p replication** that actually works — this is genuinely hard, and they've shipped it.
- **Collaborative Objects (COBs)** — issues, patches (their PRs), and reviews stored *as signed git objects* using CRDTs, fully offline-capable and independently verifiable.
- **Self-certifying repos** with **per-repo delegates + a signature threshold** (a built-in multisig-style governance for who can authorize changes).
- A **CI broker spec** (see below).

**Where Radicle is weak (and Bitsocial is strong):**
- **Identity is bare** — a public key plus an optional, non-unique alias. No rich profile, no social graph, no reputation surface.
- **No consumer social layer** — COBs are great for code, but there's no following/feeds/Explore/Discussions-as-community experience for *people*.
- **High onboarding friction** — "every user runs a node." No mainstream non-custodial hosted path (which is exactly Bitsocial's Forge RPC).
- **Niche adoption** — strong tech, small user base.

The Venn diagram is almost suspiciously clean: **Radicle = code layer, no social layer. Bitsocial = social layer, no code layer.**

---

## 6. Proposed architecture

### 6.1 The mapping

| GitHub feature | How it's centralized today | Decentralized on Bitsocial |
| --- | --- | --- |
| **Profile** (repos, followers, contribution graph) | GitHub account | **Profile node** — a Bitsocial full node (Phase 3). Identity = keypair. Served via Forge RPC for non-self-hosters; movable to your own box anytime. |
| **Code / repo hosting** | GitHub servers | Git objects replicated p2p. Git is *already* a content-addressed Merkle DAG, so it fits either Radicle's Heartwood (gossip+git) **or** Bitsocial's IPFS content-addressing. Seeded by profile nodes + Forge + competing seeders. |
| **Discussions tab** | GitHub Discussions | **A Bitsocial community** — pure p2p, the exact primitive 5chan/Seedit already ship. *(Tommaso's core insight.)* |
| **Issues** | GitHub Issues | Radicle COBs **or** Bitsocial threads attached to the repo's community. |
| **Pull requests** | GitHub PRs | Radicle **patches** (COBs) for merge mechanics; Bitsocial threads for the review/discussion social layer. |
| **Stars / follows / feed / notifications** | GitHub social graph | Bitsocial's native social graph (flagship-app primitives, Phase 3). |
| **Explore / Trending / Topics** | GitHub Explore | Competing Bitsocial **discovery / indexing services** (Phase 4). The `github-explore-bitsocial-topic` data is a head start. |
| **CI/CD (Actions)** | GitHub Actions — **mandatory, theirs only** | **Competing CI runner services over public RPC** — use *any* provider. *(Tommaso's core insight; see 6.3.)* |
| **Packages / Releases** | GitHub Packages | Content-addressed artifacts seeded p2p + competing media hosts (Phase 4). |
| **Sponsors / funding** | GitHub Sponsors | Tipping/awards + Bitsocial Network rails (Phase 2) + decentralized grants (Phase 4/5). |
| **Org / governance** | GitHub org & permissions | Radicle per-repo **delegates + threshold** ⊕ Bitsocial community ownership (keypair-controlled). |

### 6.2 The code layer — three options (a real decision for build time)

1. **Adopt Radicle (Heartwood) for code, Bitsocial for everything social.** Use Heartwood (or a fork) for repo replication + patches/issues; wrap it in a Bitsocial client that adds profiles, Discussions-as-communities, feeds, discovery, and RPC onboarding. Bridge Radicle node keys ↔ Bitsocial profile-node keys. *Least reinvention, fastest to a real forge.*
2. **Build git-on-IPFS natively on Bitsocial's stack.** Store git objects via IPFS content-addressing, discover via HTTP routers, seed like any community; reimplement patches/issues as Bitsocial content types. *Most cohesive with the existing stack, but reinvents Radicle's hard-won git-over-p2p work — and it's the **only** option where Bitsocial's content-fade model would touch code, forcing you to build a durable pinned-seeding tier yourself (see §8). That's a strong reason to prefer the hybrid.*
3. **Bridge / collaborate with Radicle.** Treat Radicle as the code substrate and Bitsocial as the social substrate, with an explicit interop layer — and talk to Radworks (Radicle's funding DAO ran an open CI-integrations RFP, so they actively want integrators). *Potentially grant-fundable and mutually beneficial.*

**Lean:** don't reinvent git-over-p2p (option 1 or 3); *do* own the social layer outright — that's the differentiated, defensible part. Decide at build time based on how Heartwood has evolved by Phase 3-5.

### 6.3 Decentralized CI — the competition unlock

This is the sharpest part of the idea, so it's worth stating precisely.

- **GitHub:** CI (Actions) is bundled and you're locked into GitHub's runners and billing. It is arguably GitHub's deepest lock-in — the thing that's hardest to leave.
- **Radicle:** CI is *self-hosted per node* — a **broker** listens for repo-change events on your node and launches **adapters** (Concourse, a generic webhook adapter, or the standalone "Ambient" adapter). Sovereign, but high-friction and with no marketplace: you run your own.
- **Bitsocial-GitHub:** CI runner services **compete via public RPC**, exactly like Bitsocial's non-custodial community-hosting RPC model. A repo (or its delegates) points at one or more runner services; *anyone* can offer one; they compete on price, speed, hardware (GPU/ARM/large runners), trust model, and policy. Unlike GitHub you are never forced onto one provider — and unlike Radicle you don't have to operate the infrastructure yourself.

**Trust model for results** (the hard part of "someone else ran my CI"):
- Runners return **signed attestations** of build/test results.
- **Reproducible builds** let anyone independently re-verify a result.
- Delegates can require **N-of-M independent runners to agree** before a green check counts toward a merge — this generalizes Radicle's "delegates run CI to gain merge confidence" into a *market* of runners, and turns trust into a tunable policy instead of a platform decree.
- Optional hardened execution (TEEs) for runners that want to sell stronger guarantees.

This is just **Phase 4 "infrastructure pluralism" applied to compute.** It's the same shape as RPCs, media hosts, and discovery services competing — CI is one more service category.

### 6.4 Identity & anti-spam — already solved by Bitsocial

- **Identity:** one keypair = your profile node = your Radicle-style code identity. Bitsocial already treats identity as keypair-controlled and portable; Radicle already maps Node ID = Peer ID = Public Key and supports DID compatibility, so unification is plausible.
- **Spam on public repos** (a real GitHub pain — issue/PR spam): Bitsocial's **per-community challenge model** maps directly. A repo can require a challenge (captcha, rate-limit, token-gate, allowlist, payment, custom code) before an outside identity can open an issue or submit a patch — local, operator-defined, no platform-level super-admin.

### 6.5 GitHub mirroring as the onboarding path

Asking a project to migrate is the hardest sell. Asking it to mirror costs nothing: the repository stays on GitHub, a mirror keeps a p2p copy in sync, and the team keeps pushing where it already pushes. [open-git](https://open-git.com/home), a self-hosted (not decentralized) code host, leads its pitch with this, and the idea transfers directly.

- **No migration step.** It is plain git on both ends, so every commit, branch, and tag is identical. Stopping the mirror loses nothing, because the repository is whole in both places.
- **The social layer arrives first.** A mirrored repo gets a project page, a Discussions community, and profile links on day one, before anyone moves issues, pull requests, or CI.
- **Mirrors are one more replaceable service.** A mirror can run on the maintainer's own node or be offered over public RPC by competing providers, like seeders and CI runners.
- **One side is canonical per ref.** Two-way sync needs a rule for diverging pushes. The simplest is fast-forward only, with GitHub canonical until the maintainers flip it. The flip is the actual migration, and by then it is a setting, not a project.
- **Code first.** Mirroring refs is easy. Mirroring issues and pull requests means two canonical states (see §8), so those stay on GitHub until a project switches.

### 6.6 Agent session records that travel with the code

A growing share of commits is written by coding agents, and review then depends on what the agent was told as much as on the diff. open-git captures the agent session (prompts, transcript, tool calls) and stores it on a metadata branch inside the repository, in a format compatible with [Entire](https://entire.io), then shows it in the pull request timeline.

This fits a p2p forge better than a hosted one, because a metadata branch is ordinary git data:

- It replicates with the repository over the code layer, so no forge database holds the record and no provider can withhold it.
- It can be signed by the same key as the commits, so "this agent session produced this commit" is verifiable by anyone.
- Any client can render it. A client that ignores the branch still works.

Session transcripts can contain secrets and private context, so capture should be opt-in per repository and off by default for public ones, as open-git does.

---

## 7. Hybrid & collaborating with Radicle

The "maybe collab with Radicle" instinct is sound, and there's a concrete hook: **Radworks** (Radicle's funding DAO, formerly Radicle DAO, backed by the **RAD** token treasury) funds ecosystem work via grants and has historically issued open RFPs (including for CI integrations). A Bitsocial social-and-onboarding layer on top of Radicle's code substrate is:

- **Complementary, not competitive** — we'd bring the social layer + mainstream RPC onboarding they lack; they bring the git-over-p2p substrate + COBs we'd otherwise reinvent.
- **Potentially grant-fundable** through Radworks.
- **A way to bootstrap a network** — existing Radicle repos could appear in the Bitsocial client on day one.

Worth at minimum a conversation before committing to a fully native build. (Decision can wait until Phase 3-5; the ecosystem will have moved by then.)

---

## 8. Hard problems / open questions (for build time)

1. **Durability is the code layer's job — not a Bitsocial problem.** *(Corrects an overstatement in the first draft.)* Bitsocial's "old content can fade" tradeoff only applies to **Bitsocial-hosted content = the social layer** (discussions, profiles, feeds), where fade is the normal, accepted social-media behavior. **Code never lives in Bitsocial** — it lives on the Radicle / git-over-p2p layer, which is built for durability (git keeps full history in every clone; seed nodes keep it available). So fade and source code never touch. The *only* place durability becomes your problem is **option 2 (git-on-IPFS native, §6.2)** — which is a real argument against it and for the hybrid. Optional refinement: a rare long-lived discussion that deserves code-like permanence (a design rationale, an accepted answer) can be pinned with the same code-layer durability if desired — an enhancement, not a requirement.
2. **CI result trust.** Signed attestations + reproducible builds + N-of-M runner consensus + optional TEEs (see 6.3). What's the default policy, and who sets it per repo?
3. **Code layer choice.** Adopt Radicle, build git-on-IPFS, or bridge (see 6.2)?
4. **Identity unification.** One key across Bitsocial profile node + Radicle code identity + DID? How does key rotation/recovery work for a *developer* identity people depend on?
5. **Code search at scale.** Search is heavy and centralizing by nature; likely a competing indexing-service category (Phase 4) rather than a protocol feature.
6. **Large binaries / LFS / release artifacts.** Content-addressed + competing media hosts, but needs a real design.
7. **Funding the commons.** Who pays for durable seeding + CI for unfunded OSS? (Bitsocial Network rails, Sponsors, decentralized grants — Phase 2/4/5.)
8. **Scope of v1.** Read-only mirror + Discussions first, or full collaboration from the start? (See staged path.)

---

## 9. A staged path (earliest-possible → full)

This lets pieces ship as the protocol matures, instead of waiting for everything:

- **v0 — Discussions, today-ish.** A Bitsocial community attachable to *any* existing repo (even a GitHub or Radicle one) as its "Discussions." The social layer is the part that's buildable earliest and is valuable standalone — a decentralized comment/community layer for OSS projects.
- **v1 — Profiles (needs Phase 3).** Profile nodes show a developer's repos + activity (mirror/read), with follows/feeds; Discussions are communities.
- **v2 — Real p2p repos.** Adopt Radicle or git-on-IPFS; patches/issues land (COBs or native). Existing projects arrive through GitHub mirroring (§6.5) instead of a migration, and agent session records (§6.6) ride along as a metadata branch.
- **v3 — CI marketplace (Phase 4 economics).** Competing runner services over public RPC, with the trust model in 6.3.
- **v4 — Sponsors/grants (Phase 2 rails).** Funding flows to maintainers and to durable seeding/CI for the commons.

---

## 10. Naming

The working name is **GitCommons**: the shared place for git that nobody owns. It is descriptive (git), it states the difference from GitHub (a commons has no owner, a hub has one), and it reads as the universal place for code rather than as a niche alternative.

**Bitsocial Forge** already names the operator and RPC service, so "forge" stays out of the product name.

The name uses "Git", which is a trademark of the Git project. The project is fully decentralized and GPL-3.0-or-later free software, so the name is used for now, and it can change if the Git project ever objects.

---

## 11. Prerequisites checklist

Before this is buildable, the network needs:

- [ ] **Profile nodes** (Phase 3) — the flagship profile-based client and profile-node infrastructure shipped.
- [ ] **Public/Forge RPC at scale** (Phase 3) — non-custodial hosted nodes so devs don't have to self-host.
- [ ] **Competing-services economy** (Phase 4) — the marketplace pattern that makes the CI-runner market real.
- [ ] **Bitsocial Network rails** (Phase 2) — for Sponsors/grants/durable-seeding funding (nice-to-have, not strictly blocking v0-v2).
- [ ] **A code-layer decision** — Radicle adopt/bridge vs git-on-IPFS native.
- [ ] **A code-layer durability tier** — handled *by the code layer* (Radicle/git seed nodes), not by Bitsocial. Only becomes a problem to solve if you pick git-on-IPFS native (§6.2 option 2).

---

## License

[GPL-3.0-or-later](LICENSE)
