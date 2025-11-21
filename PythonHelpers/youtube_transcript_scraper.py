#!/usr/bin/env python3
"""
YouTube Channel Transcript Scraper
Extracts all video titles, descriptions, and transcripts from a YouTube channel
Outputs to VidsTranscript.csv
"""

import os
import csv
import time
import re
from typing import List, Dict, Optional
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

# Configuration
YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY', 'YOUR_API_KEY_HERE')
CHANNEL_URL = 'https://www.youtube.com/@RichAndLegit'
OUTPUT_FILE = 'VidsTranscript.csv'

class YouTubeChannelScraper:
    def __init__(self, api_key: str):
        """Initialize the YouTube API client"""
        self.youtube = build('youtube', 'v3', developerKey=api_key)
        self.api_key = api_key

    def extract_channel_id(self, channel_url: str) -> Optional[str]:
        """
        Extract channel ID from various YouTube URL formats
        Handles @username handles by resolving them via API
        """
        # Extract username/handle from URL
        if '@' in channel_url:
            # Handle format: https://www.youtube.com/@RichAndLegit
            match = re.search(r'@([\w-]+)', channel_url)
            if match:
                username = match.group(1)
                return self.get_channel_id_from_handle(username)

        # Handle format: https://www.youtube.com/channel/UC...
        match = re.search(r'channel/(UC[\w-]+)', channel_url)
        if match:
            return match.group(1)

        # Handle format: https://www.youtube.com/c/channelname
        match = re.search(r'/c/([\w-]+)', channel_url)
        if match:
            channel_name = match.group(1)
            return self.get_channel_id_from_username(channel_name)

        return None

    def get_channel_id_from_handle(self, handle: str) -> Optional[str]:
        """Resolve @handle to channel ID using YouTube API"""
        try:
            request = self.youtube.search().list(
                part='snippet',
                q=f'@{handle}',
                type='channel',
                maxResults=1
            )
            response = request.execute()

            if response['items']:
                return response['items'][0]['snippet']['channelId']
        except HttpError as e:
            print(f"Error resolving handle: {e}")
        return None

    def get_channel_id_from_username(self, username: str) -> Optional[str]:
        """Resolve custom username to channel ID"""
        try:
            request = self.youtube.channels().list(
                part='id',
                forUsername=username
            )
            response = request.execute()

            if response['items']:
                return response['items'][0]['id']
        except HttpError as e:
            print(f"Error resolving username: {e}")
        return None

    def get_all_channel_videos(self, channel_id: str) -> List[str]:
        """
        Get all video IDs from a channel
        Handles pagination to retrieve all videos
        """
        video_ids = []

        try:
            # First, get the uploads playlist ID
            request = self.youtube.channels().list(
                part='contentDetails',
                id=channel_id
            )
            response = request.execute()

            if not response['items']:
                print(f"Channel not found: {channel_id}")
                return []

            uploads_playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

            # Now fetch all videos from the uploads playlist
            next_page_token = None

            while True:
                playlist_request = self.youtube.playlistItems().list(
                    part='contentDetails',
                    playlistId=uploads_playlist_id,
                    maxResults=50,
                    pageToken=next_page_token
                )
                playlist_response = playlist_request.execute()

                for item in playlist_response['items']:
                    video_ids.append(item['contentDetails']['videoId'])

                next_page_token = playlist_response.get('nextPageToken')

                print(f"Retrieved {len(video_ids)} video IDs so far...")

                if not next_page_token:
                    break

                # Small delay to avoid rate limiting
                time.sleep(0.1)

            print(f"Total videos found: {len(video_ids)}")
            return video_ids

        except HttpError as e:
            print(f"Error fetching videos: {e}")
            return []

    def get_video_details(self, video_id: str) -> Dict[str, str]:
        """Get video title and description"""
        try:
            request = self.youtube.videos().list(
                part='snippet',
                id=video_id
            )
            response = request.execute()

            if response['items']:
                snippet = response['items'][0]['snippet']
                return {
                    'title': snippet.get('title', 'No title'),
                    'description': snippet.get('description', 'No description')
                }
        except HttpError as e:
            print(f"Error fetching video details for {video_id}: {e}")

        return {
            'title': 'Error fetching title',
            'description': 'Error fetching description'
        }

    def get_video_transcript(self, video_id: str) -> str:
        """
        Get video transcript using youtube-transcript-api
        Tries multiple languages and handles errors gracefully
        """
        try:
            # Try to get transcript (auto-generated or manual)
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)

            # Combine all transcript segments into one string
            full_transcript = ' '.join([segment['text'] for segment in transcript_list])
            return full_transcript

        except TranscriptsDisabled:
            return "No transcript available (disabled by uploader)"
        except NoTranscriptFound:
            return "No transcript available (not found)"
        except Exception as e:
            return f"Error fetching transcript: {str(e)}"

    def scrape_channel(self, channel_url: str, output_file: str):
        """
        Main function to scrape entire channel and save to CSV
        """
        print(f"Starting scrape of channel: {channel_url}")
        print(f"Output file: {output_file}")
        print("-" * 60)

        # Extract channel ID
        print("Resolving channel ID...")
        channel_id = self.extract_channel_id(channel_url)

        if not channel_id:
            print("ERROR: Could not resolve channel ID from URL")
            return

        print(f"Channel ID: {channel_id}")

        # Get all video IDs
        print("\nFetching all video IDs from channel...")
        video_ids = self.get_all_channel_videos(channel_id)

        if not video_ids:
            print("ERROR: No videos found or unable to fetch videos")
            return

        # Prepare CSV file
        print(f"\nProcessing {len(video_ids)} videos...")
        print("-" * 60)

        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Video Title', 'Video Description', 'Transcript'])

            for idx, video_id in enumerate(video_ids, 1):
                print(f"\n[{idx}/{len(video_ids)}] Processing video: {video_id}")

                # Get video details
                details = self.get_video_details(video_id)
                title = details['title']
                description = details['description']

                print(f"  Title: {title[:60]}...")

                # Get transcript
                print(f"  Fetching transcript...")
                transcript = self.get_video_transcript(video_id)

                if "No transcript available" in transcript or "Error" in transcript:
                    print(f"  ⚠️  {transcript}")
                else:
                    print(f"  ✓ Transcript retrieved ({len(transcript)} characters)")

                # Write to CSV
                writer.writerow([title, description, transcript])

                # Small delay to be nice to APIs
                time.sleep(0.2)

        print("\n" + "=" * 60)
        print(f"✓ Scraping complete! Data saved to: {output_file}")
        print("=" * 60)


def main():
    """Main execution function"""

    # Check if API key is set
    if YOUTUBE_API_KEY == 'YOUR_API_KEY_HERE':
        print("=" * 60)
        print("⚠️  WARNING: YouTube API Key not set!")
        print("=" * 60)
        print("\nPlease set your YouTube Data API v3 key:")
        print("1. Set environment variable: export YOUTUBE_API_KEY='your_key'")
        print("2. Or edit this script and replace 'YOUR_API_KEY_HERE'")
        print("\nTo get an API key:")
        print("1. Go to https://console.cloud.google.com/")
        print("2. Create/select a project")
        print("3. Enable YouTube Data API v3")
        print("4. Create credentials (API Key)")
        print("=" * 60)

        # Ask if user wants to input key now
        user_key = input("\nEnter your API key now (or press Enter to exit): ").strip()
        if not user_key:
            return
        global YOUTUBE_API_KEY
        YOUTUBE_API_KEY = user_key

    # Initialize scraper
    scraper = YouTubeChannelScraper(YOUTUBE_API_KEY)

    # Run the scraper
    scraper.scrape_channel(CHANNEL_URL, OUTPUT_FILE)


if __name__ == "__main__":
    main()
