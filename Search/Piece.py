from Search.Figure import *
import numpy as np

class Piece (Figure):
	def __init__(self, vertexes: list):        
		super().__init__(vertexes)
		# 角度群の算出
		self._angles = []
		numVertexes = len(vertexes)
		for i in range(0, numVertexes):
			self._angles.append(angleBetweenVectors(np.array(vertexes[i - 1]) - np.array(vertexes[i]), np.array(vertexes[(i + 1) % numVertexes]) - np.array(vertexes[i])))

	# 複素数1から複素数2の原点を中心とした角(deg)
	def angleBetweenComplexes(complex1, complex2):
		return (np.angle(complex2/complex1, deg = True) + 360) % 360

	# ベクトル1からベクトル2の原点を中心とした角(deg)
	def angleBetweenVectors(vector1, vector2):
		return angleBetweenComplexes(vector1[0] + 1j*vector1[1], vector2[0] + 1j*vector2[1])

	def new(vertexes: list):
		return Piece(np.array(vertexes))

	# 片を回転させる
	def rotate(self):
		pass

	# 片を裏返す
	def flip(self):
		nextVertexes = []
		offset = 2 * vertexes[0][0]
		for vertex in vertexes:
			nextVertexes.append((offset - vertex[0], vertex[1]))
		vertexes = nextVertexes

	# 片を移動させる
	def move(self,point):
		for vertex in self.vertexes:
			vertex[0] += point  
			vertex[1] += point  
		vertexes[0] + vertex[0]
		vertexes[1] + vertex[1]

	# ピースの各頂点がグリッド上に存在するか(値が整数値であるか)
	def isOnGrid(self) -> bool:
		for vertex in vertexes:
			if not(isinstance(vertex[0],int)and isinstance(vertex[1],int)):
				return False
		return True


class PieceUtils:
	# ２片を結合する
	@staticmethod
	def marge(x: Piece, y: Piece) -> Piece:
		pass
