import media
import fresh_tomatoes
toy_story = media.Movie("Toy story","A story of a boy and his toys",
	"https://i.ytimg.com/vi/6xQIHvEzUAs/hqdefault.jpg?custom=true&w=196&h=110&stc=true&jpg444=true&jpgq=90&sp=68&sigh=uOTM11AZtKA6rWKK3U7Ibc1pGWU",
	"https://www.youtube.com/watch?v=6xQIHvEzUAs")


toy_story2 = media.Movie("Toy story","A story of a boy and his toys",
	"https://i.ytimg.com/vi/6xQIHvEzUAs/hqdefault.jpg?custom=true&w=196&h=110&stc=true&jpg444=true&jpgq=90&sp=68&sigh=uOTM11AZtKA6rWKK3U7Ibc1pGWU",
	"https://www.youtube.com/watch?v=6xQIHvEzUAs")

music_liu = media.Movie("Liu ruoying","A music of singer named liu ruoying ","https://i.ytimg.com/vi/7BgkFlmzwzM/hqdefault.jpg?custom=true&w=196&h=110&stc=true&jpg444=true&jpgq=90&sp=68&sigh=Q8YSnkx5E7sij-b-9YbLs_9zcZU",
	"https://www.youtube.com/watch?v=7BgkFlmzwzM")


print toy_story.storyline
# toy_story.show_trailer()

# array
movie = [toy_story,toy_story2,music_liu]

# class variables
print media.Movie.VALID_RATING

# doc of the class Movie
print media.Movie.__doc__ 
fresh_tomatoes.open_movies_page(movie)