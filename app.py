import requests
from mcp.server.fastmcp import FastMCP
from typing import Dict, List, Optional
import json
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize MCP server
mcp = FastMCP("canvas_api")

# Canvas API configuration from environment variables
CANVAS_DOMAIN = os.getenv("CANVAS_DOMAIN", "https://canvas.uoregon.edu")
API_TOKEN = os.getenv("CANVAS_API_TOKEN")
DEFAULT_PER_PAGE = int(os.getenv("DEFAULT_PER_PAGE", "50"))

# Validate required environment variables
if not API_TOKEN:
    raise ValueError("CANVAS_API_TOKEN must be set in .env file")

if not CANVAS_DOMAIN:
    raise ValueError("CANVAS_DOMAIN must be set in .env file")

# Helper function to make Canvas API requests
def canvas_request(endpoint: str, method: str = "GET", params: dict = None) -> dict:
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    url = f"{CANVAS_DOMAIN}/api/v1{endpoint}"
    try:
        response = requests.request(method, url, headers=headers, params=params)
        
        # Handle different error cases
        if response.status_code == 403:
            return {"error": "Permission denied. Please check your API token permissions."}
        elif response.status_code == 404:
            return {"error": f"Resource not found: {endpoint}"}
        elif response.status_code == 401:
            return {"error": "Invalid API token. Please check your .env file."}
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Your Canvas API functions here...