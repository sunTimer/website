import webbrowser






class Video():
	def __init__(self,title,views,poster_image,trailer_youtube):
		print "Parent class construtor called"
		self.title = title
		self.views = views
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube


class Movie(Video):
	"""This class provides a way to store movie related information"""
	# VALID_RATING= ['G','PG']
	def __init__(self,movie_title,views,poster_image,trailer_youtube,movie_storyline,movie_director="shixu"):
		Video.__init__(self,movie_title,views,poster_image,trailer_youtube)
		self.storyline = movie_storyline
		self.movie_director = movie_director


	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)



class Music(Video):
	"""This class provides a way to store music related information"""
	def __init__(self,music_title,views,poster_image,trailer_youtube,singer):
		Video.__init__(self,music_title,views,poster_image,trailer_youtube)
		self.singer = singer


	def show_singer(self):
		print "Singer's name is "+self.singer




# song_1 = Music("hello",1000,"url of img","url of video","jack chou")
# song_1.show_singer()