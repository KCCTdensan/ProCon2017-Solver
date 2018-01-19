from Search.Piece import *
#from Search.Frame import *

class PuzzleSolver:
	_pieces: list = [] #嵌め絵片(Piece型)のリスト

	def new():
		return PuzzleSolver()
	
	def appendPiece(self, piece: Piece):
		self._pieces.append(piece)

	# 参考 >> https://qiita.com/castaneai/items/9cc33817419896667f34
	def solve(self) -> list:
		return self._pieces # 取敢えず、蓄積した片のリストを返すだけ


class PuzzleSolverUtils:
	@staticmethod
	def unwrapResult(result: list) -> list:
		return [elem.getVertexes() for (_, elem) in enumerate(result)]
