from Piece import *
from PuzzleSolver import *

if __name__ == '__main__':
	try:
		p1 = Piece.new([1,2,3,4])
		p2 = Piece.new([3,3,4,5,6])

		solver = PuzzleSolver.new()
		solver.appendPiece(p1)
		solver.appendPiece(p2)
		
		result = solver.solve()
		print(PuzzleSolverUtils.unwrapResult(result))
	except PieceError as pe:
		print("PieceError: " + pe.getMessage())
