# import required library
import video
import webbrowser

class Cinema(video.Video):
    # initialize class with a parameter title,description,poster and trailer
    def __init__(self,title,description,poster,trailer):
        # initialize parent class
        video.Video.__init__(self,title,description,poster)
        # set instance variable
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        # open url in a browser
        webbrowser.open(self.trailer_youtube_url)
