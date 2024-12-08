from flask import Flask, render_template, request, redirect, url_for
import yt_dlp
import os

app = Flask(__name__)

# Define download function
def download_video(link, download_option):
    if download_option == 'video':
        format_option = 'bestvideo+bestaudio/best'
    elif download_option == 'audio':
        format_option = 'bestaudio/best'
    else:
        return "Invalid option."

    ydl_opts = {
        'format': format_option,
        'outtmpl': '/Users/sunilmakkar/YouTube-Videos/%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=False)
        title = info_dict.get('title', 'Unknown Title')
        ydl.download([link])
    
    return f"Download of {title} is complete!"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        link = request.form["url"]
        download_option = request.form["download_option"]
        
        # Call the download function
        message = download_video(link, download_option)
        return render_template("index.html", message=message)
    
    return render_template("index.html", message=None)

if __name__ == "__main__":
    app.run(debug=True)
