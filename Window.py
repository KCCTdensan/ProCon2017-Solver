﻿import tkinter as tk

class Window (tk.Frame):
	_btn_PieceInfo: tk.Button # 写真機による片の情報の取込ボタン
	_btn_FrameInfo: tk.Button # 写真機による枠の情報の取込ボタン
	_btn_FigureInfo: tk.Button # 「形状情報」の取込釦
	_btn_PlacemenIinfo: tk.Button # 「配置情報」の取込釦
	_canvas_cnvs: tk.Canvas # 描画領域
	# 等々
	_btn_quit: tk.Button # 終了ボタン

	def __init__(self, master = None):
		super().__init__(master)
		self.pack()
		master.title("ProCon2017-Solver")
		master.geometry("1000x400")
		self._createWidgets(master)

	def new(master = None):
		return Window(master)

	def _createWidgets(self, master = None):
		self._btn_PieceInfo = tk.Button(self,
			text	= "片情報取込",
			command = lambda: print("[押下] 片情報取込")
		)
		self._btn_PieceInfo.grid(column = 0, row = 0)

		self._btn_FrameInfo = tk.Button(self,
			text	= "枠情報取込",
			command = lambda: print("[押下] 枠情報取込")
		)
		self._btn_FrameInfo.grid(column = 0, row = 1)

		self._btn_FigureInfo = tk.Button(self,
			text	= "形状情報取込",
			command = lambda: print("[押下] 形状情報取込")
		)
		self._btn_FigureInfo.grid(column = 0, row = 2)

		self._btn_PlacementInfo = tk.Button(self,
			text	= "配置情報取込",
			command = lambda: print("[押下] 配置情報取込")
		)
		self._btn_placementinfo.grid(column = 0, row = 3)

		self._btn_quit = tk.Button(self,
			text = "終了",
			fg = "red",
			command = master.destroy
		)
		self._btn_quit.grid(column = 0, row = 4)