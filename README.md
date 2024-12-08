# YouTube Video Downloader

## Overview

YouTube Video Downloader is a simple web application built with Flask that allows users to download YouTube videos and audio files quickly and easily.

## Features

- Download full videos with audio
- Extract audio-only files
- Simple, user-friendly web interface
- Uses yt-dlp for robust YouTube video downloading

## Prerequisites

- Python 3.7+
- Flask
- yt-dlp

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/sunilmakkar/YT-video-downloader.git
   cd youtube-video-downloader
   ```

2. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install required dependencies:
   ```
   pip install flask yt-dlp
   ```

## Configuration

- Modify the `outtmpl` in `app.py` to change the download location:
  ```python
  'outtmpl': '/path/to/your/download/directory/%(title)s.%(ext)s'
  ```

## Running the Application

1. Ensure you're in the project directory
2. Run the Flask application:
   ```
   python app.py
   ```
3. Open a web browser and navigate to `http://localhost:5000`

## Usage

1. Enter a YouTube URL in the input field
2. Choose download option:
   - Video/Audio: Downloads full video with audio
   - Audio Only: Extracts audio track
3. Click "Download"

## Technologies Used

- Python
- Flask
- yt-dlp
- HTML5
- CSS3

## Limitations

- Respects YouTube's terms of service
- Download speed depends on your internet connection
- Large videos may take longer to download

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Sunil Makkar
