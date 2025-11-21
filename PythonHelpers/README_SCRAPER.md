# YouTube Channel Transcript Scraper

## Overview
This tool scrapes all videos from a YouTube channel and extracts:
1. Video Title
2. Video Description
3. Full Transcript (if available)

All data is saved to `VidsTranscript.csv`

**NO API KEY REQUIRED!** This tool uses `yt-dlp` and `youtube-transcript-api` which work without any authentication.

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

That's it! No API keys or authentication needed.

## Usage

### Default Channel (RichAndLegit)
Simply run:
```bash
python PythonHelpers/youtube_transcript_scraper.py
```

### Different Channel
Edit the script and change:
```python
CHANNEL_URL = 'https://www.youtube.com/@RichAndLegit'
```
to your desired channel URL.

## Output
The script creates `VidsTranscript.csv` with three columns:
- **Video Title**: The title of the video
- **Video Description**: The full description
- **Transcript**: The full transcript text (or error message if unavailable)

## Important Notes

### API Quota Limits
- YouTube Data API has a default quota of **10,000 units/day**
- Each video listing costs ~1 unit
- Large channels may require multiple days or quota increase

### Transcripts
- Not all videos have transcripts available
- Videos without transcripts will show: "No transcript available"
- The script handles this gracefully and continues processing

### Rate Limiting
- The script includes small delays to avoid rate limiting
- For large channels (1000+ videos), expect longer run times

## Troubleshooting

### "API Key not set" Error
Make sure you've set your API key using one of the methods above.

### "Quota exceeded" Error
You've hit the daily API limit. Wait 24 hours or request a quota increase from Google Cloud Console.

### "Channel not found" Error
- Verify the channel URL is correct
- Try using the channel's full URL
- Some private channels cannot be accessed

## Example Run
```
Starting scrape of channel: https://www.youtube.com/@RichAndLegit
Output file: VidsTranscript.csv
------------------------------------------------------------
Resolving channel ID...
Channel ID: UC8aG3LDTDwNR1UQhSn9uVrw

Fetching all video IDs from channel...
Retrieved 50 video IDs so far...
Retrieved 100 video IDs so far...
Total videos found: 127

Processing 127 videos...
------------------------------------------------------------

[1/127] Processing video: dQw4w9WgXcQ
  Title: Example Video Title...
  Fetching transcript...
  ✓ Transcript retrieved (15234 characters)

...

============================================================
✓ Scraping complete! Data saved to: VidsTranscript.csv
============================================================
```

## File Structure
```
PythonHelpers/
├── youtube_transcript_scraper.py     # Main script
├── youtube_transcript_scraper.txt    # Documentation
└── README_SCRAPER.md                 # This file

VidsTranscript.csv                     # Output file (created after running)
requirements.txt                       # Python dependencies
```
