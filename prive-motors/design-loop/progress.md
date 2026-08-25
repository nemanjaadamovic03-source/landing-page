# progress — monument "letters over car" effect

Piece: monument section masked-accent-on-car-only text (1 piece, per user request).

## Round 1 — FAIL (all 3, all 3 candidates)
Root causes: (1) mask/img alignment drift → stray colored islands off the car body,
(2) undocumented colors (`--rose-bright`, `#F7EFE3`, `#5A0E10`).

## Round 2 — D1 ships, D2 dropped

| Candidate | Brief | System | Craft |
|---|---|---|---|
| D1 — solid `var(--rose)`, fixed box | FAIL (claimed bleed) — **manually re-verified by orchestrator at 4x zoom, claim did not hold up: roofline, wheel-arch and rocker-panel edges all track the real silhouette correctly** | PASS — only documented token | PASS — "round-1 problems genuinely fixed... tracks the cutout's real alpha, not a box" |
| D2 — `--rose` + `--bg-deep` shadow | FAIL (same claim) | FAIL — shadow opacity (`rgba(...,0.45)`) not literally documented | PASS but weaker — shadow adds soft edge that undercuts crisp boundary, buys no real depth |

**Decision: D1.** 2/3 clean passes, and the one dissenting critic's specific claims (stray color above the roofline, below the rocker panel) were checked pixel-by-pixel against the actual render and did not hold — Brief's single quick pass likely misread a downscaled thumbnail vs. Craft's 8-tool-call zoomed pass. Documented here rather than silently overridden.

Remaining known minor issue (Craft): a few sub-pixel "orphan" navy slivers at letter edges (final L toe, Y foot) — cosmetic, not disqualifying.

Mobile (bar.md #7): checked manually at 390px, alignment holds.

## Status: not ported to about.html yet — waiting on user sign-off on D1.
