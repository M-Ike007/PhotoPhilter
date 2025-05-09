class Analyze:
    def __init__(self):
        self.names = ['img.img', '004.jpg', '005.jpg', '006.jpg', '006.png', '123.img', 'cheese.jpeg', 'cheese.jpeg', '004.jpg']
        self.seen = set()
        self.dupes = []

    # TODO method that checks for doubles
        # in names
    def find_doubles(self):     # For doubles, normally
        for x in self.names:
            if x in self.seen:
                self.dupes.append(x)
            else:
                self.seen.add(x)
        # photowise (contents)
        # Image hashing
        # https://pyimagesearch.com/2017/11/27/image-hashing-opencv-python/
        

        # with dates

    # TODO method that compares current photo to all other photos and
    # shows fotos with high(est) resemblance.
        # contents wise

        # date wise

        # color histogram wise

        # color distribution wise

    # TODO create some models that are trained on the available photos within the directory

    # TODO probably need parallel processing? could try but could also do later....

    # TODO how blurry is an image?

    # TODO can convolutions be useful? (from machine learning course, deep learning lecture nr.2)


if __name__ == '__main__':
    print('hi')
    analysis = Analyze()
    analysis.find_doubles()
    print(analysis.dupes)
