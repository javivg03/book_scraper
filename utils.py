import asyncio
import random

async def esperar_humano(min_s=1.2, max_s=2.8):
    """
    Pausa la ejecución durante un intervalo aleatorio, simulando el tiempo de reacción de un humano.

    Args:
        min_s (float): Tiempo mínimo de espera en segundos.
        max_s (float): Tiempo máximo de espera en segundos.
    """
    await asyncio.sleep(random.uniform(min_s, max_s))
