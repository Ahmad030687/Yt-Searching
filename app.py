from flask import Flask, request, jsonify
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "Zinda Hoon", "message": "Uvicorn ko kachre mein phenk diya! 😏🔥"})

@app.route('/search', methods=['GET'])
def search_youtube():
    query = request.args.get('q')
    if not query:
        return jsonify({"success": False, "message": "Oye! Kuch likh toh sahi! 😏"}), 400

    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        'extract_flat': True,
        'skip_download': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch1:{query}", download=False)
            if 'entries' in info and len(info['entries']) > 0:
                video = info['entries'][0]
                return jsonify({
                    "success": True,
                    "result": {
                        "title": video.get('title'),
                        "id": video.get('id'),
                        "url": f"https://www.youtube.com/watch?v={video.get('id')}",
                        "duration": video.get('duration'),
                        "uploader": video.get('uploader')
                    }
                })
            return jsonify({"success": False, "message": "Kuch nahi mila! 🖕"}), 404
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
    
