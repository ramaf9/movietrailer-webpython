class Video():
    # check the usage of this class
    if __name__ == "__main__":
        print("one.py is being run directly")
    else:
        print("one.py is being imported into another module")
    # initialize class with parameter title,description,poster
    def __init__(self,title,description,poster):
        # set instance variable
        self.title = title;
        self.description = description;
        self.poster_image_url = poster;
