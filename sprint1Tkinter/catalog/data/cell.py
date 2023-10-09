from PIL import Image, ImageTk

class Cell:
    def __init__(self, title, image_path):
        self.title = title
        self.image_path = image_path
        self.image_tk = self._load_image(image_path)

    def _load_image(self, image_path):
        image = Image.open(image_path)
        return ImageTk.PhotoImage(image)