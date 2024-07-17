import asyncio

from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        page = await browser.new_page()
        page.on(
            "request", lambda request: print(f"Request: {request.method} {request.url}")
        )
        page.on(
            "response",
            lambda response: print(f"Response: {response.status} {response.url}"),
        )
        await page.goto(
            "https://www.skylinewebcams.com/webcam/espana/andalucia/almeria/playa-de-mojacar.html"
        )

        # Wait for the consent dialog and accept it
        await page.wait_for_selector("button:has-text('Consentir')")
        consent_button = await page.query_selector("button:has-text('Consentir')")
        await consent_button.click()
        await page.screenshot(path="example.png")
        input("Press any key to close the browser")
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
