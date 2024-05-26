from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from retrieve_transcript_tool import RetrieveTranscriptTool
from search_videos_tool import SearchVideosTool
from video_details_tool import VideoDetailsTool
from get_comments_tool import GetCommentsTool

class YoutubeToolsToolkit(BaseToolkit, ABC):
    name: str = "YouTube Tools Toolkit"
    description: str = "Toolkit containing tools for interacting with YouTube API"

    def get_tools(self) -> List[BaseTool]:
        return [RetrieveTranscriptTool(), SearchVideosTool(), VideoDetailsTool(), GetCommentsTool()]

    def get_env_keys(self) -> List[str]:
        return ["YOUTUBE_API_KEY"]
