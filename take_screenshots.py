import asyncio
from playwright.async_api import async_playwright

URL = "http://localhost:8765/nnai-sr.html"
OUT = "screenshots"

SECTIONS = [
    ("01-hero",         "#pocetna"),
    ("02-stats",        ".stats-band"),
    ("03-usluge",       "#usluge"),
    ("04-proces",       "#proces"),
    ("05-benefiti",     "#benefiti"),
    ("06-svedocanstva", "#svedocanstva"),
    ("07-cta",          ".cta-sec"),
    ("08-footer",       "footer"),
]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto(URL, wait_until="networkidle")

        # Disable all reveal animations so everything is visible
        await page.add_style_tag(content="""
            .reveal, .reveal * {
                opacity: 1 !important;
                transform: none !important;
                transition: none !important;
            }
            .service-card, .step, .benefit-item, .testimonial-card {
                opacity: 1 !important;
                transform: none !important;
            }
        """)

        # Scroll through entire page to trigger any JS-based reveals
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await page.wait_for_timeout(800)
        await page.evaluate("window.scrollTo(0, 0)")
        await page.wait_for_timeout(400)

        # Full page screenshot
        await page.screenshot(path=f"{OUT}/00-full-page.png", full_page=True)
        print("00-full-page.png")

        for name, selector in SECTIONS:
            try:
                el = await page.query_selector(selector)
                if el:
                    # Scroll element into view
                    await el.scroll_into_view_if_needed()
                    await page.wait_for_timeout(500)
                    await el.screenshot(path=f"{OUT}/{name}.png")
                    print(f"{name}.png")
                else:
                    print(f"SKIP {name} — selector not found: {selector}")
            except Exception as e:
                print(f"ERROR {name}: {e}")

        await browser.close()

asyncio.run(main())
