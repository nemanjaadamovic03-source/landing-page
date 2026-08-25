# bar.md — "letters over the car" effect

Reference: Gauchère website, "PARISIENNE" hero row (dribbble shot, local copy fetched this session).
Mechanisms extracted from the reference, adapted to this brief (user explicitly wants a COLOR/accent
effect on the overlap — the reference itself is monochrome photography doing the work, so mechanism 2
below translates that intent rather than copying it literally).

1. Letters outside the subject render in the page's normal solid color — zero effect there, no fade-in.
2. Letters (or the portions of letters) that geometrically cross the subject's silhouette switch to a
   single deliberate accent treatment — not the same navy as the rest of the word, not multiple
   competing colors.
3. The accent-vs-normal boundary follows the subject's actual silhouette edge exactly (door line,
   roofline, wheel arch) — no soft blur, no rectangular box edge cutting across empty background.
4. The word is large enough that at least 3-4 letters have a meaningful portion (not just a corner
   pixel) crossing the subject's body.
5. The base word stays fully legible / high-contrast against the white section background outside the
   subject — the accent treatment never weakens that.
6. No new image asset required — the effect is derived from the same car cutout already on the page
   (its own alpha channel), so it stays maintainable without a design tool round-trip.
7. Effect still reads correctly at mobile width (390px) without the accent boundary breaking or
   drifting out of alignment with the car.
