from .gameobject import GameObject

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