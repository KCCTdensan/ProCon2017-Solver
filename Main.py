import tkinter as tk

from Window import *
# from Search.Piece import *
# from Search.PuzzleSolver import *
# from Search.Judge import *


def main():
	root = tk.Tk()
	Window.new(master = root)
	root.mainloop()

"""	# 以下はSolverの使い方を記述したものです
	try:
		f = Frame.new(30, 40) # 左右の頂点数: 30, 上下の頂点数: 40
		p1 = Piece.new([(1, 1), (2, 2), (3, 3), (4, 4)])
		p2 = Piece.new([(3, 3), (4, 4), (5, 5)])

		solver = PuzzleSolver.new()
		solver.setFrame(f)
		solver.appendPiece(p1)
		solver.appendPiece(p2)
		
		result = solver.solve()
		print(PuzzleSolverUtils.unwrapResult(result))
	except FigureError as fe:
		print("FigureError: " + fe.getMessage())
"""

if __name__ == '__main__':
	main()
