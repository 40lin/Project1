from fastmcp import FastMCP

mcp = FastMCP("server")

@mcp.tool
def hello(name :str) -> str:
    """
    功能:当别人向你打招呼如你好、您好等等，你会回复你好，这是一个打招呼的工具
    参数:
        name: 姓名
    返回:
        问候语
    """
    return f"Hello,nice to me too {name}!"

@mcp.resource("config://version")
def get_version() -> str:
    """
    功能:获取版本号
    返回:返回版本号
    """
    return "v0.0.1"

if __name__ == "__main__":
    mcp.run(transport="stdio")
