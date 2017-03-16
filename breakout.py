# -*- coding: utf-8 -*-
"""
OOP design principles 

Uses Tkinter which is a standard GUI library in Python
Basic collision and input detection
Draw game objects without external assets
"""
import tkinter as tk
from brick import Brick
from paddle import Paddle
from ball import Ball

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
		self.canvas.pack()
		self.pack()
		self.items = {}
		self.ball = None
		self.paddle = Paddle(self.canvas, self.width / 2, 326)
		self.items[self.paddle.item] = self.paddle
		for x in range(5, self.width - 5, 75):
			self.add_brick(x + 37.5, 50, 2)
			self.add_brick(x + 37.5, 70, 1)
			self.add_brick(x + 37.5, 90, 1)

		self.hud = None
		self.setup_game()
		self.canvas.focus_set()			# bring the canvas to the focus to bind input elements
		self.canvas.bind('<Left>', lambda _: self.move(-10))
		self.canvas.bind('<Right>', lambda _: self.move(10))

	def setup_game(self):
		self.add_ball()
		self.update_lives_text()
		self.text = self.draw_text(300, 200, 'Press Space to Start')
		self.canvas.bind('<space>', lambda _: self.start_game())

	def add_ball(self):
		if self.ball is not None:
			self.ball.delete()
			paddle_coords = self.paddle.get_position()
			x = (paddle_coords[0] + paddle_coords[2]) * 0.5
			self.ball = Ball(self.canvas, x, 310)
			self.paddle.set_ball(self.ball)

	def add_brick(self, x, y, hits):
		brick = Brick(self.canvas, x, y, hits)
		self.items[brick.item] = brick

	def draw_text(self, x, y, text, size='40'):
		"""Display text messages to the canvas"""
		font = ('Helvitica', size)
		return self.canvas.create_text(x, y, text=text, font=font)

	def update_lives_text(self):
		text = 'Lives: %s' % self.lives
		if self.hud is None:
			self.hud = self.draw_text(50, 20, text, 15)
		else:
			self.canvas.itemconfig(self.hud, text=text)

	def start_game(self):
		pass

	def update(self):
		"""
		Gets the current position and width of the canvas.
		If the position collides with the left or right border of the canvas,
		the horizontal component of the direction vector changes its sign.
		If the position collides with the upper border of the canvas,
		the vertical component of the direction vector changes its sign.
		scale the direction vector by the ball's speed
		self.move(x, y) -> moves the ball
		"""
		coords = self.get_position()
		width = self.canvas.winfo_width()
		if coords[0] <= 0 or coords[2] >= width:
			self.direction[0] *= -1
		if coords[1] <= 0:
			self.direction[1] *= -1
		x = self.direction[0] * self.speed
		y = self.direction[1] * self.speed
		self.move(x, y)

	def collide(self, game_objects):
		"""
		Method handles the outcome of a collision with one or more bricks
		"""
		coords = self.get_position()
		x = (coords[0] + coords[2]) * 0.5
		if len(game_objects) > 1:
			self.direction[1] *= -1
		elif len(game_objects) == 1:
			game_object = game_objects[0]
			coords = game_object.get_position()
			if x > coords[2]:
				self.direction[0] = 1
			elif x < coords[0]:
				self.direction[0] = -1
			else:
				self.direction[1] *= -1

		for game_object in game_objects:
			if isinstance(game_object, Brick):
				game_object.hit()











if __name__ == '__main__':
	root = tk.Tk()
	root.title("Breakout!")
	game = Game(root)
	game.mainloop()