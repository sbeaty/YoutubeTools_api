import requests
from pydantic import BaseModel, Field
from typing import Type
from superagi.tools.base_tool import BaseTool

class VideoDetailsInput(BaseModel):
    videoId: str = Field(..., description="YouTube video ID")

class VideoDetailsTool(BaseTool):
    name: str = "Video Details"
    agent_id: int = None
    args_schema: Type[BaseModel] = VideoDetailsInput
    description: str = "Retrieves details for a given YouTube video ID"

    def _execute(self, videoId: str):
        url = "http://194.195.120.112:5000/video_details"
        params = {'videoId': videoId}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': response.text}
