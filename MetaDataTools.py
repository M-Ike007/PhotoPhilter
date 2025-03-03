from PIL import Image
from PIL.ExifTags import TAGS

# TODO make a class that is a metadata frame


def get_metdat(photo):
    image = Image.open(photo)

    # extract basic metadata
    info_dict = {
        "Filename": image.filename,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode,
        "Image is Animated": getattr(image, "is_animated", False),
        "Frames in Image": getattr(image, "n_frames", 1)
    }

    # extract EXIF data
    exifdata = image.getexif()

    data_dict = {}
    # iterating over all EXIF data fields
    for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        # decode bytes
        if isinstance(data, bytes):
            data = data.decode(encoding='latin-1')
        data_dict[tag] = data

    for label, value in info_dict.items():
        print(f"{label:25}: {value}")
    for label, value in data_dict.items():
        print(f"{label:25}: {value}")

    return info_dict, data_dict

