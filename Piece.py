import math
import numpy as np

class Piece:
	_vertexes: list # 頂点((int, int)型)を格納したリスト
	_angles: list # 角度を格納したリスト

	def __init__(self, vertexes: list):
		if len(vertexes) < 3:
			raise PieceError("二次元図形には頂点が最低3つあるはずなんだよなぁ...")

		self._vertexes = vertexes

		# ここで角度の算出等
		for i,vertex in enumerate(vertexes):
			vec_front = np.array(vertexes[(i + 1) % len(vertexes)]) - np.array(vertex)
			vec_back = np.array(vertexes[(i - 1 + len(vertexes))]) - np.array(vertex)
			inner_product = np.dot(vec_front,vec_back)
			a=np.linalg.norm(vec_front)
			b=np.linalg.norm(vec_back)
			angle = math.acos(inner_product / np.linalg.norm(vec_front) * np.linalg.norm(vec_back))
			#if judge.is_in_angle(self,vertex)==false:
			#	angle = 2 * math.pi - angle
			self._angles.append(angle)

	def new(vertexes: list):
		return Piece(vertexes)

	def getVertexes(self) -> list:
		return self._vertexes

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


class PieceError(Exception):
	_message: str
	
	def __init__(self, message: str):
		self._message = message

	def getMessage(self) -> str:
		return self._message


class PieceUtils:
	# ２片を結合する
	@staticmethod
	def marge(x: Piece, y: Piece) -> Piece:
		pass
