#!/usr/bin/env python3
"""
YouTube Channel Transcript Scraper
Extracts all video titles, descriptions, and transcripts from a YouTube channel
Outputs to VidsTranscript.csv
"""

import csv
import time
from typing import List, Dict
import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

# Configuration
CHANNEL_URL = 'https://www.youtube.com/@RichAndLegit'
OUTPUT_FILE = 'VidsTranscript.csv'

class YouTubeChannelScraper:
    def __init__(self):
        """Initialize the scraper"""
        self.ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': True,  # Don't download, just get metadata
            'ignoreerrors': True,
            'nocheckcertificate': True,  # Disable SSL verification for proxy environments
        }

    def get_all_channel_videos(self, channel_url: str) -> List[Dict]:
        """
        Get all video data from a channel using yt-dlp
        This is the most reliable method and doesn't require API keys!
        """
        print(f"Fetching videos from {channel_url}...")
        print("This may take a minute...")

        videos = []
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                # Extract channel/playlist info
                result = ydl.extract_info(channel_url, download=False)

                if 'entries' in result:
                    for entry in result['entries']:
                        if entry:  # Some entries might be None if they're unavailable
                            video_data = {
                                'video_id': entry.get('id', ''),
                                'title': entry.get('title', 'No title'),
                                'description': entry.get('description', 'No description')
                            }
                            videos.append(video_data)

                            if len(videos) % 10 == 0:
                                print(f"  Retrieved {len(videos)} videos so far...")

            print(f"Total videos found: {len(videos)}")
            return videos

        except Exception as e:
            print(f"Error fetching videos: {e}")
            import traceback
            traceback.print_exc()
            return []

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

        # Get all video data
        videos = self.get_all_channel_videos(channel_url)

        if not videos:
            print("ERROR: No videos found or unable to fetch videos")
            return

        # Prepare CSV file
        print(f"\nProcessing {len(videos)} videos...")
        print("-" * 60)

        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Video Title', 'Video Description', 'Transcript'])

            for idx, video in enumerate(videos, 1):
                video_id = video['video_id']
                title = video['title']
                description = video['description']

                print(f"\n[{idx}/{len(videos)}] Processing video: {video_id}")
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

                # Small delay to be nice to YouTube
                time.sleep(0.3)

        print("\n" + "=" * 60)
        print(f"✓ Scraping complete! Data saved to: {output_file}")
        print("=" * 60)


def main():
    """Main execution function"""

    # Initialize scraper
    scraper = YouTubeChannelScraper()

    # Run the scraper
    scraper.scrape_channel(CHANNEL_URL, OUTPUT_FILE)


if __name__ == "__main__":
    main()
