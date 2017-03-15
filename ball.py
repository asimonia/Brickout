from gameobject import GameObject

class Ball(GameObject):

	"""
	Ball class will store information about the speed, direction, and radius
	of the ball.  The direction vector will always be:

	[+, +] 		bottom-right
	[-, -]		upper-left
	[+, -]		top-right
	[-, +]		bottom-left

	Change the vector component when the ball bounces against
	canvas border, brick or paddle.
	"""

	def __init__(self, canvas, x, y):
		self.radius = 10
		self.direction = [1, -1]
		self.speed = 10
		item = canvas.create_oval(x - self.radius, y - self.radius,
								  x + self.radius, y + self.radius,
								  fill='white')
		super().__init__(canvas, item)