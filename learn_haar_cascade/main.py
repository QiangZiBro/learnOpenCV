import cv2
import numpy as np

haar_front_face_xml = './data/haarcascade_frontalface_default.xml'
haar_eye_xml = './data/haarcascade_eye.xml'


# 1.静态图像中的人脸检测
def StaticDetect(filename):
    # 创建一个级联分类器 加载一个 .xml 分类器文件. 它既可以是Haar特征也可以是LBP特征的分类器.
    face_cascade = cv2.CascadeClassifier(haar_front_face_xml)

    # 加载图像
    img = cv2.imread(filename)
    # 转换为灰度图
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 进行人脸检测，传入scaleFactor，minNegihbors，分别表示人脸检测过程中每次迭代时图像的压缩率以及
    # 每个人脸矩形保留近似数目的最小值
    # 返回人脸矩形数组
    faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)
    for (x, y, w, h) in faces:
        # 在原图像上绘制矩形
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.namedWindow('Face Detected！')
    cv2.imshow('Face Detected！', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 2、视频中的人脸检测
def DynamicDetect():
    '''
    打开摄像头，读取帧，检测帧中的人脸，扫描检测到的人脸中的眼睛，对人脸绘制蓝色的矩形框，对人眼绘制绿色的矩形框
    '''
    # 创建一个级联分类器 加载一个 .xml 分类器文件. 它既可以是Haar特征也可以是LBP特征的分类器.
    face_cascade = cv2.CascadeClassifier(haar_front_face_xml)
    eye_cascade = cv2.CascadeClassifier(haar_eye_xml)

    # 打开摄像头
    camera = cv2.VideoCapture(0)
    cv2.namedWindow('Dynamic')

    while True:
        # 读取一帧图像
        ret, frame = camera.read()
        # 判断图片读取成功？
        if ret:
            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 人脸检测
            faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)
            for (x, y, w, h) in faces:
                # 在原图像上绘制矩形
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                roi_gray = gray_img[y:y + h, x:x + w]
                # 眼睛检测
                eyes = eye_cascade.detectMultiScale(roi_gray, 1.03, 5, 0, (40, 40))
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(frame, (ex + x, ey + y), (x + ex + ew, y + ey + eh), (0, 255, 0), 2)

            cv2.imshow('Dynamic', frame)
            # 如果按下q键则退出
            if cv2.waitKey(100) & 0xff == ord('q'):
                break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    #filename = 'test1.jpg'
    #StaticDetect(filename)
    DynamicDetect()
