from Search.Figure import *
import numpy as np

class Piece (Figure):
	def __init__(self, vertexes: list):        
		#複素数1から複素数2の原点を中心とした角(deg)
		def angleBetweenComplexes(complex1, complex2):
			return (np.rad2deg(np.angle(complex2/complex1)) + 360) % 360

		#ベクトル1からベクトル2の原点を中心とした角(deg)
		def angleBetweenVectors(vector1, vector2):
			return angleBetweenComplexes(vector1[0] + 1j*vector1[1], vector2[0] + 1j*vector2[1])

		super().__init__(vertexes)
		# 角度群の算出
		self._angles = []
		numVertexes = len(vertexes)
		for i in range(0, numVertexes):
			self._angles.append(angleBetweenVectors(np.array(vertexes[(i - 1 + numVertexes) % numVertexes]) - np.array(vertexes[i]), np.array(vertexes[(i + 1) % numVertexes]) - np.array(vertexes[i])))

	def new(vertexes: list):
		return Piece(np.array(vertexes))

	# 片を回転させる
	def rotate(self):
		pass

	# 片を裏返す
	def flip(self):
		pass

	# 片を移動させる
	def move(self,point):
		for vertex in self.vertexes:
			vertex[0] += point  
			vertex[1] += point  
		vertexes[0] + vertex[0]
		vertexes[1] + vertex[1]

	def isOnGrid(self) -> bool:
		pass

	def isInAngle(self) -> bool:
		pass


class PieceUtils:
	# ２片を結合する
	@staticmethod
	def marge(x: Piece, y: Piece) -> Piece:
		pass
