from django.shortcuts import render
from django.http import HttpResponse
from pytube import YouTube
from tqdm import tqdm
import time
# Create your views here.

def index(request):
    return render(request, "youtube/index.html")
    # url = request.GET.get('text','default')
    # path = request.GET.get('path','default')

    # print('Downloaded')
    # print(yt.streams)

def download(request):
    url = request.GET.get('text','default')
    path = request.GET.get('path','default')
    yt = YouTube(url)
    yt.streams.get_highest_resolution().download(path)
    # for x in tqdm(range(1000)):
    #     time.sleep(0.01)
    # print(url)
    # print(path)
    return HttpResponse("Downloaded")