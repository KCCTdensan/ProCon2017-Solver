from Piece import *

class PuzzleSolver:
	_pieces: list = [] #�ƂߊG��(Piece�^)�̃��X�g

	def new():
		return PuzzleSolver()
	
	def appendPiece(self, piece: Piece):
		self._pieces.append(piece)

	# ���̃��\�b�h�̏��������(���邢�͕��s��)���ĉ��̓��o�𑬂߂�
	# �A���S���Y������ł��ˁ�
	def solve(self) -> list:
		return self._pieces # �抸�����_���Ԃ�


class PuzzleSolverUtils:
	@staticmethod
	def unwrapResult(result: list) -> list:
		ret = []
		for (index, elem) in enumerate(result):
			ret.append(elem.getVertexes())
		return ret
