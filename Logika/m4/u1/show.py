from PIL import Image, ImageFilter

class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = []

    def open(self):
        try:
            self.original = Image.open('o.jpg')
            self.original.show()
        except:
            print('Файлу не існує')


    def do_left(self):
        left = self.original.transpobe(Image.ROTATE_90)
        self.changed.append(left)

        left.save('rotate_' + self.filename)

    def do_crop(self):
        box = (100, 100,200 ,200)
        cropped = self.original.crop(box)

        self.changed.append(cropped)
        cropped.save('cropped_' + self.filename)





img = ImageEditor('o.jpg')
img.open
img.do_crop()
