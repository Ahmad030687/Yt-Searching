from flask import Flask, request, jsonify
import yt_dlp
import os

app = Flask(__name__)

# --- HOME ROUTE (Testing ke liye) ---
@app.route('/')
def home():
    return "<h1>Sardar RDX Search API: ONLINE 😏🔥</h1>"

# --- SEARCH ROUTE ---
@app.route('/search', methods=['GET'])
def search_youtube():
    query = request.args.get('q')
    
    if not query:
        return jsonify({
            "success": False, 
            "message": "Oye saste hero! 'q' parameter mein kuch likh toh sahi! 😏🖕"
        }), 400

    # 🔥 Optimized yt-dlp settings
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        'extract_flat': True,
        'skip_download': True,
        'source_address': '0.0.0.0', # IPv4 preference
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # ytsearch1: Sirf pehla result uthayega (Sabse fast)
            search_query = f"ytsearch1:{query}"
            info = ydl.extract_info(search_query, download=False)
            
            if 'entries' in info and len(info['entries']) > 0:
                video = info['entries'][0]
                return jsonify({
                    "success": True,
                    "result": {
                        "title": video.get('title'),
                        "id": video.get('id'),
                        "url": f"https://www.youtube.com/watch?v={video.get('id')}",
                        "duration": video.get('duration'),
                        "uploader": video.get('uploader'),
                        "views": video.get('view_count')
                    }
                })
            else:
                return jsonify({
                    "success": False, 
                    "message": "Kuch nahi mila! 🖕"
                }), 404

    except Exception as e:
        return jsonify({
            "success": False, 
            "error": "System hila hua hai!",
            "details": str(e)
        }), 500

# Render port binding
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    
