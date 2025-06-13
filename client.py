import asyncio
from fastmcp import Client

client = Client("agent.py")


async def call_tool(task: str):
    async with client:
        result = await client.call_tool("browser_use", {"task": task})
        print(result)


asyncio.run(call_tool("打开浏览器并且访问https://www.bilibili.com/"))
