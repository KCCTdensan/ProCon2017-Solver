from Piece import *

class PuzzleSolver:
	_pieces: list = [] #›Æ‚ßŠG•Ğ(PieceŒ^)‚ÌƒŠƒXƒg

	def new():
		return PuzzleSolver()
	
	def appendPiece(self, piece: Piece):
		self._pieces.append(piece)

	# ‚±‚Ìƒƒ\ƒbƒh‚Ìˆ—‚ğ•À—ñ‰»(‚ ‚é‚¢‚Í•½s‰»)‚µ‚Ä‰ğ‚Ì“±o‚ğ‘¬‚ß‚é
	# ƒAƒ‹ƒSƒŠƒYƒ€Ÿ‘æ‚Å‚·‚Ëª
	def solve(self) -> list:
		return self._pieces # æŠ¸‚¦‚¸ê_–·•Ô‚µ


class PuzzleSolverUtils:
	@staticmethod
	def unwrapResult(result: list) -> list:
		ret = []
		for (index, elem) in enumerate(result):
			ret.append(elem.getVertexes())
		return ret
