import requests
from typing import Type

from pydantic import BaseModel, Field

from superagi.tools.base_tool import BaseTool


class SearchVideosInput(BaseModel):
    query: str = Field(..., description="Search query for YouTube videos")
    maxResults: int = Field(5, description="Maximum number of search results to return")


class SearchVideosTool(BaseTool):
    """
    Search Videos tool

    Attributes:
        name : The name.
        agent_id: The agent id.
        description : The description.
        args_schema : The args schema.
    """
    name: str = "Search Videos"
    agent_id: int = None
    args_schema: Type[BaseModel] = SearchVideosInput
    description: str = "Searches for YouTube videos by query"

    def _execute(self, query: str, maxResults: int = 5):
        """
        Execute the search videos tool.

        Args:
            query : The search query for YouTube videos.
            maxResults : Maximum number of search results to return.

        Returns:
            search results.
        """
        url = "http://194.195.120.112:5000/search"
        params = {'query': query, 'maxResults': maxResults}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': response.text}
