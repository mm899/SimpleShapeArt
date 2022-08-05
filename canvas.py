import numpy as np
from PIL import Image


class Canvas:

    """
    Object where all the shapes are going to be drawn
    """

    def __init__(self, width, height, colour):
        self.width = width
        self.height = height
        self.colour = colour

        # Create an empty numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Change the [0,0,0] RGB colour of the canvas to the user defined colour
        self.data[:] = self.colour

    def make(self, imagepath):
        """Converts the current array into an image file"""
        image_object = Image.fromarray(self.data, 'RGB')
        image_object.save(imagepath)
