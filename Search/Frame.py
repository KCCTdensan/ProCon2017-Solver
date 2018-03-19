from Search.Figure import *

class Frame (Figure):
	def __init__(self, width: int, height, int):
		self._vertexes = [(0, 0), (width, 0), (0, height), (width, height)]

	def new(width: int, height: int):
		return Frame(width, height)
