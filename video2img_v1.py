import cv2
import os

# 영상의 의미지를 연속적으로 캡쳐할 수 있게 하는 class
root_path = 'C:/Users/KimJunha/Desktop/vision nerf 베트남/input/D3/230724_camera(3)_출근'
path = os.path.join('D3_S20230724090001_E20230724092554.mp4')
# path = 'D3_S20230724090001_E20230724092554.mp4'
vidcap = cv2.VideoCapture(path)

count = 0

while (vidcap.isOpened()):
    # read()는 grab()와 retrieve() 두 함수를 한 함수로 불러옴
    # 두 함수를 동시에 불러오는 이유는 프레임이 존재하지 않을 때
    # grab() 함수를 이용하여 return false 혹은 NULL 값을 넘겨 주기 때문
    ret, image = vidcap.read()

    if (int(vidcap.get(1)) % 10 == 0):  # 초당 30프레임 정도이므로 7개 프레임마다 자름
        print('Saved frame number : ' + str(int(vidcap.get(1))))
        # save_path = os.path.join(root_path, f'images/{count:06d}.jpg')
        save_path = "images/%06.d.jpg" % count
        cv2.imwrite(save_path, image)
        print('Saved frame%d.jpg' % count)
        count += 1

vidcap.release()