#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
OOP design principles 

Uses Tkinter which is a standard GUI library in Python
Basic collision and input detection
Draw game objects without external assets
"""
import tkinter as tk
from gameobjects.brick import Brick
from gameobjects.paddle import Paddle
from gameobjects.ball import Ball

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
		self.canvas.pack()		# displays widgets on the parent container
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

		# bring the canvas to the focus to bind input elements
		# Key input binding, syntax: (event and event handler)
		self.canvas.focus_set()
		self.canvas.bind('<Left>', lambda _: self.paddle.move(-10))
		self.canvas.bind('<Right>', lambda _: self.paddle.move(10))

	def setup_game(self):
		self.add_ball()
		self.update_lives_text()
		self.text = self.draw_text(300, 200, 'Press Space to Start')
		self.canvas.bind('<space>', lambda _: self.start_game())

	def add_ball(self):
		"""Add ball during initialization"""
		if self.ball is not None:
			self.ball.delete()
		paddle_coords = self.paddle.get_position()
		x = (paddle_coords[0] + paddle_coords[2]) * 0.5
		self.ball = Ball(self.canvas, x, 310)
		self.paddle.set_ball(self.ball)

	def add_brick(self, x, y, hits):
		"""Add brick during initialization"""
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
		self.canvas.unbind('<space>')
		self.canvas.delete(self.text)
		self.paddle.ball = None
		self.game_loop()

	def game_loop(self):
		self.check_collisions()
		num_bricks = len(self.canvas.find_withtag('brick'))
		if num_bricks == 0: 
			self.ball.speed = None
			self.draw_text(300, 200, 'You win!')
		elif self.ball.get_position()[3] >= self.height: 
			self.ball.speed = None
			self.lives -= 1
			if self.lives < 0:
				self.draw_text(300, 200, 'Game Over')
			else:
				self.after(1000, self.setup_game)
		else:
			self.ball.update()
			self.after(50, self.game_loop)

	def check_collisions(self):
		ball_coords = self.ball.get_position()
		items = self.canvas.find_overlapping(*ball_coords)
		objects = [self.items[x] for x in items if x in self.items]
		self.ball.collide(objects)




if __name__ == '__main__':
	root = tk.Tk()
	root.title("Breakout!")
	game = Game(root)
	game.mainloop()