﻿from Search.Piece import *
#from Search.Frame import *

class PuzzleSolver:
	_frame: Frame # 枠
	_pieces: list = [] #片のリスト

	def new():
		return PuzzleSolver()

	def setFrame(self, frame: Frame):
		self._frame = frame
		
	def appendPiece(self, piece: Piece):
		self._pieces.append(piece)

	def solve(self) -> list:
		return self._pieces # 取敢えず、蓄積した片のリストを返すだけ


class PuzzleSolverUtils:
	@staticmethod
	def unwrapResult(result: list) -> list:
		return [elem.getVertexes() for (_, elem) in enumerate(result)]
