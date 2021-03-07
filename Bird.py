from PIL import Image

class Bird:
        
    def __init__(self, x_new, y_new, image_path_new):
        self.x = x_new
        self.y = y_new
        self.image_path = image_path_new
        self.image = Image.open(image_path_new)
        self._update_size()
        self._update_edges()

    def update(self, x_new, y_new, image_path_new):
        self.x = x_new
        self.y = y_new
        self.image_path = image_path_new
        self.image = Image.open(image_path_new)
        self._update_size()
        self._update_edges()

    def _update_size(self):
        self.width, self.height = self.image.size        

    def _update_edges(self):
        # Define the edges of the image
        self.left_edge = self.x
        self.right_edge = self.x + self.width
        self.top_edge = self.y
        self.bottom_edge = self.y + self.height

    def get_image_path(self):
        return self.image_path

    def get_size(self):
        return self.width, self.height

    def get_edges(self):
        return self.left_edge, self.right_edge, self.top_edge, self.bottom_edge

    def get_corners(self):

        # Get the corner coordinates
        top_left = (self.left_edge, self.top_edge)
        top_right = (self.right_edge, self.top_edge)
        bottom_left = (self.left_edge, self.bottom_edge)
        bottom_right = (self.right_edge, self.bottom_edge)

        # Return the list of corners
        return [top_left, top_right, bottom_left, bottom_right]