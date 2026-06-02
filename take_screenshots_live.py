import asyncio
from playwright.async_api import async_playwright

URL = "https://nnai.framer.ai/"
OUT = "brand/site-screens"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=1
        )
        await page.goto(URL, wait_until="networkidle", timeout=30000)
        await page.wait_for_timeout(4000)

        # Scroll through entire page slowly to trigger lazy loads and animations
        total = await page.evaluate("document.body.scrollHeight")
        step = 600
        y = 0
        while y < total:
            await page.evaluate(f"window.scrollTo(0, {y})")
            await page.wait_for_timeout(300)
            y += step
        await page.evaluate("window.scrollTo(0, 0)")
        await page.wait_for_timeout(1500)

        import os
        os.makedirs(OUT, exist_ok=True)

        # Full page — clip to actual content width to avoid blank sides
        await page.screenshot(
            path=f"{OUT}/00-full-page.png",
            full_page=True,
            type="png"
        )
        print("00-full-page.png")

        # Get page height and take viewport shots at each "screen"
        total_height = await page.evaluate("document.body.scrollHeight")
        viewport_height = 900
        screen_num = 1
        y = 0

        while y < total_height:
            await page.evaluate(f"window.scrollTo(0, {y})")
            await page.wait_for_timeout(600)
            await page.screenshot(path=f"{OUT}/{screen_num:02d}-scroll-{y}.png")
            print(f"{screen_num:02d}-scroll-{y}.png")
            y += viewport_height
            screen_num += 1

        await browser.close()

asyncio.run(main())
