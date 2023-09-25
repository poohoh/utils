# path의 파일 확장자 일괄 변경
import os

path = './compact'
files = os.listdir(path)
for name in files:
    if not os.path.isdir(name):
        src = os.path.splitext(name)
        os.rename(os.path.join(path, name), os.path.join(path, src[0] + '.png'))
