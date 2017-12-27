# クラス: 嵌め絵片自体を表す
class Piece:
	# フィールド: 各頂点を格納したリスト
	#
	# 型	>> :: [(int, int)]
	_vertexes: list

	# コンストラクタ
	#
	# 引数	>> vertexes :: [(int, int)]
	#
	# 発生の可能性のある例外	>> PieceError
	def __init__(self, vertexes: list):
		if len(vertexes) < 3:
			#二次元図形には頂点が最低3つあるはずなんだよなぁ...
			# [求: 情報] ↓を↑の日本語でpypyする方法
			raise PieceError("Two dimensional figure should have at least three vertices ...")

		self._vertexes = vertexes
		
		# ここで角度算出等

	# メソッド: 疑似コンストラクタ
	#
	# 引数	>> vertexes :: [(int, int)]
	# 戻り値	>> Piece クラスのオブジェクト :: Piece
	#
	# 発生の可能性のある例外	>> :: PieceError
	def new(vertexes: list):
		return Piece(vertexes)

	# メソッド: _vertexes のゲッター
	#
	# 戻り値	>> _vertexes :: [(int, int)]
	def getVertexes(self) -> list:
		return self._vertexes

	# メソッド: 片を回転させる
	def rotate(self):
		pass

	# メソッド: 片を裏返す
	def flip(self):
		pass

	# メソッド: 片を移動させる
	def move(self):
		pass

	# メソッド: 
	#
	# 戻り値	>> か否か :: bool
	def isOnGrid(self) -> bool:
		pass


# クラス: Piece クラスに関する例外用
class PieceError(Exception):
	# フィールド: 例外内容のメッセージ
	#
	# 型	>> :: str
	_message: str

	# コンストラクタ
	#
	# 引数	>> message :: str
	def __init__(self, message: str):
		self._message = message

	# メソッド: _message のゲッター
	#
	# 戻り値	>> _message :: str
	def getMessage(self) -> str:
		return self._message


# クラス: Pieceクラスのオブジェクト（インスタンス）に対する操作等を提供
class PieceUtils:
	# メソッド: 片２つを結合して返す
	#
	# 引数	>> 片２つ :: Piece -> Piece
	# 戻り値	>> 結合された片 :: Piece
	#
	# 発生の可能性のある例外	>> :: 
	@staticmethod
	def marge(x: Piece, y: Piece) -> Piece:
		pass
