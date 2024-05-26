import requests
from pydantic import BaseModel, Field
from typing import Type
from superagi.tools.base_tool import BaseTool

class SearchVideosInput(BaseModel):
    query: str = Field(..., description="Search query for YouTube videos")
    maxResults: int = Field(5, description="Maximum number of search results to return")

class SearchVideosTool(BaseTool):
    name: str = "Search Videos"
    agent_id: int = None
    args_schema: Type[BaseModel] = SearchVideosInput
    description: str = "Searches for YouTube videos by query"

    def _execute(self, query: str, maxResults: int = 5):
        url = "http://194.195.120.112:5000/search"
        params = {'query': query, 'maxResults': maxResults}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': response.text}
