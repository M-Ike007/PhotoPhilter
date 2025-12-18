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

    return info_dict, data_dict

def generate_dataframes(info, data):
    # make info dataframe
    df_info = pd.DataFrame(columns=info.keys())
    # make dataframe for EXIF metadata
    df_exif = pd.DataFrame(columns=data.keys())
    return df_info, df_exif


def store_metadata(dfi: pd.DataFrame, dfe: pd.DataFrame, info: dict, data: dict):
    dfi = pd.concat([dfi, pd.DataFrame([info])], ignore_index=True)
    dfe = pd.concat([dfe, pd.DataFrame([data])], ignore_index=True)
    return dfi, dfe



if __name__ == '__main__':
    x, y = get_metdat("C:/Users/ike004/OneDrive - Wageningen University & Research/Desktop/foto\'s/004 - kopie.JPG")
    # print(x)
    # print('\nnext\n')
    # print(y)
    inf, exif = generate_dataframes(x, y)
    print(inf, exif)
    inf, exif = store_metadata(inf, exif, x, y)
    print(inf.to_string(), '\n', exif.to_string())


