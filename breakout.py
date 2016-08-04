import tkinter as tk


class Game(tk.Frame):
	"""Class for our basic GUI layout"""
	def __init__(self, master):
		super(Game, self).__init__(master)
		self.lives = 3
		self.width = 610
		self.height = 400
		self.canvas = tk.Canvas(self, bg="#aaaaff",
								width=self.width,
								height=self.height)
		self.canvas.pack()
		self.pack()


class GameObjectMixin:
	"""Ball, Paddle and Brick inherit from this Mixin"""
	def __init__(self, canvas, item):
		self.canvas = canvas
		self.item = item

	def get_position(self):
		return self.canvas.coords(self.item)

	def move(self, x, y):
		self.canvas.move(self.item, x, y)

	def delete(self):
		self.canvas.delete(self.item)


class Ball(GameObjectMixin):
	"""Create ball and initialize radius; moves towards top right"""
	def __init__(self, canvas, x, y):
		self.radius = 10
		self.direction = [1, -1]
		self.speed = 10
		item = canvas.create_oval(x - self.radius, y - self.radius,
								  x + self.radius, y + self.radius, fill='red')
		super(Ball, self).__init__(canvas, item)


class Paddle(GameObjectMixin):
	def __init__(self, canvas, x, y):
		self.width = 80
		self.height = 10
		self.ball = None
		item = canvas.create_rectangle(x - self.width / 2,
									   y - self.height / 2,
									   x + self.width / 2,
									   y + self.height /2,
									   fill='blue')
		super(Paddle, self).__init__(canvas, item)

	def set_ball(self, ball):
		sefl.ball = ball

	def move(self, offset):
		coords = self.get_position()
		width = self.canvas.winfo_width()
		if coords[0] + offset >= 0 and \
			coords[2] + offset <= width:
			super(Paddle, self).move(offset, 0)
			if self.ball is not None:
				self.ball.move(offset, 0)

class Paddle(GameObjectMixin):
	pass


class Brick(GameObjectMixin):
	pass


if __name__ == '__main__':
	root = tk.Tk()
	root.title("Breakout")
	game = Game(root)
	game.mainloop()