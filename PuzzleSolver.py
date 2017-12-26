from Piece import *

class PuzzleSolver:
	_pieces: list = [] #嵌め絵片(Piece型)のリスト

	def new():
		return PuzzleSolver()
	
	def appendPiece(self, piece: Piece):
		self._pieces.append(piece)

	# このメソッドの処理を並列化(あるいは平行化)して解の導出を速める
	# アルゴリズム次第ですね↑
	def solve(self) -> list:
		return self._pieces # 取敢えず鸚鵡返し


class PuzzleSolverUtils:
	@staticmethod
	def unwrapResult(result: list) -> list:
		ret = []
		for (index, elem) in enumerate(result):
			ret.append(elem.getVertexes())
		return ret
