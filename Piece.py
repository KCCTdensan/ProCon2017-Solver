class Piece:
	_vertexes: list # ’¸“_(intŒ^)‚ğŠi”[‚µ‚½ƒŠƒXƒg

	def __init__(self, vertexes: list):
		if len(vertexes) < 3:
			#“ñŸŒ³}Œ`‚É‚Í’¸“_‚ªÅ’á3‚Â‚ ‚é‚Í‚¸‚È‚ñ‚¾‚æ‚È‚Ÿ..."
			# [‹: î•ñ] “ú–{Œê‚Åpypy‚·‚é•û–@
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
	def marge(x: Piece, y: Piece):
		pass

	@staticmethod
	def rotate(x: Piece):
		pass
