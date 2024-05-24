import requests
from typing import Type

from pydantic import BaseModel, Field

from superagi.tools.base_tool import BaseTool


class VideoDetailsInput(BaseModel):
    videoId: str = Field(..., description="YouTube video ID")


class VideoDetailsTool(BaseTool):
    """
    Video Details tool

    Attributes:
        name : The name.
        agent_id: The agent id.
        description : The description.
        args_schema : The args schema.
    """
    name: str = "Video Details"
    agent_id: int = None
    args_schema: Type[BaseModel] = VideoDetailsInput
    description: str = "Retrieves details for a given YouTube video ID"

    def _execute(self, videoId: str):
        """
        Execute the video details tool.

        Args:
            videoId : The YouTube video ID.

        Returns:
            details of the video.
        """
        url = "http://194.195.120.112:5000/video_details"
        params = {'videoId': videoId}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': response.text}
