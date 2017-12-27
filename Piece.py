class Piece:
	_vertexes: list # 頂点((int, int)型)を格納したリスト

	def __init__(self, vertexes: list):
		if len(vertexes) < 3:
			#二次元図形には頂点が最低3つあるはずなんだよなぁ...
			# [求: 情報] 日本語でpypyする方法
			raise PieceError("Two dimensional figure should have at least three vertices ...")

		self._vertexes = vertexes

	def new(vertexes: list):
		return Piece(vertexes)

	def getVertexes(self) -> list:
		return self._vertexes


class PieceError(Exception):
	_message: str
	
	def __init__(self, message: str):
		self._message = message

	def getMessage(self) -> str:
		return self._message


class PieceUtils:
	@staticmethod
	def marge(x: Piece, y: Piece) -> Piece:
		pass

	@staticmethod
	def rotate(x: Piece) -> Piece:
		pass
