import requests
from pydantic import BaseModel, Field
from typing import Type
from superagi.tools.base_tool import BaseTool

class RetrieveTranscriptInput(BaseModel):
    video_link: str = Field(..., description="YouTube video URL")

class RetrieveTranscriptTool(BaseTool):
    name: str = "Retrieve Transcript"
    agent_id: int = None
    args_schema: Type[BaseModel] = RetrieveTranscriptInput
    description: str = "Retrieves transcript for a given YouTube video URL"

    def _execute(self, video_link: str):
        url = "http://194.195.120.112:5000/transcript"
        params = {'video_link': video_link}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': response.text}
