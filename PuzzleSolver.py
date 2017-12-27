from Piece import *

class PuzzleSolver:
	_pieces: list = [] #�ƂߊG��(Piece�^)�̃��X�g

	def new():
		return PuzzleSolver()
	
	def appendPiece(self, piece: Piece):
		self._pieces.append(piece)

	# ���̃��\�b�h�̏��������(���͕��s��)���ĉ��̓��o�𑬂߂�
	# �A���S���Y������ł��ˁ�
	#
	# ����: �}���`�X���b�h�ŏ������s����
	# ���s��: �}���`�v���Z�X�ŏ������s�����B�v���Z�X�P�ʂ̕����ɂ��A�}���`�R�A�ŏ����\�B
	# �Q�lURL >> https://qiita.com/castaneai/items/9cc33817419896667f34
	def solve(self) -> list:
		return self._pieces # �抸�����_���Ԃ�


class PuzzleSolverUtils:
	@staticmethod
	def unwrapResult(result: list) -> list:
		return [elem.getVertexes() for (_, elem) in enumerate(result)]
