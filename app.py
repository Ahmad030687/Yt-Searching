from flask import Flask, request, jsonify
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "Zinda", "msg": "Sardar RDX System On Hai! 😏"})

@app.route('/search')
def search_youtube():
    query = request.args.get('q')
    if not query: return jsonify({"success": False}), 400
    
    ydl_opts = {'format': 'best', 'quiet': True, 'extract_flat': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch1:{query}", download=False)
        video = info['entries'][0]
        return jsonify({"success": True, "result": {"title": video['title'], "url": video['url']}})

if __name__ == "__main__":
    # Render PORT environment variable se port uthayega
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    
