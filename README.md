# YTC - YouTube Content Tools

A collection of browser-based tools for YouTube content creators and music producers. All tools run entirely in your browser - no server, no signup, no data uploaded.

## 🚀 Live Tools

Access all tools directly via GitHub Pages:

1. **Music Thumbnail Generator**
   https://some-dude-999.github.io/YTC/MUSIC%20THUMBNAIL%20GEN.html

2. **WAV Duplicate Checker**
   https://some-dude-999.github.io/YTC/MUSIC%20WAVE%20DUPLICATE%20CHECKER.html

3. **Video Screenshot Extractor**
   https://some-dude-999.github.io/YTC/thumbnail-extractor.html

4. **Bulk Downloader Link Opener**
   https://some-dude-999.github.io/YTC/Bulk%20Downloader%20Link%20Opener.html

See [LINK.txt](LINK.txt) for the complete list.

---

## 📚 Tools Overview

### 🎨 Music Thumbnail Generator
**Create professional YouTube thumbnails with custom text overlays**

- 560+ Google Fonts organized by music genre
- Master template system for batch customization
- Drag-and-drop text positioning with 1px precision
- Font categories: EDM, Hip-Hop, Lo-fi, Rock, Classical, Synthwave, Halloween, Christmas, and more
- Export at 1280x720 (YouTube standard)
- Text effects: Drop shadow, glow, or none
- Favorites system for quick access

**Perfect for:** Music channels, playlists, mix uploads

📖 [Full Documentation](MUSIC%20THUMBNAIL%20GEN.txt)

---

### 🎵 WAV Duplicate Checker
**Find duplicate audio files in your sample libraries**

- Detects duplicates by file size, duration, and filename similarity
- Built-in audio player with progress bars
- Identifies unplayable files (codec warnings)
- Favorites system for marking keepers
- "Played songs" tracking for large libraries
- Consolidate deleted files automatically
- Dark mode cyberpunk design

**Perfect for:** Music producers managing sample packs, clearing duplicate downloads

📖 [Full Documentation](MUSIC%20WAVE%20DUPLICATE%20CHECKER.txt)

---

### 📸 Video Screenshot Extractor
**Extract frames from videos at regular intervals**

- Process multiple videos simultaneously
- Extract 10-5000 frames per video
- Download individual frames as high-quality JPG
- Responsive grid layout
- Remove unwanted frames
- Native video resolution preserved

**Perfect for:** Creating video thumbnails, storyboards, reference sheets

📖 [Full Documentation](thumbnail-extractor.txt)

---

### 🚀 Bulk Downloader Link Opener
**Open multiple download tabs for batch processing**

- Opens 1-50 tabs with controlled delay
- Prevents browser blocking (1-second intervals)
- Optimized for yt1s.biz downloader
- Pop-up blocker detection

**Perfect for:** Downloading multiple videos efficiently

📖 [Full Documentation](Bulk%20Downloader%20Link%20Opener.txt)

---

## 🛠️ Features

### All Tools Share:
- ✅ **100% Client-Side** - No server, no data uploaded
- ✅ **No Installation** - Run directly in browser
- ✅ **No Signup** - No accounts, no tracking
- ✅ **Free Forever** - Open source, hosted on GitHub Pages
- ✅ **Mobile Friendly** - Responsive design (where applicable)
- ✅ **Offline Capable** - Most tools work offline after first load (except font loading)

---

## 📖 Documentation

Each HTML file has a corresponding `.txt` documentation file:

- [Bulk Downloader Link Opener.txt](Bulk%20Downloader%20Link%20Opener.txt)
- [MUSIC THUMBNAIL GEN.txt](MUSIC%20THUMBNAIL%20GEN.txt)
- [MUSIC WAVE DUPLICATE CHECKER.txt](MUSIC%20WAVE%20DUPLICATE%20CHECKER.txt)
- [thumbnail-extractor.txt](thumbnail-extractor.txt)

Documentation includes:
- Data sources and dependencies
- Functionality breakdown
- Workflow explanations
- Browser compatibility notes
- Technical corrections and clarifications

---

## 🔧 Development

### Link Manager
Automatically update `LINK.txt` with GitHub Pages URLs:

```bash
python PythonHelpers/link_manager.py
```

This script:
- Detects repository owner/name from git remote
- Finds all HTML files
- Generates GitHub Pages URLs with proper encoding
- Preserves existing descriptions in LINK.txt

### Project Structure
```
YTC/
├── *.html                           # Main tool files
├── *.txt                            # Documentation files
├── LINK.txt                         # GitHub Pages URL index
├── CLAUDE.md                        # Development rules
├── README.md                        # This file
└── PythonHelpers/
    └── link_manager.py              # URL automation script
```

### Development Rules
See [CLAUDE.md](CLAUDE.md) for:
- Documentation-first workflow
- Git branching strategy
- Link management automation
- Commit/PR guidelines

---

## 🌐 Browser Compatibility

| Tool | Chrome | Firefox | Edge | Safari |
|------|--------|---------|------|--------|
| Music Thumbnail Generator | ✅ | ✅ | ✅ | ✅ |
| WAV Duplicate Checker | ✅ | ✅ | ✅ | ⚠️* |
| Video Screenshot Extractor | ✅ | ✅ | ✅ | ✅ |
| Bulk Downloader Link Opener | ✅ | ✅ | ✅ | ✅ |

*WAV Duplicate Checker: Safari has limited codec support for WAV files

---

## 🎯 Use Cases

### For Music Producers:
- Create eye-catching thumbnails for music uploads
- Clean up duplicate samples in your library
- Extract album artwork from music videos

### For Content Creators:
- Generate custom thumbnails quickly
- Extract video frames for social media
- Batch process downloads efficiently

### For Educators:
- Create video storyboards
- Extract presentation slides from recordings
- Organize lecture materials

---

## 🤝 Contributing

Contributions welcome! Please:

1. Follow documentation guidelines in [CLAUDE.md](CLAUDE.md)
2. Create `.txt` documentation for any new HTML tools
3. Run `python PythonHelpers/link_manager.py` after adding HTML files
4. Update this README if adding new tools

---

## 📜 License

MIT License - Free to use, modify, and distribute.

---

## 🔗 Links

- **Live Tools**: See [LINK.txt](LINK.txt)
- **GitHub Repository**: https://github.com/some-dude-999/YTC
- **Issues/Feedback**: https://github.com/some-dude-999/YTC/issues

---

## 📝 Changelog

### 2025-11-19
- Added comprehensive documentation for all tools
- Created automated link management system
- Structured project with proper README

### Previous
- Initial tool development
- GitHub Pages deployment

---

**Made with 💜 for creators by creators**
