from fastapi import FastAPI, Query
import yt_dlp
import uvicorn

app = FastAPI()

@app.get("/search")
def search_youtube(q: str = Query(None)):
    if not q:
        return {"success": False, "message": "Oye! Kuch likh toh sahi saste hero! 😏"}

    # 🔥 Sardar RDX Heavy Settings
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        'extract_flat': True,
        'skip_download': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # ytsearch1 matlab pehla result search karo
            search_query = f"ytsearch1:{q}"
            info = ydl.extract_info(search_query, download=False)
            
            if 'entries' in info and len(info['entries']) > 0:
                video = info['entries'][0]
                return {
                    "success": True,
                    "result": {
                        "title": video.get('title'),
                        "id": video.get('id'),
                        "url": f"https://www.youtube.com/watch?v={video.get('id')}",
                        "duration": video.get('duration'),
                        "uploader": video.get('uploader'),
                        "views": video.get('view_count')
                    }
                }
            else:
                return {"success": False, "message": "Kuch nahi mila! 🖕"}
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
  
