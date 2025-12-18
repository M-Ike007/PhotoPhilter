import json
import pandas as pd
from PIL import Image
from PIL.ExifTags import TAGS

# TODO make a class that is a metadata frame


def print_info(info_dict, data_dict):
    for label, value in info_dict.items():
        print(f"{label:25}: {value}")
    for label, value in data_dict.items():
        print(f"{label:25}: {value}")


def get_metdat(photopath):
    image = Image.open(photopath)

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

    metadata = info_dict | data_dict

    return metadata

def generate_dataframe(data):
    # make dataframe for metadata
    df_meta = pd.DataFrame(columns=data.keys())
    return df_meta


def add_to_dataframe(df_meta: pd.DataFrame, data: dict):
    df_meta = pd.concat([df_meta, pd.DataFrame([data])], ignore_index=True)
    return df_meta

def store_dataframes(df_meta: pd.DataFrame):
    with open('settings.json', 'r') as outfile:
        settings = json.load(outfile)
        # TODO add the file somehwere more sensible
    df_meta.to_csv(path_or_buf='metadata.csv')


if __name__ == '__main__':

    x = get_metdat("C:/Users/ike004/OneDrive - Wageningen University & Research/Desktop/foto\'s/004 - kopie.JPG")
    # print(x)
    # print('\nnext\n')
    # print(y)
    inf = generate_dataframe(x)
    print(inf)
    inf = add_to_dataframe(inf, x)
    store_dataframes(inf)


