from contextlib import suppress
from pathlib import Path
import asyncio
import subprocess
import json
import sys
import time

import aiohttp

BASE_URL = "http://localhost:8080"
STATUS_URL = f"{BASE_URL}/etda/api/v1/status"


async def check_status():  # pragma: no cover
    """Check status."""
    async with aiohttp.ClientSession() as session:
        async with session.post(STATUS_URL) as resp:
            assert resp.status == 200        


if __name__ == "__main__":  # pragma: no cover
    try:
        FUNC = {
            f.__name__: f
            for f in [check_status, ]
        }.get(sys.argv[1])
        asyncio.get_event_loop().run_until_complete(FUNC(*sys.argv[2:]))
    except Exception as err:
        print(err)
        sys.exit(1)
    sys.exit(0)
