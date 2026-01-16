import os
from fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("Test MCP Server")


@mcp.tool
def fetch_document(title: str) -> dict:
    """Fetch a document by its title.
    
    Args:
        title: The title of the document to fetch
        
    Returns:
        A dictionary containing the document information
    """
    # This is a test implementation - returns mock data
    return {
        "title": title,
        "content": f"This is the content of the document titled '{title}'.",
        "status": "success",
        "message": "Document fetched successfully (mock data)"
    }


# Create ASGI application for deployment
app = mcp.http_app(path="/mcp")


if __name__ == "__main__":
    # For local development
    port = int(os.environ.get("PORT", 8000))
    mcp.run(transport="http", host="0.0.0.0", port=port)
