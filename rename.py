import glob
import os
import tqdm

camera_num = "D3"

def read_files(path):
    images = [file for file in os.listdir(path) if file.endswith('.png')]

    for image in tqdm.tqdm(images):
        src = image
        dst = os.path.join(f'{camera_num}_{os.path.basename(image)}')
        # dst = os.path.join(f'{os.path.basename(image)[3:]}')
        print(f'src: {src}')
        print(f'dst: {dst}')
        os.rename(src, dst)

    print(f'completed: {path}')

root_path = './'

read_files(root_path)