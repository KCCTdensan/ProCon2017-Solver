from Piece import *

class PuzzleSolver:
	_pieces: list = [] #嵌め絵片(Piece型)のリスト

	def new():
		return PuzzleSolver()
	
	def appendPiece(self, piece: Piece):
		self._pieces.append(piece)

	# このメソッドの処理を並列化(或は並行化)して解の導出を速める
	# アルゴリズム次第ですね↑
	#
	# 並列化: マルチスレッドで処理を行う事
	# 並行化: マルチプロセスで処理を行う事。プロセス単位の分離により、マルチコアで処理可能。
	# 参考URL >> https://qiita.com/castaneai/items/9cc33817419896667f34
	def solve(self) -> list:
		return self._pieces # 取敢えず鸚鵡返し


class PuzzleSolverUtils:
	@staticmethod
	def unwrapResult(result: list) -> list:
		return [elem.getVertexes() for (_, elem) in enumerate(result)]
