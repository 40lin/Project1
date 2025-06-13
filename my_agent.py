# 该文件用于测试Browse_use
from langchain_openai import ChatOpenAI
from my_browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv
from pydantic import SecretStr

load_dotenv()
import asyncio
import os

api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-turbo-latest",
    api_key=SecretStr(api_key),
)
browser = Browser(
    config=BrowserConfig(
        # NOTE: you need to close your chrome browser - so that this can open your browser in debug mode
        browser_binary_path="C:\Program Files\Google\Chrome\Application\chrome.exe",
    )
)


async def main():
    agent = Agent(
        task="""打开https://www.bilibili.com/,返回视频的标题""",
        # message_context="",
        llm=llm,
        browser=browser,
    )
    result = await agent.run(max_steps=15)
    print(result)
    await browser.close()
    input("Press Enter to close...")


asyncio.run(main())
