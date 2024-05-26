import requests
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
from pydantic import BaseModel, Field
from typing import Type
from superagi.tools.base_tool import BaseTool
import re
import logging

class RetrieveTranscriptInput(BaseModel):
    video_link: str = Field(..., description="YouTube video URL")

class RetrieveTranscriptTool(BaseTool):
    name: str = "Retrieve Transcript"
    agent_id: int = None
    args_schema: Type[BaseModel] = RetrieveTranscriptInput
    description: str = "Retrieves transcript for a given YouTube video URL"

    def _execute(self, video_link: str):
        try:
            # Extract the video ID from the YouTube URL
            video_id = self.extract_video_id(video_link)
            logging.info(f"Extracted video ID: {video_id}")
            # Fetch the transcript using the video ID
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
            # Concatenate all text entries into one block of text
            full_transcript = ' '.join([entry['text'] for entry in transcript_list])
            return {'transcript': full_transcript}
        except VideoUnavailable:
            logging.error("The video is unavailable.")
            return {'error': 'The video is unavailable.'}
        except TranscriptsDisabled:
            logging.error("Subtitles are disabled for this video.")
            return {'error': 'Subtitles are disabled for this video.'}
        except NoTranscriptFound:
            logging.error("No transcript found for this video.")
            return {'error': 'No transcript found for this video.'}
        except ValueError as ve:
            logging.error(f"Invalid YouTube URL: {str(ve)}")
            return {'error': f"Invalid YouTube URL: {str(ve)}"}
        except Exception as e:
            logging.error(f"An unexpected error occurred: {str(e)}")
            return {'error': f'An unexpected error occurred: {str(e)}'}

    def extract_video_id(self, video_link: str) -> str:
        match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', video_link)
        if not match:
            raise ValueError('Invalid YouTube URL')
        return match.group(1)
