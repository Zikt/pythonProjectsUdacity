import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        " a boy and his toys come to life...",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4")

sound_of_music = media.Movie("Sound of Music",
                             "A beautiful family life...",
                             "https://upload.wikimedia.org/wikipedia/en/c/c6/Sound_of_music.jpg",
                             "https://www.youtube.com/watch?v=5fH2FOn1V5g")
                             


#print(avatar.storyline)
#avatar.show_trailer()

#sound_of_music.show_trailer()

movies = [toy_story,avatar,sound_of_music]
fresh_tomatoes.open_movies_page(movies)

