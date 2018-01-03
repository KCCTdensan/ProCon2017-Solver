﻿from Search.Figure import *
import numpy as np
class Piece (Figure):
	def __init__(self, vertexes: list):
		super().__init__(vertexes)

		# ここで角度の算出等
		self._angles = []
		for i,vertex in enumerate(vertexes):
			vec_front = np.array(vertexes[(i + 1) % len(vertexes)]) - np.array(vertex)
			vec_back = np.array(vertexes[(i - 1 + len(vertexes)) % len(vertexes)]) - np.array(vertex)
			inner_product = np.dot(vec_front,vec_back)
			rad = np.arccos(float(inner_product) / (np.linalg.norm(vec_front) * np.linalg.norm(vec_back)))
			if rad == 0.0:
				raise FigureError("角度が0度")
			angle = np.rad2deg(rad)
			#if judge.is_in_angle(self,vertex)==false: #外角だった場合
			#	angle = 360.0 - angle
			self._angles.append(angle)

	def new(vertexes: list):
		return Piece(vertexes)

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
