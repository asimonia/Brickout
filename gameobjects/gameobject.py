class GameObject:

	"""
	Base class for all objects.
	Get the position, move, and delete objects.
	"""

	def __init__(self, canvas, item):
		self.canvas = canvas
		self.item = item

	def get_position(self):
		"""Returns the coordinates of the bounding box of an item."""
		return self.canvas.coords(self.item)

	def move(self, x, y):
		"""Moves an item by a horizonal and vertical offset."""
		return self.move(self.item, x, y)

	def delete(self):
		"""Deletes an item off the canvas."""
		return self.delete(self.item)