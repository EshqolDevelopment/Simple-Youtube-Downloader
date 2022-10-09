import os
from pathlib import Path
from tkinter import filedialog, Tk
from kivy.core.window import Window

Window.size = (800, 550)
Window.minimum_height = 350
Window.minimum_width = 700

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.settings import ContentPanel
from kivymd.app import MDApp
from kiv import Main
import threading
import pytube
from youtube_search import YoutubeSearch


root = Tk()
root.withdraw()


class Youtube(MDApp):
    path = str(Path.home() / "Downloads")
    option = 'high'
    state = StringProperty("start")
    update = StringProperty("")
    pathToOpen = None


    def build(self):
        # self.icon = "icon.png"
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Orange'
        self.title = "Youtube Downloader"
        self.use_kivy_settings = False
        self.settings_cls = ContentPanel
        return Builder.load_string(Main)


    def setPath(self, x: str):
        if x.strip() == '':
            self.root.ids.downloads.hint_text = self.path
        else:
            self.root.ids.downloads.hint_text = x


    def setOptions(self, x: str):
        self.option = x


    def start(self):
        if self.update not in ['Successfully downloaded!', 'Invalid URL', 'unexpected error', '']:
            return False

        self.root.ids.progress.start()
        self.state = 'stop'
        self.update = "Searching for video..."
        thread = threading.Thread(target=self.download, daemon=True)
        thread.start()


    def download(self):
        try:
            txt = self.root.ids.video.text
            if "youtube.com/" not in txt:

                results = YoutubeSearch(txt, max_results=1).to_dict()[0]

                txt = "https://www.youtube.com/" + results["url_suffix"]
                # returns a dictionary

            yt = pytube.YouTube(txt)

        except Exception as e:
            print(e)

            self.update = 'Invalid URL'
            self.root.ids.progress.stop()
            self.state = 'start'
            return False

        try:
            audio = False
            pathToSave = self.root.ids.downloads.hint_text

            if self.option == 'audio':
                audio = True
                stream = yt.streams.get_audio_only()

            elif self.option == 'low':
                stream = yt.streams.get_lowest_resolution()

            else:
                stream = yt.streams.get_highest_resolution()


            if not audio:
                self.update = f'Download started\nresolution: {stream.resolution}, fps: {stream.fps}\nfile size: {round(stream.filesize / 1000000, 2)}Mb'

            else:
                self.update = f'Download started\nquality: {stream.abr}\n file size: {round(stream.filesize / 1000000, 2)}Mb'

            stream.download(pathToSave)
            self.update = 'Successfully downloaded!'
            self.state = 'start'
            self.pathToOpen = pathToSave + '/' + stream.default_filename

        except Exception as e:
            print(e)
            self.update = 'unexpected error'

        self.root.ids.progress.stop()


    def folder(self):
        save_path = filedialog.askdirectory()

        if save_path is not None:
            self.root.ids.downloads.text = save_path


    def startFile(self):
        if self.pathToOpen is None:
            return False

        os.startfile(self.pathToOpen)


if __name__ == '__main__':
    Youtube().run()
