class Piece:
	_vertexes: list # ���_(int�^)���i�[�������X�g

	def __init__(self, vertexes: list):
		if len(vertexes) < 3:
			#�񎟌��}�`�ɂ͒��_���Œ�3����͂��Ȃ񂾂�Ȃ�..."
			# [��: ���] ���{���pypy������@
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
