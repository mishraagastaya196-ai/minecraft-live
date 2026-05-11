import os, subprocess

# Video Direct Download Link (YouTube Shorts format)
VIDEO_URL = "https://docs.google.com/uc?export=download&id=1zNwUOV5BE0JhcNoeiTqoKJ7zAcwdT_LE"

# Stream Key (Secrets se auto-load hogi)
SK = os.getenv("STREAM_KEY")

def start():
    # Loop (-stream_loop -1) aur Shorts Ratio (-vf "scale=720:1280") set hai
    cmd = (
        f'ffmpeg -re -stream_loop -1 -i "{VIDEO_URL}" '
        f'-vf "scale=720:1280,setdar=9/16" '
        f'-c:v libx264 -preset veryfast -b:v 3000k -maxrate 3000k -bufsize 6000k '
        f'-pix_fmt yuv420p -g 50 -c:a aac -b:a 128k -ar 44100 '
        f'-f flv rtmp://a.rtmp.youtube.com/live2/{SK}'
    )
    
    while True:
        print("Minecraft Shorts Stream Loop Chalu Hai...")
        subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    start()

