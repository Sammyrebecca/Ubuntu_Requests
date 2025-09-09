#!/usr/bin/env python3
"""
Image Downloader Script
Downloads images from URLs and saves them to Fetched_Images directory
"""

import os
import requests
from urllib.parse import urlparse, unquote
from pathlib import Path
import mimetypes

def create_directory(directory_name):
    """Create directory if it doesn't exist"""
    try:
        os.makedirs(directory_name, exist_ok=True)
        print(f"✓ Directory '{directory_name}' is ready")
        return True
    except PermissionError:
        print("✗ Permission denied: Cannot create directory")
        return False
    except OSError as e:
        print(f"✗ Error creating directory: {e}")
        return False

def extract_filename(url, content_type=None):
    """
    Extract filename from URL or generate one based on content type
    Returns appropriate filename with extension
    """
    # Parse the URL to get the path
    parsed_url = urlparse(url)
    path = unquote(parsed_url.path)  # Decode URL-encoded characters
    
    # Try to get filename from URL path
    if path and '/' in path:
        filename = path.split('/')[-1]
        if filename and '.' in filename:
            return filename
    
    # If no filename in URL, generate one based on content type
    if content_type:
        extension = mimetypes.guess_extension(content_type)
        if extension:
            return f"downloaded_image{extension}"
    
    # Fallback: use generic filename
    return "downloaded_image.jpg"

def download_image(url, save_directory):
    """Download image from URL and save to specified directory"""
    try:
        print(f"🔗 Connecting to: {url}")
        
        # Send GET request with timeout and headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0'
        }
        response = requests.get(url, headers=headers, timeout=30, stream=True)
        
        # Check for HTTP errors
        response.raise_for_status()
        
        # Get content type to determine file extension
        content_type = response.headers.get('content-type', '')
        
        # Extract or generate filename
        filename = extract_filename(url, content_type)
        filepath = os.path.join(save_directory, filename)
        
        # Handle filename conflicts
        counter = 1
        base_name, extension = os.path.splitext(filename)
        while os.path.exists(filepath):
            filename = f"{base_name}_{counter}{extension}"
            filepath = os.path.join(save_directory, filename)
            counter += 1
        
        # Save the image
        print(f"💾 Saving as: {filename}")
        with open(filepath, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        
        # Get file size
        file_size = os.path.getsize(filepath)
        print(f"✅ Download successful! Saved to: {filepath}")
        print(f"📦 File size: {file_size / 1024:.2f} KB")
        
        return True
        
    except requests.exceptions.HTTPError as e:
        print(f"✗ HTTP Error: {e}")
        print("ℹ️ The server returned an error response. Please check the URL.")
        
    except requests.exceptions.ConnectionError:
        print("✗ Connection Error: Unable to connect to the server")
        print("ℹ️ Please check your internet connection and the URL.")
        
    except requests.exceptions.Timeout:
        print("✗ Timeout Error: The request took too long")
        print("ℹ️ The server is not responding. Please try again later.")
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Request Error: {e}")
        
    except IOError as e:
        print(f"✗ File I/O Error: {e}")
        print("ℹ️ Cannot write to file. Check directory permissions.")
        
    except Exception as e:
        print(f"✗ Unexpected Error: {e}")
        
    return False

def main():
    """Main function to run the image downloader"""
    print("=" * 50)
    print("🌐 Ubuntu Image Downloader")
    print("=" * 50)
    
    # Create directory for images
    directory_name = "Fetched_Images"
    if not create_directory(directory_name):
        return
    
    while True:
        print("\n" + "-" * 30)
        url = input("Please enter the image URL (or 'quit' to exit): ").strip()
        
        if url.lower() in ['quit', 'exit', 'q']:
            print("👋 Thank you for using Ubuntu Image Downloader!")
            break
        
        if not url:
            print("ℹ️ Please enter a valid URL")
            continue
        
        # Add http:// prefix if missing
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            print(f"ℹ️ Added protocol: {url}")
        
        # Download the image
        download_image(url, directory_name)
        
        print("\n" + "-" * 30)
        continue_download = input("Download another image? (y/n): ").strip().lower()
        if continue_download not in ['y', 'yes']:
            print("👋 Thank you for using Ubuntu Image Downloader!")
            break

if __name__ == "__main__":
    main()