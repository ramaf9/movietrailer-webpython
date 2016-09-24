import cinema
import fresh_tomatoes

# create an object of cinema
theraid = cinema.Cinema("The raid",
                        "some action story from indonesia",
                        "https://upload.wikimedia.org/wikipedia/en/6/6b/The_Raid_Redemption.jpg",
                        "https://www.youtube.com/watch?v=7KJ0N7ik3yI"
                        )
kiminonawa = cinema.Cinema("Kimi no na wa",
                            "some anime ",
                            "https://a.ltrbxd.com/resized/film-poster/3/0/7/6/8/4/307684-your-name--0-230-0-345-crop.jpg?k=e1507d4401",
                            "https://youtu.be/hRfHcp2GjVI")
click = cinema.Cinema("Click!",
                            "some comedy ",
                            "http://www.gstatic.com/tv/thumb/movieposters/159128/p159128_p_v8_aa.jpg",
                            "https://youtu.be/APUqyhgtCfk")
batman = cinema.Cinema("Batman - The dark knight ",
                            "some comedy ",
                            "http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v8_aa.jpg",
                            "https://youtu.be/EXeTwQWrcwY")


# add object to arraylist
movies = [theraid,kiminonawa,click,batman]
# generate the html code
fresh_tomatoes.open_movies_page(movies);
