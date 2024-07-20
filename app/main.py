import asyncio

import uvicorn
from fastapi import FastAPI

from app.api.api import api_routers

app = FastAPI()

for api_router in api_routers:
    app.include_router(api_router, prefix="/api")


async def main():
    uvicorn.run(app="main:app", host='localhost', port=3000, reload=True)


if __name__ == "__main__":
    asyncio.run(main())
