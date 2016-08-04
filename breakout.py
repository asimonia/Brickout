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
	pass


class Brick(GameObjectMixin):
	pass


if __name__ == '__main__':
	root = tk.Tk()
	root.title("Breakout")
	game = Game(root)
	game.mainloop()