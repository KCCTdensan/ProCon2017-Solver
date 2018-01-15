from Search.Piece import *
from Search.PuzzleSolver import *
from Search.Judge import *


if __name__ == '__main__':
	try:
		p1 = Piece.new([(1, 1), (2, 2), (3, 3), (4, 4)])
		p2 = Piece.new([(3, 3), (4, 4), (5, 5)])
		frame = Piece.new([(0,0),(4,0),(4,4),(0,4)])
		p3 = Piece.new([(0,0),(3,0),(0,3)])
		p4 = Piece.new([(0,0),(5,0),(5,1),(4,1)])
		p5 = Piece.new([(0,0),(2,0),(2,5),(1,5),(1,3),(0,3)])
		solver = PuzzleSolver.new()
		solver.appendPiece(p1)
		solver.appendPiece(p2)
		
		print(p1)
		print(p2)
		print(p3)

		Judgement = Judge.new();

		print(Judgement.isOverlapped(frame,p3))
		print(Judgement.isOverlapped(frame,p4))
		print(Judgement.isOverlapped(frame,p5))

		result = solver.solve()
		print(PuzzleSolverUtils.unwrapResult(result))
	except FigureError as pe:
		print("FigureError: " + pe.getMessage())
