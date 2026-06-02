import asyncio, base64, os
from pathlib import Path
from playwright.async_api import async_playwright

BASE = Path(__file__).parent
LOGO_B64 = (BASE / "_logo_b64.txt").read_text().strip()
LOGO_SRC = f"data:image/png;base64,{LOGO_B64}"

# ──────────────────────────────────────────
# BRAND GUIDELINES HTML
# ──────────────────────────────────────────
GUIDELINES_HTML = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;600;700;900&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{
    background:#000;
    color:#fff;
    font-family:'Inter',sans-serif;
    width:1400px;
    padding:0;
  }}

  /* ── HEADER ── */
  .header{{
    background:linear-gradient(135deg,#111 0%,#0a0a0a 100%);
    border-bottom:1px solid rgba(255,255,255,.08);
    padding:52px 80px 48px;
    display:flex;
    align-items:center;
    justify-content:space-between;
  }}
  .header-left .eyebrow{{
    font-size:11px;font-weight:700;letter-spacing:.18em;
    text-transform:uppercase;color:rgba(255,255,255,.4);
    margin-bottom:10px;
  }}
  .header-left h1{{
    font-family:'Figtree',sans-serif;
    font-size:58px;font-weight:900;line-height:1;
    letter-spacing:-.04em;color:#fff;
  }}
  .header-left h1 span{{
    background:linear-gradient(229deg,#e8188c 0%,#8030d0 50%,#2840ff 100%);
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;
    background-clip:text;
  }}
  .header-left .sub{{
    font-size:15px;color:rgba(255,255,255,.45);
    margin-top:10px;letter-spacing:.02em;
  }}
  .header-right img{{
    width:140px;height:140px;object-fit:contain;
  }}
  .logo-img{{
    filter:hue-rotate(-28deg) saturate(1.72) brightness(0.87) contrast(1.32);
  }}

  /* ── SECTION LABEL ── */
  .sec-label{{
    font-size:10px;font-weight:700;letter-spacing:.2em;
    text-transform:uppercase;
    color:#e8188c;
    margin-bottom:6px;
  }}

  /* ── DIVIDER LINE ── */
  .divider{{
    border:none;border-top:1px solid rgba(255,255,255,.07);
    margin:0;
  }}

  /* ── 2-COL SECTION ── */
  .two-col{{
    display:grid;
    grid-template-columns:1fr 1fr;
    border-bottom:1px solid rgba(255,255,255,.07);
  }}
  .two-col .col{{
    padding:52px 80px;
  }}
  .two-col .col:first-child{{
    border-right:1px solid rgba(255,255,255,.07);
  }}

  /* ── LOGO DISPLAY ── */
  .logo-display{{
    display:flex;flex-direction:column;align-items:flex-start;gap:20px;
    margin-top:28px;
  }}
  .logo-display img{{width:100px;height:100px;object-fit:contain;}}
  .logo-wordmark{{
    font-family:'Figtree',sans-serif;
    font-size:48px;font-weight:900;letter-spacing:-.05em;
    background:linear-gradient(229deg,#e8188c 0%,#8030d0 50%,#2840ff 100%);
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  }}
  .logo-specs{{margin-top:8px;}}
  .logo-specs p{{font-size:12px;color:rgba(255,255,255,.4);line-height:1.8;}}
  .logo-specs span{{font-family:monospace;font-size:11px;color:rgba(255,255,255,.3);}}

  /* ── LOGO VARIATIONS ── */
  .variations{{
    display:flex;flex-direction:column;gap:14px;
    margin-top:28px;
  }}
  .var-row{{display:flex;gap:14px;}}
  .var-box{{
    flex:1;border-radius:12px;
    border:1px solid rgba(255,255,255,.1);
    overflow:hidden;
  }}
  .var-preview{{
    height:90px;
    display:flex;align-items:center;justify-content:center;gap:14px;
    padding:0 20px;
  }}
  .var-preview.dark{{background:#000;}}
  .var-preview.light{{background:#fff;}}
  .var-preview.purple{{background:linear-gradient(135deg,#1a0a2e,#0a0a0a);}}
  .var-preview img{{width:44px;height:44px;object-fit:contain;}}
  .var-preview .wm{{
    font-family:'Figtree',sans-serif;font-size:26px;font-weight:900;letter-spacing:-.04em;
  }}
  .var-preview .wm.grad{{
    background:linear-gradient(229deg,#e8188c,#2840ff);
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  }}
  .var-preview .wm.white{{color:#fff;}}
  .var-preview .wm.dark-text{{color:#000;}}
  .var-caption{{
    background:#161616;padding:10px 16px;border-top:1px solid rgba(255,255,255,.07);
    font-size:11px;color:rgba(255,255,255,.4);font-weight:500;
  }}

  /* ── CLEARSPACE ── */
  .clearspace-sec{{
    padding:52px 80px;
    border-bottom:1px solid rgba(255,255,255,.07);
  }}
  .clearspace-demo{{
    margin-top:28px;
    display:flex;align-items:center;gap:60px;
  }}
  .clearspace-box{{
    position:relative;
    display:inline-flex;
    align-items:center;justify-content:center;
    width:220px;height:220px;
  }}
  .clearspace-box .outer{{
    position:absolute;inset:0;
    border:1.5px dashed rgba(232,24,140,.35);
    border-radius:4px;
  }}
  .clearspace-box .inner{{
    position:absolute;inset:32px;
    border:1.5px dashed rgba(232,24,140,.6);
    border-radius:4px;
    background:rgba(80,48,208,.06);
  }}
  .clearspace-box img{{
    position:relative;z-index:1;
    width:100px;height:100px;object-fit:contain;
  }}
  .clearspace-label{{
    position:absolute;
    font-size:9px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
    color:rgba(232,24,140,.6);
  }}
  .clearspace-label.top{{top:6px;left:50%;transform:translateX(-50%)}}
  .clearspace-label.bottom{{bottom:6px;left:50%;transform:translateX(-50%)}}
  .clearspace-label.left{{left:6px;top:50%;transform:translateY(-50%) rotate(-90deg)}}
  .clearspace-label.right{{right:6px;top:50%;transform:translateY(-50%) rotate(90deg)}}
  .clearspace-rules{{max-width:420px;}}
  .clearspace-rules h3{{
    font-family:'Figtree',sans-serif;font-size:18px;font-weight:700;
    margin-bottom:14px;
  }}
  .clearspace-rules ul{{list-style:none;display:flex;flex-direction:column;gap:10px;}}
  .clearspace-rules ul li{{
    font-size:13px;color:rgba(255,255,255,.6);
    display:flex;align-items:flex-start;gap:10px;line-height:1.5;
  }}
  .clearspace-rules ul li::before{{content:'→';color:#2840ff;flex-shrink:0;}}

  /* ── COLOR PALETTE ── */
  .palette-sec{{
    padding:52px 80px;
    border-bottom:1px solid rgba(255,255,255,.07);
  }}
  .swatches{{
    display:grid;
    grid-template-columns:repeat(5,1fr);
    gap:14px;
    margin-top:28px;
  }}
  .swatch-card{{
    border-radius:14px;overflow:hidden;
    border:1px solid rgba(255,255,255,.08);
  }}
  .swatch-color{{height:80px;}}
  .swatch-info{{
    background:#161616;padding:12px;
    border-top:1px solid rgba(255,255,255,.07);
  }}
  .swatch-name{{font-size:12px;font-weight:600;margin-bottom:3px;}}
  .swatch-hex{{font-family:monospace;font-size:11px;color:rgba(255,255,255,.45);margin-bottom:2px;}}
  .swatch-role{{font-size:10px;color:rgba(255,255,255,.3);}}

  .gradient-row{{
    margin-top:14px;
    border-radius:12px;overflow:hidden;
    border:1px solid rgba(255,255,255,.08);
  }}
  .gradient-bar{{
    height:72px;
    background:linear-gradient(90deg,#e8188c 0%,#8030d0 50%,#2840ff 100%);
    display:flex;align-items:center;justify-content:space-between;
    padding:0 28px;
  }}
  .gradient-bar span{{font-family:monospace;font-size:13px;font-weight:600;color:rgba(0,0,0,.65);}}
  .gradient-meta{{
    background:#161616;padding:14px 20px;
    border-top:1px solid rgba(255,255,255,.07);
    display:flex;justify-content:space-between;align-items:center;
  }}
  .gradient-meta .label{{font-size:13px;font-weight:600;}}
  .gradient-meta .code{{font-family:monospace;font-size:11px;color:rgba(255,255,255,.35);}}

  /* ── TYPOGRAPHY ── */
  .type-sec{{
    padding:52px 80px;
    border-bottom:1px solid rgba(255,255,255,.07);
  }}
  .font-cards{{
    display:grid;grid-template-columns:1fr 1fr;gap:16px;
    margin-top:28px;
  }}
  .font-card{{
    background:#141414;
    border:1px solid rgba(255,255,255,.08);
    border-radius:14px;
    padding:28px 28px 24px;
  }}
  .font-card .role{{
    font-size:10px;font-weight:700;letter-spacing:.15em;text-transform:uppercase;
    color:#e8188c;margin-bottom:14px;
  }}
  .font-card .big-ab{{
    font-size:64px;font-weight:900;line-height:1;
    margin-bottom:10px;color:rgba(255,255,255,.9);
  }}
  .font-card .name-weight{{
    font-size:13px;font-weight:600;
    background:linear-gradient(229deg,#e8188c,#2840ff);
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
    margin-bottom:10px;
  }}
  .font-card .alphabet{{
    font-size:14px;color:rgba(255,255,255,.45);
    line-height:1.8;letter-spacing:.02em;margin-bottom:14px;
  }}
  .font-card .weights{{display:flex;flex-wrap:wrap;gap:6px;}}
  .weight-pill{{
    font-size:11px;
    background:rgba(255,255,255,.06);
    border:1px solid rgba(255,255,255,.1);
    border-radius:20px;padding:3px 12px;
    color:rgba(255,255,255,.6);
  }}
  .type-scale{{
    margin-top:20px;
    background:#141414;border:1px solid rgba(255,255,255,.08);border-radius:14px;
    overflow:hidden;
  }}
  .scale-row{{
    display:flex;align-items:baseline;
    padding:14px 28px;
    border-bottom:1px solid rgba(255,255,255,.05);
  }}
  .scale-row:last-child{{border-bottom:none;}}
  .scale-meta{{
    min-width:110px;font-size:10px;font-family:monospace;
    color:rgba(255,255,255,.3);flex-shrink:0;line-height:1.6;
  }}
  .scale-sample{{color:rgba(255,255,255,.9);font-family:'Figtree',sans-serif;}}

  /* ── BUTTONS & ICONS ── */
  .bottom-sec{{
    display:grid;grid-template-columns:1fr 1fr;
    border-bottom:1px solid rgba(255,255,255,.07);
  }}
  .bottom-col{{padding:52px 80px;}}
  .bottom-col:first-child{{border-right:1px solid rgba(255,255,255,.07);}}

  .btn-showcase{{
    display:flex;flex-direction:column;gap:16px;margin-top:28px;
  }}
  .btn{{
    display:inline-flex;align-items:center;gap:8px;
    padding:13px 26px;border-radius:8px;
    font-family:'Inter',sans-serif;font-size:14px;font-weight:600;
    border:none;width:fit-content;cursor:default;
  }}
  .btn-nav{{
    background:#7c3aed;color:#fff;
    border-radius:8px;
    padding:10px 22px;font-size:14px;
  }}
  .btn-primary{{
    background:#7c3aed;
    color:#fff;
    border-radius:8px;
    box-shadow:0 4px 20px rgba(124,58,237,.4);
  }}
  .btn-secondary{{
    background:transparent;color:#fff;
    border-radius:8px;
    border:1px solid rgba(255,255,255,.25);
  }}
  .btn-pill{{
    background:#7c3aed;color:#fff;
    border-radius:50px;
    padding:13px 28px;
    box-shadow:0 4px 20px rgba(124,58,237,.4);
  }}
  .btn-spec{{font-size:11px;color:rgba(255,255,255,.3);font-family:monospace;margin-top:4px;}}

  .icon-grid{{
    display:grid;grid-template-columns:repeat(6,1fr);gap:12px;
    margin-top:28px;
  }}
  .icon-box{{
    background:#141414;border:1px solid rgba(255,255,255,.08);border-radius:10px;
    aspect-ratio:1;display:flex;align-items:center;justify-content:center;
    font-size:22px;
  }}

  /* ── UI COMPONENTS ── */
  .ui-sec{{
    padding:52px 80px;
    border-bottom:1px solid rgba(255,255,255,.07);
  }}
  .ui-grid{{
    display:grid;grid-template-columns:1fr 1fr;gap:32px;
    margin-top:28px;
  }}
  .ui-block{{}}
  .ui-block-title{{
    font-size:10px;font-weight:700;letter-spacing:.15em;text-transform:uppercase;
    color:rgba(255,255,255,.3);margin-bottom:14px;
  }}

  /* Nav demo */
  .nav-demo{{
    background:#000;
    border:1px solid rgba(255,255,255,.1);
    border-radius:12px;
    overflow:hidden;
  }}
  .nav-inner{{
    border-bottom:1px solid rgba(255,255,255,.08);
    padding:0 24px;height:54px;
    display:flex;align-items:center;justify-content:space-between;
  }}
  .nav-logo{{
    display:flex;align-items:center;gap:10px;
  }}
  .nav-logo img{{width:28px;height:28px;object-fit:contain;}}
  .nav-logo span{{
    font-family:'Figtree',sans-serif;font-size:18px;font-weight:900;
    letter-spacing:-.04em;color:#fff;
  }}
  .nav-links{{
    display:flex;gap:24px;
  }}
  .nav-links a{{
    font-size:13px;color:rgba(255,255,255,.75);text-decoration:none;
  }}
  .nav-cta{{
    background:#7c3aed;color:#fff;
    padding:8px 18px;border-radius:8px;
    font-size:13px;font-weight:600;
    font-family:'Inter',sans-serif;
  }}

  /* Section badges */
  .badges-demo{{
    display:flex;flex-wrap:wrap;gap:8px;
    margin-top:4px;
  }}
  .site-badge{{
    display:inline-flex;align-items:center;
    padding:6px 14px;
    background:#161616;
    border:1px solid rgba(255,255,255,.15);
    border-radius:50px;
    font-size:12px;font-weight:500;color:#fff;
    font-family:'Inter',sans-serif;
  }}

  /* Hero orb */
  .hero-demo{{
    background:#000;border:1px solid rgba(255,255,255,.1);border-radius:12px;
    height:160px;
    display:flex;align-items:center;justify-content:center;
    position:relative;overflow:hidden;
  }}
  .hero-orb{{
    width:120px;height:120px;
    border-radius:50%;
    background:radial-gradient(circle at 40% 40%, rgba(80,48,208,.9) 0%, rgba(60,20,100,.6) 50%, transparent 80%);
    filter:blur(20px);
    position:absolute;
    top:50%;left:50%;transform:translate(-50%,-50%);
  }}
  .hero-text{{
    position:relative;z-index:1;text-align:center;
  }}
  .hero-text h3{{font-family:'Figtree',sans-serif;font-size:22px;font-weight:900;letter-spacing:-.03em;margin-bottom:6px;}}
  .hero-text p{{font-size:12px;color:rgba(255,255,255,.55);}}

  /* Trust bar */
  .trust-demo{{
    background:#000;border:1px solid rgba(255,255,255,.1);border-radius:12px;
    padding:20px 24px;
    display:flex;align-items:center;gap:8px;
  }}
  .trust-label{{font-size:11px;color:rgba(255,255,255,.3);margin-right:8px;white-space:nowrap;}}
  .trust-logo{{
    background:#161616;border:1px solid rgba(255,255,255,.08);border-radius:8px;
    padding:8px 16px;font-size:12px;font-weight:600;color:rgba(255,255,255,.6);
    font-family:'Inter',sans-serif;
  }}

  /* ── CARD COMPONENTS ── */
  .cards-sec{{
    padding:52px 80px;
    border-bottom:1px solid rgba(255,255,255,.07);
  }}
  .cards-grid{{
    display:grid;grid-template-columns:1fr 1fr;gap:24px;
    margin-top:28px;
  }}
  .card-block-title{{
    font-size:10px;font-weight:700;letter-spacing:.15em;text-transform:uppercase;
    color:rgba(255,255,255,.3);margin-bottom:12px;
  }}

  /* Service card */
  .service-card{{
    background:#141414;
    border:1px solid rgba(255,255,255,.1);
    border-radius:14px;
    padding:28px;
  }}
  .service-tag{{
    display:inline-flex;padding:5px 12px;
    background:#0d0d0d;border:1px solid rgba(255,255,255,.12);
    border-radius:50px;font-size:11px;font-weight:500;
    color:rgba(255,255,255,.7);margin-bottom:14px;
  }}
  .service-card h3{{
    font-family:'Figtree',sans-serif;font-size:20px;font-weight:700;
    letter-spacing:-.02em;margin-bottom:10px;line-height:1.3;
  }}
  .service-card p{{
    font-size:13px;color:rgba(255,255,255,.55);line-height:1.6;margin-bottom:16px;
  }}
  .service-pills{{display:flex;flex-wrap:wrap;gap:6px;}}
  .service-pill{{
    display:inline-flex;padding:4px 12px;
    background:#1a1a1a;border:1px solid rgba(255,255,255,.1);
    border-radius:50px;font-size:11px;color:rgba(255,255,255,.6);
  }}

  /* Process step card */
  .process-card{{
    background:#141414;
    border:1px solid rgba(255,255,255,.1);
    border-radius:16px;
    padding:28px;
  }}
  .process-step-label{{
    font-size:11px;font-weight:600;color:rgba(255,255,255,.35);
    letter-spacing:.05em;text-transform:uppercase;margin-bottom:10px;
  }}
  .process-card h3{{
    font-family:'Figtree',sans-serif;font-size:22px;font-weight:700;
    letter-spacing:-.02em;margin-bottom:10px;
  }}
  .process-card p{{
    font-size:13px;color:rgba(255,255,255,.5);line-height:1.6;
  }}

  /* Benefit card */
  .benefit-card{{
    background:linear-gradient(180deg,#141414 0%,rgba(124,58,237,.12) 100%);
    border:1px solid rgba(255,255,255,.08);
    border-radius:14px;
    padding:24px;
  }}
  .benefit-icon{{
    font-size:22px;margin-bottom:12px;
  }}
  .benefit-card h3{{
    font-family:'Figtree',sans-serif;font-size:17px;font-weight:700;margin-bottom:8px;
  }}
  .benefit-card p{{
    font-size:12px;color:rgba(255,255,255,.5);line-height:1.6;
  }}

  /* CTA card */
  .cta-card{{
    background:linear-gradient(135deg,#1a0833 0%,#0d0028 60%,#120020 100%);
    border:1px solid rgba(80,48,208,.2);
    border-radius:20px;
    padding:48px;
    text-align:center;
  }}
  .cta-card h2{{
    font-family:'Figtree',sans-serif;font-size:32px;font-weight:900;
    letter-spacing:-.04em;margin-bottom:10px;line-height:1.2;
  }}
  .cta-card p{{font-size:14px;color:rgba(255,255,255,.55);margin-bottom:24px;}}

  /* FAQ card */
  .faq-card{{
    background:#0d0d0d;
    border:1px solid rgba(255,255,255,.08);
    border-radius:12px;
    padding:18px 22px;
    display:flex;align-items:center;justify-content:space-between;
    margin-bottom:8px;
  }}
  .faq-card span{{font-size:14px;color:rgba(255,255,255,.85);}}
  .faq-chevron{{font-size:16px;color:rgba(255,255,255,.3);}}

  /* Footer section */
  .footer-demo{{
    background:#000;
    border:1px solid rgba(255,255,255,.08);
    border-radius:14px;
    padding:32px;
  }}
  .footer-top{{
    display:flex;gap:48px;margin-bottom:24px;
  }}
  .footer-brand{{flex:1;}}
  .footer-brand .fl{{
    display:flex;align-items:center;gap:10px;margin-bottom:10px;
  }}
  .footer-brand .fl img{{width:24px;height:24px;object-fit:contain;}}
  .footer-brand .fl span{{
    font-family:'Figtree',sans-serif;font-size:16px;font-weight:900;
    letter-spacing:-.04em;color:#fff;
  }}
  .footer-brand p{{font-size:12px;color:rgba(255,255,255,.4);line-height:1.6;}}
  .footer-col h4{{font-size:12px;font-weight:600;color:rgba(255,255,255,.6);margin-bottom:10px;}}
  .footer-col a{{display:block;font-size:12px;color:rgba(255,255,255,.4);margin-bottom:6px;}}
  .footer-bottom{{
    border-top:1px solid rgba(255,255,255,.07);padding-top:16px;
    display:flex;justify-content:space-between;align-items:center;
  }}
  .footer-bottom span{{font-size:11px;color:rgba(255,255,255,.25);}}

  /* ── BRAND RULES ── */
  .rules-sec{{
    padding:52px 80px;
    border-bottom:1px solid rgba(255,255,255,.07);
  }}
  .rules-grid{{
    display:grid;grid-template-columns:1fr 1fr;gap:20px;
    margin-top:28px;
  }}
  .rule-box{{
    border-radius:14px;
    border:1px solid;
    padding:24px;
  }}
  .rule-box.do{{
    background:rgba(34,197,94,.04);
    border-color:rgba(34,197,94,.2);
  }}
  .rule-box.dont{{
    background:rgba(239,68,68,.04);
    border-color:rgba(239,68,68,.2);
  }}
  .rule-tag{{
    display:inline-flex;align-items:center;gap:6px;
    font-size:10px;font-weight:700;letter-spacing:.15em;text-transform:uppercase;
    margin-bottom:14px;padding:4px 10px;border-radius:50px;
  }}
  .rule-tag.do{{background:rgba(34,197,94,.12);color:#4ade80;}}
  .rule-tag.dont{{background:rgba(239,68,68,.12);color:#f87171;}}
  .rule-box ul{{list-style:none;display:flex;flex-direction:column;gap:8px;}}
  .rule-box ul li{{
    font-size:13px;color:rgba(255,255,255,.7);
    display:flex;align-items:flex-start;gap:10px;line-height:1.5;
  }}
  .rule-box.do ul li::before{{content:'✓';color:#4ade80;font-weight:700;flex-shrink:0;}}
  .rule-box.dont ul li::before{{content:'✕';color:#f87171;font-weight:700;flex-shrink:0;}}

  /* ── FOOTER ── */
  .footer{{
    padding:32px 80px;
    display:flex;justify-content:space-between;align-items:center;
  }}
  .footer .logo-mark{{
    font-family:'Figtree',sans-serif;font-size:24px;font-weight:900;letter-spacing:-.04em;
    background:linear-gradient(229deg,#e8188c,#2840ff);
    -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  }}
  .footer .version{{font-size:12px;color:rgba(255,255,255,.25);}}
</style>
</head>
<body>

<!-- HEADER -->
<div class="header">
  <div class="header-left">
    <div class="eyebrow">— NNAI · AI Automation Agency</div>
    <h1>BRAND<br><span>GUIDELINES</span></h1>
    <div class="sub">Visual Identity System · v2.0 · 2026</div>
  </div>
  <div class="header-right">
    <img class="logo-img" class="logo-img" src="{LOGO_SRC}" alt="NNAI Logo">
  </div>
</div>

<!-- LOGO + VARIATIONS -->
<div class="two-col">
  <div class="col">
    <div class="sec-label">● COMPANY LOGO</div>
    <div class="logo-display">
      <img class="logo-img" class="logo-img" src="{LOGO_SRC}" alt="NNAI N mark">
      <div class="logo-wordmark">NNAI</div>
      <div class="logo-specs">
        <p>Font: <span>Figtree / 900 Black</span><br>
        Letter-spacing: <span>−0.05em</span><br>
        Gradient: <span>229° · #e8188c → #2840ff</span></p>
      </div>
    </div>
  </div>
  <div class="col">
    <div class="sec-label">● LOGO VARIATIONS</div>
    <div class="variations">
      <div class="var-box">
        <div class="var-preview dark">
          <img class="logo-img" class="logo-img" src="{LOGO_SRC}" alt="">
          <div class="wm grad">NNAI</div>
        </div>
        <div class="var-caption">Dark Background — Primarna upotreba</div>
      </div>
      <div class="var-row">
        <div class="var-box">
          <div class="var-preview light">
            <img class="logo-img" class="logo-img" src="{LOGO_SRC}" alt="">
            <div class="wm grad">NNAI</div>
          </div>
          <div class="var-caption">Light Background</div>
        </div>
        <div class="var-box">
          <div class="var-preview purple">
            <img class="logo-img" class="logo-img" src="{LOGO_SRC}" alt="">
            <div class="wm white">NNAI</div>
          </div>
          <div class="var-caption">Color Background</div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- CLEARSPACE -->
<div class="clearspace-sec">
  <div class="sec-label">● LOGO CLEARSPACE</div>
  <div class="clearspace-demo">
    <div class="clearspace-box">
      <div class="outer"></div>
      <div class="inner"></div>
      <span class="clearspace-label top">X</span>
      <span class="clearspace-label bottom">X</span>
      <span class="clearspace-label left">X</span>
      <span class="clearspace-label right">X</span>
      <img class="logo-img" class="logo-img" src="{LOGO_SRC}" alt="">
    </div>
    <div class="clearspace-rules">
      <h3>Minimum Clear Space</h3>
      <ul>
        <li>Uvek ostaviti minimum 1× visine logoa slobodnog prostora sa svih strana</li>
        <li>Ne stavljati tekst, ikonice ni druge elemente unutar zone X</li>
        <li>Na manjim veličinama (ispod 32px) koristiti samo N simbol</li>
        <li>Minimalna veličina wordmarka: 80px širine</li>
      </ul>
    </div>
  </div>
</div>

<!-- COLOR PALETTE -->
<div class="palette-sec">
  <div class="sec-label">● BRAND PALETTE</div>
  <div class="swatches">
    <div class="swatch-card">
      <div class="swatch-color" style="background:#7c3aed;"></div>
      <div class="swatch-info">
        <div class="swatch-name">CTA Purple</div>
        <div class="swatch-hex">#7c3aed</div>
        <div class="swatch-role">Dugmad i CTA akcenti</div>
      </div>
    </div>
    <div class="swatch-card">
      <div class="swatch-color" style="background:#e8188c;"></div>
      <div class="swatch-info">
        <div class="swatch-name">Pink Accent</div>
        <div class="swatch-hex">#e8188c</div>
        <div class="swatch-role">Logo gradient, hover</div>
      </div>
    </div>
    <div class="swatch-card">
      <div class="swatch-color" style="background:#8030d0;"></div>
      <div class="swatch-info">
        <div class="swatch-name">Gradient Mid</div>
        <div class="swatch-hex">#8030d0</div>
        <div class="swatch-role">Gradient prelaz</div>
      </div>
    </div>
    <div class="swatch-card">
      <div class="swatch-color" style="background:#000;border-bottom:1px solid rgba(255,255,255,.1);"></div>
      <div class="swatch-info">
        <div class="swatch-name">Black</div>
        <div class="swatch-hex">#000000</div>
        <div class="swatch-role">Primarna pozadina sajta</div>
      </div>
    </div>
    <div class="swatch-card">
      <div class="swatch-color" style="background:#141414;border-bottom:1px solid rgba(255,255,255,.08);"></div>
      <div class="swatch-info">
        <div class="swatch-name">Card BG</div>
        <div class="swatch-hex">#141414</div>
        <div class="swatch-role">Kartice i komponente</div>
      </div>
    </div>
    <div class="swatch-card">
      <div class="swatch-color" style="background:#161616;border-bottom:1px solid rgba(255,255,255,.08);"></div>
      <div class="swatch-info">
        <div class="swatch-name">Dark BG</div>
        <div class="swatch-hex">#161616</div>
        <div class="swatch-role">Sekundarna pozadina</div>
      </div>
    </div>
    <div class="swatch-card">
      <div class="swatch-color" style="background:#fff;"></div>
      <div class="swatch-info">
        <div class="swatch-name">White</div>
        <div class="swatch-hex">#ffffff</div>
        <div class="swatch-role">Primarni tekst</div>
      </div>
    </div>
    <div class="swatch-card">
      <div class="swatch-color" style="background:rgba(255,255,255,.55);position:relative;">
        <div style="position:absolute;inset:0;background:repeating-linear-gradient(45deg,#2a2a2a 0,#2a2a2a 8px,#1a1a1a 8px,#1a1a1a 16px);z-index:-1;"></div>
      </div>
      <div class="swatch-info">
        <div class="swatch-name">Body Text</div>
        <div class="swatch-hex">#ffffff · 55%</div>
        <div class="swatch-role">Opisi i body tekst</div>
      </div>
    </div>
    <div class="swatch-card">
      <div class="swatch-color" style="background:rgba(255,255,255,.1);position:relative;">
        <div style="position:absolute;inset:0;background:repeating-linear-gradient(45deg,#2a2a2a 0,#2a2a2a 8px,#1a1a1a 8px,#1a1a1a 16px);z-index:-1;"></div>
      </div>
      <div class="swatch-info">
        <div class="swatch-name">Border</div>
        <div class="swatch-hex">#ffffff · 10%</div>
        <div class="swatch-role">Ivice / separatori</div>
      </div>
    </div>
    <div class="swatch-card">
      <div class="swatch-color" style="background:linear-gradient(135deg,#1a0833,#0d0028);"></div>
      <div class="swatch-info">
        <div class="swatch-name">CTA Dark Purple</div>
        <div class="swatch-hex">#1a0833 → #0d0028</div>
        <div class="swatch-role">CTA sekcija pozadina</div>
      </div>
    </div>
  </div>
  <div class="gradient-row">
    <div class="gradient-bar">
      <span>#e8188c</span>
      <span>→</span>
      <span>#8030d0</span>
      <span>→</span>
      <span>#2840ff</span>
    </div>
    <div class="gradient-meta">
      <span class="label">Primary Brand Gradient</span>
      <span class="code">linear-gradient(229deg, #e8188c 0%, #8030d0 50%, #2840ff 100%)</span>
    </div>
  </div>
</div>

<!-- TYPOGRAPHY -->
<div class="type-sec">
  <div class="sec-label">● TYPOGRAPHY</div>
  <div class="font-cards">
    <div class="font-card">
      <div class="role">Display / Headings</div>
      <div class="big-ab" style="font-family:'Figtree',sans-serif;font-weight:900;">Ag</div>
      <div class="name-weight" style="font-family:'Figtree',sans-serif;">FIGTREE · SEMI-BOLD / BOLD / BLACK</div>
      <div class="alphabet" style="font-family:'Figtree',sans-serif;">
        ABCDEFGHIJKLM<br>NOPQRSTUVWXYZ<br>abcdefghijklm<br>nopqrstuvwxyz
      </div>
      <div class="weights">
        <span class="weight-pill" style="font-family:'Figtree';font-weight:600;">600 SemiBold</span>
        <span class="weight-pill" style="font-family:'Figtree';font-weight:700;">700 Bold</span>
        <span class="weight-pill" style="font-family:'Figtree';font-weight:900;">900 Black</span>
      </div>
    </div>
    <div class="font-card">
      <div class="role">Body / UI Text</div>
      <div class="big-ab" style="font-family:'Inter',sans-serif;font-weight:400;">Ag</div>
      <div class="name-weight" style="font-family:'Inter',sans-serif;">INTER · LIGHT / REGULAR / MEDIUM</div>
      <div class="alphabet" style="font-family:'Inter',sans-serif;">
        ABCDEFGHIJKLM<br>NOPQRSTUVWXYZ<br>abcdefghijklm<br>nopqrstuvwxyz
      </div>
      <div class="weights">
        <span class="weight-pill" style="font-family:'Inter';font-weight:300;">300 Light</span>
        <span class="weight-pill" style="font-family:'Inter';font-weight:400;">400 Regular</span>
        <span class="weight-pill" style="font-family:'Inter';font-weight:500;">500 Medium</span>
        <span class="weight-pill" style="font-family:'Inter';font-weight:600;">600 SemiBold</span>
      </div>
    </div>
  </div>
  <div class="type-scale">
    <div class="scale-row">
      <div class="scale-meta">70px / 900<br>−0.06em</div>
      <div class="scale-sample" style="font-size:70px;font-weight:900;letter-spacing:-.06em;line-height:1;">NNAI</div>
    </div>
    <div class="scale-row">
      <div class="scale-meta">45px / 900<br>−0.05em</div>
      <div class="scale-sample" style="font-size:45px;font-weight:900;letter-spacing:-.05em;line-height:1.1;">AI Automatizacija</div>
    </div>
    <div class="scale-row">
      <div class="scale-meta">28px / 700<br>−0.03em</div>
      <div class="scale-sample" style="font-size:28px;font-weight:700;letter-spacing:-.03em;">Sekcijski naslovi i podnaslovi</div>
    </div>
    <div class="scale-row">
      <div class="scale-meta">15px / 400<br>0em · 1.6lh</div>
      <div class="scale-sample" style="font-size:15px;font-weight:400;color:rgba(255,255,255,.55);font-family:'Inter',sans-serif;">Standardni body tekst za opise. Razmak između redova 1.6em za optimalnu čitljivost.</div>
    </div>
  </div>
</div>

<!-- BUTTONS + ICONOGRAPHY -->
<div class="bottom-sec">
  <div class="bottom-col">
    <div class="sec-label">● BUTTON STYLE</div>
    <div class="btn-showcase">
      <div>
        <button class="btn btn-nav">Book a call</button>
        <div class="btn-spec">Nav CTA · #7c3aed · border-radius: 8px · 10px 22px</div>
      </div>
      <div>
        <button class="btn btn-primary">Get in touch</button>
        <div class="btn-spec">Primary · #7c3aed · border-radius: 8px · shadow 40%</div>
      </div>
      <div>
        <button class="btn btn-secondary">View services</button>
        <div class="btn-spec">Secondary · transparent · 1px white 25% border · 8px</div>
      </div>
      <div>
        <button class="btn btn-pill">Book a call Today</button>
        <div class="btn-spec">CTA pill · #7c3aed · border-radius: 50px · hero / CTA sekcija</div>
      </div>
      <div style="margin-top:4px;font-size:12px;color:rgba(255,255,255,.25);line-height:1.8;">
        Font: Inter 600 · Size: 13–14px<br>
        Nav / Service buttons: 8px radius &nbsp;·&nbsp; CTA standalone: 50px radius
      </div>
    </div>
  </div>
  <div class="bottom-col">
    <div class="sec-label">● ICONOGRAPHY STYLE</div>
    <div style="margin-top:28px;font-size:13px;color:rgba(255,255,255,.4);margin-bottom:16px;">
      Ikone: Lucide Icons · stroke-width: 1.5 · size: 20–24px
    </div>
    <div class="icon-grid">
      <div class="icon-box">⚡</div>
      <div class="icon-box">🤖</div>
      <div class="icon-box">📊</div>
      <div class="icon-box">🔗</div>
      <div class="icon-box">💬</div>
      <div class="icon-box">🚀</div>
      <div class="icon-box">⚙️</div>
      <div class="icon-box">📧</div>
      <div class="icon-box">📅</div>
      <div class="icon-box">💡</div>
      <div class="icon-box">🌐</div>
      <div class="icon-box">🔒</div>
    </div>
    <div style="margin-top:16px;font-size:12px;color:rgba(255,255,255,.25);line-height:1.8;">
      Na tamnoj pozadini: rgba(255,255,255,0.8)<br>
      Akcentovane: #7c3aed / #e8188c<br>
      Benefit kartice: emoji ikone u white stilu
    </div>
  </div>
</div>

<!-- UI COMPONENTS -->
<div class="ui-sec">
  <div class="sec-label">● UI COMPONENTS — NAVIGACIJA I ELEMENTI</div>
  <div class="ui-grid">
    <div class="ui-block">
      <div class="ui-block-title">Navigation Bar</div>
      <div class="nav-demo">
        <div class="nav-inner">
          <div class="nav-logo">
            <img class="logo-img" class="logo-img" src="{LOGO_SRC}" alt="">
            <span>NNAI</span>
          </div>
          <div class="nav-links">
            <a href="#">Home</a>
            <a href="#">About</a>
            <a href="#">Contact</a>
          </div>
          <div class="nav-cta">Book a call</div>
        </div>
        <div style="height:48px;background:#000;display:flex;align-items:center;padding:0 24px;">
          <span style="font-size:11px;color:rgba(255,255,255,.3);font-family:monospace;">bg: #000 · border-bottom: 1px rgba(255,255,255,.08) · height: 54px</span>
        </div>
      </div>
    </div>
    <div class="ui-block">
      <div class="ui-block-title">Section Badges</div>
      <div style="background:#000;border:1px solid rgba(255,255,255,.1);border-radius:12px;padding:28px;">
        <div class="badges-demo">
          <div class="site-badge">Our Services</div>
          <div class="site-badge">Workflow Automation</div>
          <div class="site-badge">AI Assistant</div>
          <div class="site-badge">Sales &amp; Marketing</div>
          <div class="site-badge">Our Process</div>
          <div class="site-badge">Benefits</div>
          <div class="site-badge">Testimonials</div>
          <div class="site-badge">Custom Projects</div>
        </div>
        <div style="margin-top:16px;font-family:monospace;font-size:11px;color:rgba(255,255,255,.25);line-height:1.8;">
          bg: #161616 · border: 1px rgba(255,255,255,.15)<br>
          border-radius: 50px · padding: 6px 14px · Inter 500 12px
        </div>
      </div>
    </div>
    <div class="ui-block">
      <div class="ui-block-title">Hero Section — Decorative Orb</div>
      <div class="hero-demo">
        <div class="hero-orb"></div>
        <div class="hero-text">
          <h3>AI Automation That Works</h3>
          <p>for Your Business</p>
        </div>
      </div>
    </div>
    <div class="ui-block">
      <div class="ui-block-title">Trust Bar — Powered by Platforms</div>
      <div style="background:#000;border:1px solid rgba(255,255,255,.1);border-radius:12px;padding:28px 24px;display:flex;flex-direction:column;gap:12px;">
        <div class="trust-demo">
          <span class="trust-label">Powered by trusted tools &amp; platforms</span>
          <div class="trust-logo">OpenAI</div>
          <div class="trust-logo">Slack</div>
          <div class="trust-logo">Make</div>
          <div class="trust-logo">n8n</div>
        </div>
        <div style="font-family:monospace;font-size:11px;color:rgba(255,255,255,.25);">
          Logosi: grayscale / white opacity · bg: #161616 · border: rgba(255,255,255,.08)
        </div>
      </div>
    </div>
  </div>
</div>

<!-- CARD COMPONENTS -->
<div class="cards-sec">
  <div class="sec-label">● CARD COMPONENTS — SISTEM KARTICA</div>
  <div class="cards-grid">
    <div>
      <div class="card-block-title">Service Card</div>
      <div class="service-card">
        <div class="service-tag">Workflow Automation</div>
        <h3>Automate internal business workflows</h3>
        <p>We help you streamline internal operations by automating manual workflows like data entry, reporting, and approval chains.</p>
        <div class="service-pills">
          <div class="service-pill">Internal Task Bots</div>
          <div class="service-pill">100+ Automations</div>
        </div>
      </div>
      <div style="margin-top:8px;font-family:monospace;font-size:10px;color:rgba(255,255,255,.25);line-height:1.7;">
        bg: #141414 · border: 1px rgba(255,255,255,.1) · radius: 14px · p: 28px
      </div>
    </div>
    <div>
      <div class="card-block-title">Process Step Card</div>
      <div class="process-card">
        <div class="process-step-label">Step 1</div>
        <h3>Discovery &amp; Analysis</h3>
        <p>We assess your workflows, systems, and business needs to identify automation opportunities and define the right AI solutions.</p>
      </div>
      <div style="margin-top:8px;font-family:monospace;font-size:10px;color:rgba(255,255,255,.25);line-height:1.7;">
        bg: #141414 · border: 1px rgba(255,255,255,.1) · radius: 16px · p: 28px
      </div>
    </div>
    <div>
      <div class="card-block-title">Benefit Card</div>
      <div class="benefit-card">
        <div class="benefit-icon">⚡</div>
        <h3>Increased Productivity</h3>
        <p>Automation reduces manual work and repetitive tasks, allowing teams to focus on higher value activities.</p>
      </div>
      <div style="margin-top:8px;font-family:monospace;font-size:10px;color:rgba(255,255,255,.25);line-height:1.7;">
        bg: gradient #141414 → rgba(124,58,237,.12) · radius: 14px · p: 24px
      </div>
    </div>
    <div>
      <div class="card-block-title">FAQ Item</div>
      <div>
        <div class="faq-card">
          <span>What is AI automation?</span>
          <span class="faq-chevron">∨</span>
        </div>
        <div class="faq-card">
          <span>How can AI automation help my business?</span>
          <span class="faq-chevron">∨</span>
        </div>
        <div class="faq-card">
          <span>What industries can benefit?</span>
          <span class="faq-chevron">∨</span>
        </div>
      </div>
      <div style="margin-top:8px;font-family:monospace;font-size:10px;color:rgba(255,255,255,.25);line-height:1.7;">
        bg: #0d0d0d · border: 1px rgba(255,255,255,.08) · radius: 12px · p: 18px 22px
      </div>
    </div>
  </div>

  <!-- CTA Card full width -->
  <div style="margin-top:24px;">
    <div class="card-block-title">CTA Section Card</div>
    <div class="cta-card">
      <h2>Let AI do the Work so you can Scale Faster</h2>
      <p>Book a Call Today and Start Automating</p>
      <button class="btn btn-pill">Book a call</button>
    </div>
    <div style="margin-top:8px;font-family:monospace;font-size:10px;color:rgba(255,255,255,.25);line-height:1.7;">
      bg: linear-gradient(135deg, #1a0833, #0d0028) · border: 1px rgba(80,48,208,.2) · radius: 20px · p: 48px · text-align: center
    </div>
  </div>

  <!-- Footer demo -->
  <div style="margin-top:24px;">
    <div class="card-block-title">Footer Layout</div>
    <div class="footer-demo">
      <div class="footer-top">
        <div class="footer-brand">
          <div class="fl">
            <img class="logo-img" class="logo-img" src="{LOGO_SRC}" alt="">
            <span>NNAI</span>
          </div>
          <p>NNAI – Automate Smarter,<br>Optimize Faster, and Grow Stronger.</p>
        </div>
        <div class="footer-col">
          <h4>Links</h4>
          <a href="#">Services</a>
          <a href="#">Process</a>
          <a href="#">Benefits</a>
        </div>
        <div class="footer-col">
          <h4>Pages</h4>
          <a href="#">Home</a>
          <a href="#">About</a>
          <a href="#">Contact</a>
        </div>
        <div class="footer-col">
          <h4>Socials</h4>
          <a href="#">Instagram</a>
          <a href="#">Facebook</a>
          <a href="#">LinkedIn</a>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© 2026 NNAI · nnai.framer.ai</span>
        <span>bg: #000 (NE koristiti purple/dark-purple pozadinu)</span>
      </div>
    </div>
  </div>
</div>

<!-- BRAND RULES -->
<div class="rules-sec">
  <div class="sec-label">● BRAND RULES — ŠTA RADITI I ŠTA NE RADITI</div>
  <div class="rules-grid">
    <div class="rule-box do">
      <div class="rule-tag do">✓ DO</div>
      <ul>
        <li>Koristiti čistu crnu (#000) kao primarnu pozadinu celog sajta</li>
        <li>Koristiti purple (#7c3aed) kao boju CTA dugmadi — puna ispuna, bez gradienta</li>
        <li>Koristiti pill border-radius (50px) samo na standalone CTA dugmadima i section badge-ovima</li>
        <li>Koristiti 8px border-radius za dugmad u navigaciji i service sekcijama</li>
        <li>Koristiti benefit kartice sa subtilnim purple gradientom na dnu</li>
        <li>Koristiti dark UI mockup ilustracije umesto fotografija</li>
        <li>Gradient (#e8188c → #2840ff) koristiti isključivo na logou i CTA sekciji</li>
        <li>Footer pozadina: uvek čista crna (#000)</li>
        <li>Section labels: uvek pill badge sa #161616 background i rgba(255,255,255,.15) border</li>
      </ul>
    </div>
    <div class="rule-box dont">
      <div class="rule-tag dont">✕ DON'T</div>
      <ul>
        <li>Ne koristiti purple/dark-purple boju kao pozadinu footera</li>
        <li>Ne koristiti gradient na primary dugmetu u navigaciji — samo solid purple</li>
        <li>Ne koristiti realnu fotografiju (stock foto) u sekcijama — samo UI mokapi</li>
        <li>Ne mešati pill i rectangular button stil unutar iste sekcije</li>
        <li>Ne koristiti pink akcenat (#e8188c) van logoa bez jasnog razloga</li>
        <li>Ne stavljati logo "Made in Framer" badge na produkcijskom sajtu</li>
        <li>Ne koristiti testimonial kartice bez vizuelnog brand identiteta (cards moraju biti dark styled)</li>
        <li>Ne koristiti sive ili neutralne boje za section badge — uvek dark pill</li>
      </ul>
    </div>
  </div>
</div>

<!-- FOOTER -->
<div class="footer">
  <div class="logo-mark">NNAI</div>
  <div class="version">Brand Guidelines v2.0 · nnai.framer.ai · © 2026 NNAI. Sva prava zadržana.</div>
</div>

</body>
</html>"""

# ──────────────────────────────────────────
# LOGO VARIANTS HTML
# ──────────────────────────────────────────
def logo_html(bg_color, text_color_class, bg_label):
    wm_style = ""
    if text_color_class == "grad":
        wm_style = "background:linear-gradient(229deg,#e8188c,#8030d0,#2840ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;"
    elif text_color_class == "white":
        wm_style = "color:#fff;"
    else:
        wm_style = "color:#000;"

    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@900&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:800px;height:400px;background:{bg_color};
  display:flex;align-items:center;justify-content:center;
  gap:32px;font-family:'Figtree',sans-serif;}}
img{{width:120px;height:120px;object-fit:contain;}}
.wm{{font-size:64px;font-weight:900;letter-spacing:-.05em;{wm_style}}}
</style></head><body>
<img class="logo-img" class="logo-img" src="{LOGO_SRC}">
<div class="wm">NNAI</div>
</body></html>"""

LOGO_DARK_HTML   = logo_html("#000000", "grad", "Dark")
LOGO_LIGHT_HTML  = logo_html("#ffffff", "grad", "Light")

# ──────────────────────────────────────────
# COLORS HTML
# ──────────────────────────────────────────
COLORS_HTML = """<!DOCTYPE html><html><head><meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{width:1200px;background:#0d0d0d;padding:48px;font-family:'Inter',sans-serif;}
.title{font-size:11px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;
  color:rgba(255,255,255,.35);margin-bottom:28px;}
.row{display:flex;gap:14px;}
.swatch{flex:1;border-radius:12px;overflow:hidden;border:1px solid rgba(255,255,255,.08);}
.color{height:100px;}
.info{background:#141414;padding:14px;border-top:1px solid rgba(255,255,255,.07);}
.name{font-size:13px;font-weight:600;color:#fff;margin-bottom:3px;}
.hex{font-family:monospace;font-size:12px;color:rgba(255,255,255,.45);}
.grad-bar{height:80px;background:linear-gradient(90deg,#e8188c,#8030d0,#2840ff);margin-top:14px;border-radius:12px;}
</style></head><body>
<div class="title">NNAI — Color Palette</div>
<div class="row">
  <div class="swatch"><div class="color" style="background:#2840ff"></div>
    <div class="info"><div class="name">Purple Primary</div><div class="hex">#2840ff</div></div></div>
  <div class="swatch"><div class="color" style="background:#e8188c"></div>
    <div class="info"><div class="name">Pink Accent</div><div class="hex">#e8188c</div></div></div>
  <div class="swatch"><div class="color" style="background:#8030d0"></div>
    <div class="info"><div class="name">Gradient Mid</div><div class="hex">#8030d0</div></div></div>
  <div class="swatch"><div class="color" style="background:#000;border-bottom:1px solid rgba(255,255,255,.1)"></div>
    <div class="info"><div class="name">Black</div><div class="hex">#000000</div></div></div>
  <div class="swatch"><div class="color" style="background:#0d0d0d;border-bottom:1px solid rgba(255,255,255,.08)"></div>
    <div class="info"><div class="name">Dark BG</div><div class="hex">#0d0d0d</div></div></div>
  <div class="swatch"><div class="color" style="background:#fff"></div>
    <div class="info"><div class="name">White</div><div class="hex">#ffffff</div></div></div>
  <div class="swatch">
    <div class="color" style="background:rgba(255,255,255,.75);position:relative;">
      <div style="position:absolute;inset:0;background:repeating-linear-gradient(45deg,#2a2a2a 0,#2a2a2a 8px,#1a1a1a 8px,#1a1a1a 16px);z-index:-1;"></div>
    </div>
    <div class="info"><div class="name">Subtle White</div><div class="hex">#fff · 75%</div></div></div>
  <div class="swatch">
    <div class="color" style="background:rgba(255,255,255,.1);position:relative;">
      <div style="position:absolute;inset:0;background:repeating-linear-gradient(45deg,#2a2a2a 0,#2a2a2a 8px,#1a1a1a 8px,#1a1a1a 16px);z-index:-1;"></div>
    </div>
    <div class="info"><div class="name">Border</div><div class="hex">#fff · 10%</div></div></div>
</div>
<div class="grad-bar"></div>
</body></html>"""


# ──────────────────────────────────────────
# RENDER
# ──────────────────────────────────────────
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()

        async def shot(html_str, out_path, w, h, full_page=False):
            page = await browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
            await page.set_content(html_str, wait_until="networkidle")
            await page.wait_for_timeout(1200)
            await page.screenshot(path=str(out_path), full_page=full_page)
            await page.close()
            print(f"  OK {out_path.name}")

        print("Generating brand assets...")
        await shot(GUIDELINES_HTML,   BASE / "nnai-brand-guidelines.png",  1400, 900, full_page=True)
        await shot(LOGO_DARK_HTML,    BASE / "nnai-logo-dark.png",          800, 400)
        await shot(LOGO_LIGHT_HTML,   BASE / "nnai-logo-light.png",         800, 400)
        await shot(COLORS_HTML,       BASE / "nnai-colors.png",            1200, 340, full_page=True)

        await browser.close()

    # cleanup
    (BASE / "_logo_b64.txt").unlink(missing_ok=True)
    (BASE / "_render.html").unlink(missing_ok=True)
    print("Done!")

asyncio.run(main())
