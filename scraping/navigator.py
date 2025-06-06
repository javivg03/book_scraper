from playwright.async_api import async_playwright
from utils import esperar_humano

async def scrapear_quotes(url: str) -> list:
    resultados = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
            )
        )
        page = await context.new_page()

        await page.goto(url, timeout=60000)
        await esperar_humano()

        await page.wait_for_selector(".quote")

        # Captura de pantalla
        await page.screenshot(path="output/captura.png", full_page=True)

        citas = await page.query_selector_all(".quote")
        print(f"Se encontraron {len(citas)} citas")

        for cita in citas[:10]:
            try:
                texto_el = await cita.query_selector(".text")
                autor_el = await cita.query_selector(".author")
                tag_els = await cita.query_selector_all(".tag")

                texto = await texto_el.text_content() if texto_el else None
                autor = await autor_el.text_content() if autor_el else None
                tags = [await t.text_content() for t in tag_els] if tag_els else []

                resultados.append({
                    "texto": texto.strip() if texto else None,
                    "autor": autor.strip() if autor else None,
                    "tags": [t.strip() for t in tags],
                    "url": url
                })

            except Exception as e:
                print(f"Error extrayendo una cita: {e}")

        await browser.close()

    return resultados
