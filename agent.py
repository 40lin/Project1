# 不断改进版
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig, Controller
from dotenv import load_dotenv
from pydantic import SecretStr, BaseModel
from fastmcp import FastMCP
from typing import List

load_dotenv()
import asyncio
import os

mcp = FastMCP("server")

# 定义视频标题的Pydantic模型
class VideoTitle(BaseModel):
    title: str

class VideoTitles(BaseModel):
    titles: List[VideoTitle]

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
    
    # 创建一个Browser实例
    browser = Browser(
        config=BrowserConfig(
            # NOTE: you need to close your chrome browser - so that this can open your browser in debug mode
            browser_binary_path="C:\Program Files\Google\Chrome\Application\chrome.exe",
        )
    )
    
    # 创建Controller并指定输出模型
    controller = Controller(output_model=VideoTitles)
    
    # 将controller传递给Agent
    agent = Agent(
        task=task,
        # message_context="",
        llm=llm,
        browser=browser,
        controller=controller
    )
    
    # 运行agent
    history = await agent.run(max_steps=15)
    print(history)
    
    # 获取最终结果
    result = history.final_result()
    if result:
        return result
    else:
        return "任务执行成功，但未找到结果"


if __name__ == "__main__":
    mcp.run(transport="sse")
