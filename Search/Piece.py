from Search.Figure import *
import numpy

class Piece (Figure):
	# ここに角度のデータを格納した変数等

	def __init__(self, vertexes: list):
		super().__init__(vertexes)

		# ここで角度の算出等

	def new(vertexes: list):
		#return Piece(vertexes)
		return Piece(numpy.array(vertexes))

	# 片を回転させる
	def rotate(self):
		pass

	# 片を裏返す
	def flip(self):
		pass

	# 片を移動させる
	def move(self):
		pass

	def isOnGrid(self) -> bool:
		pass

	def isInAngle(self) -> bool:
		pass


class PieceUtils:
	# ２片を結合する
	@staticmethod
	def marge(x: Piece, y: Piece) -> Piece:
		pass
