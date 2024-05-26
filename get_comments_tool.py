import requests
from pydantic import BaseModel, Field
from typing import Type
from superagi.tools.base_tool import BaseTool

class GetCommentsInput(BaseModel):
    videoId: str = Field(..., description="YouTube video ID")
    maxResults: int = Field(5, description="Maximum number of comments to return")

class GetCommentsTool(BaseTool):
    name: str = "Get Comments"
    agent_id: int = None
    args_schema: Type[BaseModel] = GetCommentsInput
    description: str = "Retrieves comments for a given YouTube video ID"

    def _execute(self, videoId: str, maxResults: int = 5):
        url = "http://194.195.120.112:5000/comments"
        params = {'videoId': videoId, 'maxResults': maxResults}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': response.text}
