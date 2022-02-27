from datetime import datetime as dt

from telethon import events
from ethon.pyfunc import fast_upload, fast_download

def dl_name(mime):
    name = None
    if 'mp4' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
        return name
    elif msg.video:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
        return name
    elif 'x-matroska' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mkv" 
        return name            
    elif 'webm' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".webm" 
        return name
    elif 'zip' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".zip" 
        return name            
    elif 'jpg' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".jpg" 
        return name
    elif 'png' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".png"
        return name
    elif 'pdf' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".pdf" 
        return name
    elif 'rar' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".rar"
        return name
    elif 'mp3' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp3" 
        return name
    elif 'ogg' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".ogg" 
        return name          
    elif 'flac' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".flac"  
        return name
    elif 'wav' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".wav" 
        return name
    elif 'webp' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".webp" 
        return name
    
async def downloader(msg, reply=None):
    if reply is None:
        reply = await msg.reply("Preparing to Download.")
    if telethon != True:
        reply = await PyroBot.get_messages(reply.sender_id, reply.id)
        msg = await PyroBot.get_messages(msg.sender_id, msg.id)
        file = await PyroBot.download_media(
            msg,
            progress=PFP,
            progress_args=(
                PyroBot,
                "**DOWNLOADING:**\n",
                reply,
                time.time()
            )
        )
        return file
    else:
        name = msg.file.name
        if name is None:
            name = dl_name(msg.file.mime_type)
        media = msg.media
        if hasattr(msg.media, "document"):
            media = msg.media.document
        await fast_download(name, media, Drone, reply, time.time(), "**DOWNLOADING:**")
        return name
    
