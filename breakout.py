# -*- coding: utf-8 -*-
"""
OOP design principles 

Uses Tkinter which is a standard GUI library in Python
Basic collision and input detection
Draw game objects without external assets
"""
import tkinter as tk

class Game(tk.Frame):

	"""
	Game class defines the global variables for the game.
	Tkinter has a Frame widget and a Canvas widget as a child.
	Instantiate the Frame to initialize.  Instantiate a Canvas
	with the width and height.
	"""

	def __init__(self, master):
		super().__init__(master)
		self.lives = 3
		self.width = 610
		self.height = 400
		self.canvas = tk.Canvas(self, bg='#aaaaff', 
								width=self.width, 
								height=self.height)





if __name__ == '__main__':
	root = tk.Tk()
	root.title("Breakout!")
	game = Game(root)
	game.mainloop()