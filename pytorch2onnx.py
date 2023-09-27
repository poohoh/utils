import argparse
import os
import sys

import torch.onnx

from inception import inception_v3

classes = {0: 'fire', 1: 'nonfire'}

def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--pt_path', type=str, default='checkpoint')
    parser.add_argument('--image_path', type=str, default='test_image')
    parser.add_argument('--alarm_path', type=str, default='test_alarm')
    parser.add_argument('--frame_width', type=int, default=1280)
    parser.add_argument('--frame_height', type=int, default=720)
    parser.add_argument('--stepSize', type=int, default=112)
    parser.add_argument('--windowSize', type=int, default=224)
    parser.add_argument('--batchSize', type=int, default=64)
    parser.add_argument('--model_Epoch', type=int, default=45)
    parser.add_argument('--model_lr', type=float, default=0.001)  # learning rate

    return parser.parse_args(argv)

if __name__=='__main__':
    args = parse_arguments(sys.argv[1:])

    if not os.path.exists(args.pt_path):
        os.mkdir(args.pt_path)
    if not os.path.exists(args.image_path):
        os.mkdir(args.image_path)
    if not os.path.exists(args.alarm_path):
        os.mkdir(args.alarm_path)


    # 모델 생성
    net = inception_v3(pretrained=0, num_classes=len(classes))
    net.cuda()

    print("===> Resuming from checkpoint.")
    checkpoint = torch.load("checkpoint/45.pt")
    net.load_state_dict(checkpoint)

    # 모델을 추론 모드로 전환합니다
    net.eval()

    # 모델에 대한 입력값
    batch_size = 1
    x = torch.randn(batch_size, 3, 224, 224, requires_grad=True)
    device = torch.device('cuda:0')
    x = x.to(device)
    torch_out = net(x)

    # 모델 변환
    torch.onnx.export(net,  # 실행될 모델
                      x,  # 모델 입력값 (튜플 또는 여러 입력값들도 가능)
                      "checkpoint/45.onnx",  # 모델 저장 경로 (파일 또는 파일과 유사한 객체 모두 가능)
                      export_params=True,  # 모델 파일 안에 학습된 모델 가중치를 저장할지의 여부
                      opset_version=10,  # 모델을 변환할 때 사용할 ONNX 버전
                      do_constant_folding=True,  # 최적화시 상수폴딩을 사용할지의 여부
                      input_names=['input'],  # 모델의 입력값을 가리키는 이름
                      output_names=['output'],  # 모델의 출력값을 가리키는 이름
                      dynamic_axes={'input': {0: 'batch_size'},  # 가변적인 길이를 가진 차원
                                    'output': {0: 'batch_size'}},
                      verbose=True) # export 과정 출력
