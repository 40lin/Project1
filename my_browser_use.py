# 该文件用于备份Browser_use的mcp
from langchain_openai import ChatOpenAI
from my_browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv
from pydantic import SecretStr
from fastmcp import FastMCP

load_dotenv()
import asyncio
import os

mcp = FastMCP("server")


@mcp.tool
async def browser_use(task: str) -> str:
    """
    打开浏览器，完成任务
    参数:
        task: 任务
    """

    llm = ChatOpenAI(
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        model="qwen-turbo-latest",
        api_key="sk-3a9a8c8e53ce4f1d96cc00a39a9a4a91",
    )
    browser = Browser(
        config=BrowserConfig(
            # NOTE: you need to close your chrome browser - so that this can open your browser in debug mode
            browser_binary_path="C:\Program Files\Google\Chrome\Application\chrome.exe",
        )
    )
    agent = Agent(
        task=task,
        # message_context="",
        llm=llm,
        browser=browser,
    )
    result = await agent.run(max_steps=15)
    print(result)
    return result


if __name__ == "__main__":
    mcp.run(transport="sse")
