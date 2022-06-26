from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
from urllib.parse import unquote
from .process import run


def index(request):
    return render(request, 'main/main.html')



class VideoCamera(object):
    def __init__(self, link, resolution): # http://131.95.3.162:80/mjpg/video.mjpg
        self.link = link
        self.resolution = resolution
        threading.Thread(target=self.update, args=()).start()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        def callback(frame):
            self.frame = frame
        run(self.link, 'gpu', callback, resolution=self.resolution)


def gen(camera):
    while True:
        try:
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        except:
            pass


@gzip.gzip_page
def livefe(request):
    try:
        # http://127.0.0.1:8000/cam?link=http://131.95.3.162:80/mjpg/video.mjpg&czxczx=ZXZ&xzczxc=zxczxc
        cam = VideoCamera(request.GET.get('link', 'http://176.112.162.177:8081/mjpg/video.mjpg'), int(request.GET.get('resolution', 360)))
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass