import media
import fresh_tomatoes
crazy_animal_city = media.Movie("Crazy Animal City",1000,
	"https://i.ytimg.com/vi/x9lgmyc5VJo/hqdefault.jpg?custom=true&w=196&h=110&stc=true&jpg444=true&jpgq=90&sp=68&sigh=_btAVTY8-t7DAgUO0Mqe5XTUJFI",
	"https://www.youtube.com/watch?v=yxF4kqADYlI",
	"A story of animals")


kongfu_panda = media.Movie("KongFu Panda","222,234",
	"https://i.ytimg.com/vi/9AJITKu-Cic/hqdefault.jpg?custom=true&w=120&h=90&jpg444=true&jpgq=90&sp=68&sigh=ETu89KC3Agolw-ecVCFAdO9gd5Q",
	"https://www.youtube.com/watch?v=9AJITKu-Cic",
	"A story of panda")

return_of_king = media.Movie("Return of the King","123,233",
	"https://i.ytimg.com/vi/71EXHEHFz5U/hqdefault.jpg?custom=true&w=196&h=110&stc=true&jpg444=true&jpgq=90&sp=68&sigh=cac6jMlsVGM6vfMNZNeYxqqKfTE",
	"https://www.youtube.com/watch?v=71EXHEHFz5U",
	"King")

ice_age = media.Movie("Ice Age","212,123",
	"https://i.ytimg.com/vi/HOsDOsk19lI/hqdefault.jpg?custom=true&w=196&h=110&stc=true&jpg444=true&jpgq=90&sp=68&sigh=Iy9aGwvqIl73ugRqgmqJ5_ArORQ",
	"https://www.youtube.com/watch?v=HOsDOsk19lI","aha")

lover_from_past = media.Music("Lover from past","3223,333,123",
	"https://i.ytimg.com/vi/j9k3liT2MLo/hqdefault.jpg?custom=true&w=196&h=110&stc=true&jpg444=true&jpgq=90&sp=68&sigh=AtYpy6WAu_B-rkWuxi7yTGlWHfA",
	"https://www.youtube.com/watch?v=j9k3liT2MLo",
	"Jay Chou")

party_animal = media.Music("Party animal","322,343",
	"https://i.ytimg.com/vi/Fn7NLWHJw4s/hqdefault.jpg?custom=true&w=196&h=110&stc=true&jpg444=true&jpgq=90&sp=68&sigh=Q9F2Psk8WJhWUnfugSWu10PsDvs",
	"https://www.youtube.com/watch?v=Fn7NLWHJw4s","May Day")

secret = media.Music("Secret","433,324,222",
	"https://i.ytimg.com/vi/uIWypArI73w/hqdefault.jpg?custom=true&w=196&h=110&stc=true&jpg444=true&jpgq=90&sp=68&sigh=_9XJn17eoFNUkIY-ImEVrjUektA",
	"https://www.youtube.com/watch?v=uIWypArI73w","Jay Chou")
hello = media.Music("Hello","544,333,222",
	"https://i.ytimg.com/vi/YQHsXMglC9A/hqdefault.jpg?custom=true&w=196&h=110&stc=true&jpg444=true&jpgq=90&sp=68&sigh=6HaIXywQKQrYOZlAeFVW9oI_0Os",
	"https://www.youtube.com/watch?v=YQHsXMglC9A","Adele")
	
# print toy_story.storyline
# toy_story.show_trailer()

# array
movies = [crazy_animal_city,kongfu_panda,return_of_king,ice_age]
musics = [lover_from_past,party_animal,secret,hello]
# class variables
# print media.Movie.VALID_RATING

# doc of the class Movie
print media.Movie.__doc__ 


fresh_tomatoes.open_movies_page(movies, musics)