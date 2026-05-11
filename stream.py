import os, subprocess

# Video Direct Download Link (Converted from your Drive link)
VIDEO_URL = "https://docs.google.com/uc?export=download&id=1zNwUOV5BE0JhcNoeiTqoKJ7zAcwdT_LE"

# Stream Key (Secrets se aayegi)
SK = os.getenv("STREAM_KEY")

def start():
    # ffmpeg command for YouTube Live
    cmd = (
        f'ffmpeg -re -stream_loop -1 -i "{VIDEO_URL}" '
        f'-c:v libx264 -preset veryfast -b:v 3000k -maxrate 3000k -bufsize 6000k '
        f'-pix_fmt yuv420p -g 50 -c:a aac -b:a 128k -ar 44100 '
        f'-f flv rtmp://a.rtmp.youtube.com/live2/{SK}'
    )
    
    while True:
        print("Starting Stream...")
        subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    start()


 
