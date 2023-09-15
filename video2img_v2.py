# import cv2
# import os

# video_path = '230719_camera(1)_7-8'
# video_dir = 'D1_S20230719090001_E20230719091810.mp4'
# video_name = os.path.split(os.path.splitext(video_dir)[0])[1]

# # 영상의 이미지를 연속적으로 캡쳐할 수 있게 하는 class
# vidcap = cv2.VideoCapture(os.path.join(video_path, video_dir))

# os.makedirs('output', exist_ok=True)

# count = 0

# while (vidcap.isOpened()):
#     # read()는 grab()와 retrieve() 두 함수를 한 함수로 불러옴
#     # 두 함수를 동시에 불러오는 이유는 프레임이 존재하지 않을 때
#     # grab() 함수를 이용하여 return false 혹은 NULL 값을 넘겨 주기 때문
#     ret, image = vidcap.read()

#     if (int(vidcap.get(1)) % 7 == 0):  # 초당 30프레임 정도이므로 7개 프레임마다 자름
#         print('Saved frame number : ' + str(int(vidcap.get(1))))
#         cv2.imwrite(f"output/{video_name}_{count:06d}.jpg", image)
#         print(f'Saved frame{count:06d}.jpg')
#         count += 1

# vidcap.release()

import cv2
import numpy as np
import os
from tqdm import tqdm



def read_files(path):
    video_to_image(path)

    directories = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

    if directories:
        for directory in directories:
            read_files(os.path.join(path, directory))

def video_to_image(path):
    videos = [f for f in os.listdir(path) if f.endswith('.mp4')]

    if not videos:
        return

    for video_name in videos:
        # 비디오 파일 열기
        cap = cv2.VideoCapture(os.path.join(path, video_name))

        name_no_ext = os.path.splitext(video_name)[0]

        # # OpenCV DNN 모듈에 GPU를 사용하도록 설정
        # cv2.cuda.setDevice(0)_출근

        out_path = os.path.join(path, f'{name_no_ext}_frames')
        os.makedirs(out_path, exist_ok=True)
        print('output path : ' + out_path)

        frame_count = 0
        saved_count = 0

        if not cap.isOpened():
            print(f'Video open failed!: {video_name}')
            return
        else:
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

            for _ in tqdm(range(total_frames)):
                ret, frame = cap.read()
                if not ret:
                    break

                if (frame_count % 10 == 0):  # 10프레임마다 자름
                    # frame을 이미지 파일로 저장
                    save_path = os.path.join(out_path, f'{saved_count:06d}.png')
                    cv2.imwrite(save_path, frame)
                    saved_count += 1
                
                frame_count += 1
            
            cap.release()

        # while(cap.isOpened()):
        #     ret, frame = cap.read()
        #     if ret == False:
        #         break

        #     if (frame_count % 10 == 0):  # 10프레임마다 자름
        #         # # frame을 GPU 메모리로 전송
        #         # gpu_frame = cv2.cuda_GpuMat()
        #         # gpu_frame.upload(frame)

        #         # 프레임을 이미지 파일로 저장
        #         save_path = os.path.join(out_path, f'{saved_count:06d}.png')
        #         cv2.imwrite(save_path, frame)

        #         print(f'Image Saved: {save_path}')
        #         saved_count += 1

        #     frame_count += 1

        # cap.release()

################ 사용시 수정 부분 ##################

root_path = 'C:\\Users\\KimJunha\\Desktop\\vision nerf vietnam\\input\\videos'  # 경로에 한글 있으면 안 됨.

###################################################

read_files(root_path)