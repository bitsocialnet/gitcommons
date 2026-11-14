# Radicle research

Background research on [Radicle](https://radicle.dev/) — a mature pure-peer-to-peer code-collaboration stack ("sovereign forge") — to inform a Bitsocial GitHub alternative. Researched 2026-06-02.

---

## What Radicle is

Radicle is a peer-to-peer stack for code collaboration built **on top of Git**, designed to work without any centralized service like GitHub. Its current-generation protocol is called **Heartwood**. It bills itself as *"the sovereign forge."*

The core promise: a sovereign, censorship-resistant network where developers fully control their code and collaboration data, and the network survives as long as anyone runs a node.

---

## Is it federated or pure p2p?

**Pure p2p.** This was Tommaso's open question, and the answer is unambiguous from Radicle's own docs:

> *"There are no clients or servers; only nodes, and every user has to run their own. This ensures that there is no single point of failure, and the Radicle network can keep on existing as long as there are users to run nodes."*

- **Not federation.** There are no instances issuing accounts (unlike ActivityPub/Mastodon). Identity isn't granted by a server; it's a keypair you hold.
- **What can *look* federated:** **seed nodes** — always-on nodes that keep repositories available for others to fetch. They're an availability convenience, not an authority. This is the same role Bitsocial calls a **seeder** / full node. So both systems are "p2p with optional always-on seeds," which is part of why they fit together.

---

## Architecture (Heartwood)

- **Nodes identified by public keys.** "Node ID," "Peer ID," and "Public Key" are interchangeable terms. The keypair identifies peers *and* signs all published artifacts.
- **Discovery + replication via gossip.** A gossip protocol handles peer and repository discovery; **Git's own protocol** handles data replication. A node opens a secure connection to a peer and does a git fetch to pull the objects it wants.
- **Secure transport.** Connections use a **Noise XK** handshake (same pattern as the Lightning Network), with the Node ID as the static key.
- **Self-certifying repos.** Each repo has a unique ID and an **identity document** (canonical JSON at `refs/rad/id`) holding `name`, `description`, `defaultBranch`, the **delegates'** public keys, and a **signature threshold** — i.e., built-in multisig-style governance for who may authorize changes to the repo.
- **Replication condition.** Any node can locate, replicate, and verify any published repo *as long as at least one peer seeding it is online* — which is why seed nodes matter for availability.
- **Selective sync.** Inspired by Secure Scuttlebutt's pub/sub gossip, peers host and sync **only the data they care about**.

---

## Collaborative Objects (COBs) — the social/collaboration primitive

Git doesn't natively support discussing issues and patches, so Radicle extended it:

- **COBs = issues, patches (PRs), reviews, discussions, stored *as Git objects* inside the repo.** Each has its own Git Object ID (OID).
- Built on **CRDTs** (conflict-free replicated data types) for consistency, and every update is **cryptographically signed** so interactions are independently verifiable.
- **Fully offline-capable** — because they live in git's object database / the bare repo, not a server.
- Heartwood ships three predefined COBs — `issue`, `patch`, `id` — but the type system is **extensible**: users can customize them or define entirely new datatypes.
- "Patches" are Radicle's pull-request equivalent, supporting non-destructive updates and reviews tied to specific patch revisions.

**This is the part Bitsocial would most likely *reuse rather than rebuild*** — COBs are a solid, verifiable, offline model for issues/PRs. (Though Bitsocial could also model issues/PRs as its own content types if a native build is chosen.)

---

## Radicle CI (the broker model)

Directly relevant to the "decentralize CI" idea — and a useful contrast with the marketplace approach.

- **Architecture:** a **broker** listens for repo-change events on a node and launches the appropriate **adapter** per change, by configuration. Adapters exist for Concourse, a **generic webhook adapter** (to bolt on external CI), and an **Ambient** adapter (Jan 2025) that made Radicle CI viable as a standalone CI system.
- **Per-node opt-in, by interest:** each node decides what it runs CI for.
  - A repo's **delegates** might run CI on all patches to make merge decisions with more confidence.
  - A contributor might run CI only on their own patches.
  - A downstream user might run CI on projects they depend on, to decide whether it's safe to deploy.
- **Implication:** Radicle CI is **sovereign but self-operated** — there's no marketplace; you (or your delegates) run it. The Bitsocial twist is to turn this into **competing runner services reachable via public RPC**, so you get the sovereignty *without* having to run the infrastructure, plus price/speed/trust competition. The "delegates run CI for merge confidence" idea generalizes nicely into "require N-of-M independent runner attestations."

---

## Governance & funding (Radworks / RAD)

- Radicle's funding/governance organization is **Radworks** (formerly the Radicle DAO), with a treasury denominated in the **RAD** token.
- Radworks funds ecosystem development via **grants** and has historically issued **open RFPs** (including for CI integrations and a "decentralized CI/CD pipeline" grant track).
- **Why this matters for Bitsocial:** there's an existing, funded, integration-friendly DAO. A Bitsocial social/onboarding layer on top of Radicle's code substrate could plausibly be **grant-funded and welcomed** rather than seen as competition. (Treat specifics as "verify at build time" — tokenomics/DAO details drift.)

---

## Strengths vs. gaps (the case for a hybrid)

| | Radicle | Bitsocial |
| --- | --- | --- |
| Git-over-p2p replication | ✅ Mature (Heartwood) | ❌ Would need building (or adopt Radicle) |
| Issues/PRs/reviews | ✅ COBs (signed, CRDT, offline) | ➖ Could reuse COBs or model natively |
| Per-repo governance | ✅ Delegates + threshold | ➖ Community ownership (keypair) |
| CI | ✅ Self-hosted broker/adapters | 🎯 Competing runners via public RPC (the upgrade) |
| **Identity / profiles** | ❌ Bare pubkey + alias | ✅ Rich profiles = profile nodes (Phase 2) |
| **Social graph** (follow/feed/Explore) | ❌ None | ✅ Native (flagship app, Phase 2) |
| **Discussions as community** | ❌ None | ✅ Core primitive (5chan/Seedit) |
| **Mainstream onboarding** | ❌ Everyone runs a node | ✅ Non-custodial Forge RPC |
| **Anti-spam on public repos** | ➖ Limited | ✅ Per-community challenge model |
| **Funding rails** | ✅ Radworks/RAD grants | ✅ Bitsocial Network (Phase 3) + grants |

The overlap is small and the complementarity is large: **Radicle owns the code layer; Bitsocial owns the human layer.**

---

## Sources

- [Radicle — the sovereign forge (radicle.dev)](https://radicle.dev/)
- [Radicle Protocol Guide](https://radicle.dev/guides/protocol)
- [Radicle Protocol Overview — Heartwood Release (HackMD)](https://hackmd.io/@radicle/rJ2UH54P6)
- [heartwood repo (GitHub mirror)](https://github.com/radicle-dev/heartwood)
- [Radicle: peer-to-peer collaboration with Git (LWN.net)](https://lwn.net/Articles/966869/)
- [State of Radicle CI and where it's going: December 2025](https://blog.liw.fi/posts/2025/radicle-ci-status-quo/)
- [Radicle CI Integrations — Request for Proposals (HackMD)](https://hackmd.io/@radicle/HJja4EBt3)
- [Grant Application — Decentralized CI/CD Pipeline (Radworks Community)](https://community.radworks.org/t/grant-application-decentralized-ci-cd-pipeline/3251)
- [Radicle Pioneers Peer-to-Peer Code Collaboration (HackerNoon)](https://hackernoon.com/radicle-pioneers-peer-to-peer-code-collaboration)
