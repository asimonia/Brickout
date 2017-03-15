from gameobject import GameObject

class Brick(GameObject):

	COLORS = {1: '#999999', 2: '#555555', 3: '#222222'}

	def __init__(self, canvas, x, y, hits):
		self.width = 75
		self.height = 20
		self.hits = hits
		color = Brick.COLORS[hits]
		item = canvas.create_rectange(x - self.width / 2,
									  y - self.height / 2,
									  x + self.width / 2,
									  y + self.height / 2,
									  fill=color,
									  tags='brick')
		super().__init__(canvas, item)

	def hit(self):
		"""Decrease paddle hits when hit, until it disappears.
		   Change the color of the brick when hit.
		"""
		self.hits -= 1
		if self.hits == 0:
			self.delete()
		else:
			self.canvas.itemconfig(self.item, fill=Brick.COLORS[self.hits])
