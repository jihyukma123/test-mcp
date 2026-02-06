import os
from fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("Test MCP Server")


@mcp.tool(
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": False,
    }
)
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

@mcp.tool(
    annotations={
        "readOnlyHint": False,
        "destructiveHint": False,
        "openWorldHint": False,
    }
)
def send_email(title: str, recipient_email: str, cc_recipient: str, content: str) -> str:
    """Mock-send an email.

    This tool does not send a real email yet; it only returns a confirmation message.

    Args:
        title: Email subject/title
        recipient_email: Primary recipient email address
        cc_recipient: CC recipient email address (optional; pass empty string if none)
        content: Email body

    Returns:
        A confirmation message in Korean.
    """
    return f"{recipient_email}에게 아래 내용으로 이메일이 전송되었습니다. {content}"


# Create ASGI application for deployment
app = mcp.http_app(path="/mcp")


if __name__ == "__main__":
    # For local development
    port = int(os.environ.get("PORT", 8000))
    mcp.run(transport="http", host="0.0.0.0", port=port)
