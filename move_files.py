import glob
import os
import tqdm

def read_files(path):
    directories = [file for file in os.listdir(path) if os.path.isdir(os.path.join(path, file))]

    if directories:
        for directory in directories:
            read_files(os.path.join(path, directory))
    else:
        move_files(path)

def move_files(path):
    files = glob.glob(os.path.join(path, '*'))
    files = [f for f in files]
    print(f'path: {path}')

    for file in files:
        target_dir = os.path.join('./', path.split('_')[-1], os.path.split(path)[-1])
        os.makedirs(target_dir, exist_ok=True)

        src = file
        dst = os.path.join(target_dir, os.path.basename(file))
        print(f'src: {src}')
        print(f'dst: {dst}')
        os.rename(src, dst)

    print(f'completed: {path}')

root_path = './'

read_files(root_path)