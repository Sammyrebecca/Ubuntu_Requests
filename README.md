# Ubuntu Image Downloader

A Python script that downloads images from URLs and organizes them in a dedicated directory.

## Features

- 🌐 Downloads images from any accessible URL
- 📁 Creates "Fetched_Images" directory automatically
- 🎯 Extracts filenames from URLs or generates appropriate ones
- ⚡ Handles various error scenarios gracefully
- 🔄 Supports multiple downloads in one session
- 🛡️ Includes proper timeout and connection handling

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/Ubuntu_Requests.git
cd Ubuntu_Requests
Usage
Run the script:

bash
python image_downloader.py
Follow the prompts to enter image URLs. The script will:

Create the "Fetched_Images" directory if it doesn't exist

Download images with proper filenames

Handle errors gracefully

Allow multiple downloads in one session

## Error Handling
The script handles:

HTTP errors (404, 403, etc.)

Connection errors

Timeout errors

File I/O errors

Permission issues

Invalid URLs

## Ubuntu Principles Implemented
Community: Connects to the wider web community to fetch images

Respect: Graceful error handling without crashing

Sharing: Organizes images in a dedicated directory for easy sharing

Practicality: Solves a real-world need for image downloading
## Key Features Implemented
Directory Creation: Uses os.makedirs() with exist_ok=True

Error Handling: Comprehensive error handling for all common scenarios

Filename Extraction: Smart filename extraction from URLs with fallbacks

Binary Mode Saving: Saves images properly in binary mode

User-Friendly: Clean interface with progress feedback

Ubuntu Principles: Respects community, handles errors gracefully, organizes content practically

