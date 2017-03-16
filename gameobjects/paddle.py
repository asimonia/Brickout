from .gameobject import GameObject

class Paddle(GameObject):

	def __init__(self, canvas, x, y):
		self.width = 80
		self.height = 10
		self.ball = None
		item = canvas.create_rectangle(x - self.width / 2,
									   y - self.height / 2,
									   x + self.width / 2,
									   y + self.height / 2,
									   fill='blue')
		super().__init__(canvas, item)

	def set_ball(self, ball):
		self.ball = ball

	def move(self, offset):
		coords = self.get_position()			# gets the coords of the paddle
		width = self.canvas.winfo_width()		# gets the canvas width
		# if the min and max x coords plus offset from movement
		# are inside the boundaries of the canvas, then move the paddle
		# if the paddle still has a reference to the ball, move the ball
		if coords[0] + offset >= 0 and coords[2] + offset <= width:
			super().move(offset, 0)
			if self.ball is not None:
				self.ball.move(offset, 0)
