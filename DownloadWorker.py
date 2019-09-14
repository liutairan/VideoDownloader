import youtube_dl
import urllib
import shutil

class DownloadWorker:
    def __init__(self):
        pass

    def work(self, linkList, options={}):
        # ydl_opts = {}
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download(linkList)

    def extractInfo(self, linkList, options={}):
        with youtube_dl.YoutubeDL(options) as ydl:
            for link in linkList:
                meta = ydl.extract_info(link, download=False)
                print(meta)
        # ydl = youtube_dl.YoutubeDL()
        # ydl.add_default_info_extractors()
        # for link in linkList:
        #     meta = ydl.extract_info(link, download=False)
        #     print(meta)
