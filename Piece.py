# �N���X: �ƂߊG�Ў��̂�\��
class Piece:
	# �t�B�[���h: �e���_���i�[�������X�g
	#
	# �^	>> :: [(int, int)]
	_vertexes: list

	# �R���X�g���N�^
	#
	# ����	>> vertexes :: [(int, int)]
	#
	# �����̉\���̂����O	>> PieceError
	def __init__(self, vertexes: list):
		if len(vertexes) < 3:
			#�񎟌��}�`�ɂ͒��_���Œ�3����͂��Ȃ񂾂�Ȃ�...
			# [��: ���] �������̓��{���pypy������@
			raise PieceError("Two dimensional figure should have at least three vertices ...")

		self._vertexes = vertexes

	# ���\�b�h: �^���R���X�g���N�^
	#
	# ����	>> vertexes :: [(int, int)]
	# �߂�l	>> Piece �N���X�̃I�u�W�F�N�g :: Piece
	#
	# �����̉\���̂����O	>> :: PieceError
	def new(vertexes: list):
		return Piece(vertexes)

	# ���\�b�h: _vertexes �̃Q�b�^�[
	#
	# �߂�l	>> _vertexes :: [(int, int)]
	def getVertexes(self) -> list:
		return self._vertexes


# �N���X: Piece �N���X�Ɋւ����O�p
class PieceError(Exception):
	# �t�B�[���h: ��O���e�̃��b�Z�[�W
	#
	# �^	>> :: str
	_message: str

	# �R���X�g���N�^
	#
	# ����	>> message :: str
	def __init__(self, message: str):
		self._message = message

	# ���\�b�h: _message �̃Q�b�^�[
	#
	# �߂�l	>> _message :: str
	def getMessage(self) -> str:
		return self._message


# �N���X: Piece�N���X�̃I�u�W�F�N�g�i�C���X�^���X�j�ɑ΂��鑀�쓙���
class PieceUtils:
	# ���\�b�h: 
	#
	# ����	>> 
	# �߂�l	>> 
	#
	# �����̉\���̂����O	>> :: PieceError
	@staticmethod
	def marge(x: Piece, y: Piece) -> Piece:
		pass

	# ���\�b�h: 
	#
	# ����	>> 
	# �߂�l	>> 
	#
	# �����̉\���̂����O	>> :: 
	@staticmethod
	def rotate(x: Piece) -> Piece:
		pass
