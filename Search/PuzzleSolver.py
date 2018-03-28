from Search.Piece import *
#from Search.Frame import *

class PuzzleSolver:
	_frame: Frame # 枠
	_pieces: list = [] #片のリスト

	MergedPieces = [] #mergeしたpieceのリスト

	def new():
		return PuzzleSolver()

	def setFrame(self, frame: Frame):
		self._frame = frame
		
	def appendPiece(self, piece: Piece):
		self._pieces.append(piece)

	def solve(self) -> list:
		if len(self._pieces) == 0:#完成
			return True
		for piece in self._pieces:
			for i in range(len(piece._vertexes)):#pieceごとにすべての辺の組合わせをみる
				if Judge.isMarge(self._frame, piece, piece.vertexes[i], piece.vertexes[(i+1) % len(piece.vertexes)]):
					self._frame.marge(piece, piece.vertexes[i], piece.vertexes[(i+1) % len(piece.vertexes)])
					#self._vertexesからmergeしたpieceを削除
					PuzzleSolver.MergedPieces += piece #pieceがmergeされる際の座標をスタックにプッシュ
					Solver = PuzzleSolver.new(self._frame, self._pieces)
					return PuzzleSolver.solve()
		PuzzleSolver.MergedPieces.pop() #スタックからポップ
		return False #このルートは完成までたどり着けない


class PuzzleSolverUtils:
	@staticmethod
	def unwrapResult(result: list) -> list:
		return [elem.getVertexes() for (_, elem) in enumerate(result)]
