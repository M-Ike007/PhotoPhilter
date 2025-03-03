from os import listdir
import json
import pathlib


# class that determines photo. should work on its own.
class Pictures:
    def __init__(self):
        self.directory = self.get_dir()

        # Define photo storage places
        self.images = []
        self.other_files = []
        self.extensions = []    # TODO use this somewhere

        # widgets
        self.get_images()

    def get_dir(self):
        with open("settings.json") as json_file:
            json_data = json.load(json_file)
            json_file.close()
        return json_data['directory']

    def get_images(self):
        # returns a list with names of all images of appropriate datatypes
        for file in listdir(self.directory):
            if file.endswith(".jpg") or file.endswith('.png') or file.endswith('.PNG') or file.endswith('.JPG'):
                self.images.append(file)
            else:
                self.other_files.append(file)
                if pathlib.Path(file).suffix not in self.extensions:        # fills a list with all unused extensions
                    self.extensions.append(pathlib.Path(file).suffix)
        # check if all items are either in images or in other_files
        if len(self.images) + len(self.other_files) != len(listdir(self.directory)):
            print("in function 'get images', some files have not been accounted for")

    def reset(self):
        ...     # TODO method that resets the self.images list and rechecks for images in CURRENT directory

    def report(self):
        print('currently stored pictures:', len(self.images))
        for image in self.images:
            print(image, self.images[image])
        print('\n')
        print('other stuff:', len(self.other_files))
        for item in self.other_files:
            print(item, self.other_files[item])
        print('\n')
        return ...  # TODO define return statement

    def get_image(self, position: str = 'start', fullpath=False):
        if position == 'start':
            if fullpath:
                my_str = self.directory + "/" + self.images[0]
            else:
                my_str = self.images[0]
        elif position == 'end':
            if fullpath:
                my_str = self.directory + "/" + self.images[-1]
            else:
                my_str = self.images[-1]
        elif position == 'middle':
            if fullpath:
                my_str = self.directory + "/" + self.images[int(len(self.images)/2)]
            else:
                my_str = self.images[int(len(self.images)/2)]
        else:
            my_str = ''
            print('wrong input for position')
        return my_str

    def add(self, other):
        self.images.append(other)
        return self.images

    def remove(self, other):
        if other in self.images:
            self.images.remove(other)
        else:
            print(other, 'not found')

    def __repr__(self):
        return 'Pictures Object containing: {}'.format(self.images)

    def __le__(self, other):
        return len(self.images) <= other

    def __eq__(self, other):
        return self.images == other

    def __ne__(self, other):
        return self.images != other

    def __lt__(self, other):
        return len(self.images) < other

    def __gt__(self, other):
        return len(self.images) > other

    def __ge__(self, other):
        return len(self.images) >= other

    def __len__(self):
        return len(self.images)

    def __iter__(self):
        return iter(self.images)

    # TODO add append and remove features with dunder. take out the studying_this functions that currently do this.


if __name__ == '__main__':
    pictures = Pictures()
    pictures.get_images()
