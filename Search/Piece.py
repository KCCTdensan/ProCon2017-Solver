from Search.Figure import *

class Piece (Figure):
	# ここに角度のデータを格納した変数等

	def __init__(self, vertexes: list):
		super().__init__(vertexes)

		# ここで角度の算出等

	def new(vertexes: list):
		return Piece(vertexes)

	# 片を回転させる
	def rotate(self,self_vertex1,self_vertex2,another_vertex1,another_vertex2):
		self_vertexes = self.getVertexes()
        # ベクトルにする
		vecter_self = self.vertexes[self_vertex2]-self.vertexes[self_vertex1]
		vecter_another = another.vertexes[another_vertex2]-another.vertexes[another_vertex1]
        # 内積やなんやらで角度を出す
		rotate_angle = math.acos(numpy.dot(vecter_self,vecter_another) / (numpy.linalg.norm(vecter_self) * numpy.linalg.norm(vecter_another)))
        # ↓回転行列
		rotate_matrix = numpy.matrix([
            [numpy.cos(rotate_angle) , -numpy.sin(rotate_angle)],
            [numpy.sin(rotate_angle) , numpy.cos(rotate_angle)]
            ])
        # 座標変更
		shifted_self_vertexes=numpy.squeeze(numpy.asarray((rotate_matrix*self_vertexes.T).T))
		return shifted_self_vertexes

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
