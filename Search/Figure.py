class Figure:
	_vertexes: list # 頂点を格納したリスト :: [(int, int)]

	def __init__(self, vertexes: list):
		if len(vertexes) < 3:
			raise FigureError("二次元図形には頂点が最低3つあるはずなんだよなぁ...")

		self._vertexes = vertexes

	def new(vertexes: list):
		return Figure(vertexes)

	def getVertexes(self) -> list:
		return self._vertexes


class FigureError (Exception):
	_message: str
	
	def __init__(self, message: str):
		self._message = message

	def getMessage(self) -> str:
		return self._message
