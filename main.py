import asyncio
from scraping.navigator import scrapear_quotes
from exports.exporter import exportar_a_json

async def main():
    url = "https://quotes.toscrape.com/js/"
    resultados = await scrapear_quotes(url)
    exportar_a_json(resultados, nombre_archivo="quotes.json", carpeta="output")
    print(f"Scraping completado. {len(resultados)} citas extraídas.")

if __name__ == "__main__":
    asyncio.run(main())
