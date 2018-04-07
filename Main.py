import tkinter as tk

from Window import *
# from Search.Piece import *
# from Search.PuzzleSolver import *

if __name__ == '__main__':
	root = tk.Tk()
	window =Window.new(master = root)
	window.mainloop()

"""	# 以下はSolverの使い方を記述したものです
	try:
		p1 = Piece.new([(1, 1), (2, 2), (3, 3), (4, 4)])
		p2 = Piece.new([(3, 3), (4, 4), (5, 5)])

		solver = PuzzleSolver.new()
		solver.appendPiece(p1)
		solver.appendPiece(p2)
		
		result = solver.solve()
		print(PuzzleSolverUtils.unwrapResult(result))
	except FigureError as pe:
		print("FigureError: " + pe.getMessage())
"""



