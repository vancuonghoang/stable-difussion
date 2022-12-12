import os
import glob
import io
import json
from PIL import Image
from tqdm import tqdm

# save_root = 'data_v1/closed_mouth'
# 1girl
# green_background
# hat
save_root = r'C:\Users\hvcuong3\Desktop\imagen_data\data_v1\jewelry'
os.makedirs(save_root, exist_ok=True)
search_root = r'C:\Users\hvcuong3\Desktop\imagen_data\raw'
label = save_root.split('\\')[-1]
labels = ['1girl', 'aqua_eyes', 'baseball_cap', 'blonde_hair', 'earrings', 'green_background', 'jewelry',
         'hat', 'short_hair', 'closed_mouth']

print(search_root)
for image in tqdm(glob.glob(f"{search_root}\{label}\*image")):
    # print(image)
    name = image.split('\\')[-1]
    name = name[:-6]
    if os.path.exists(f"{save_root}/{name}.png"):
        continue
    annotation = []
    with open(f"{search_root}\{label}\{name}.caption", 'r') as f1:
        tag_string_general = json.load(f1)
    tag_string_general = tag_string_general['tag_string_general']
    for a in tag_string_general.split():
        if a in labels:
            annotation.append(a)
    with open(f"{save_root}/{name}.txt", 'w') as anno:
        anno.write(' '.join(annotation))

    with open(image, 'rb') as f:
        image_byte = bytearray(f.read())
    image = Image.open(io.BytesIO(image_byte))
    # print(image_byte)
    image.save(f"{save_root}/{name}.png")
    # break