"""
从视频中选取多个的ROI
功能：
r：进入选取ROI模式，选取ROI模式内
    - （1）唯一退出方法：0.5秒以内按q快速退出（本程序还不能任意时刻按q都能退出）
    - （2）开始选取ROI：等待0.5秒以上或者按其它键，使用鼠标点击移动可以选取ROI

l: 加载可能的ROI文件
s：保存当前矩形框为 rois.pkl
p: 删除最后一个ROI
q：退出

Author：QiangZiBro
Github：https://github.com/QiangZiBro
EMAIL：qiangzibro@gmail.com
"""
import os
import cv2
import pickle


class ROISelector(object):
    def __init__(self, camera=cv2.VideoCapture(0)):
        self.camera = camera
        self.ROIs = []
        self.update()

    def update(self):
        while True:
            if self.camera.isOpened():
                (self.status, self.frame) = self.camera.read()
                self._draw_ROIs()
                cv2.imshow('image', self.frame)

                key = cv2.waitKey(2)
                if key == ord('r'):
                    self._select_roi()
                if key == ord('q'):
                    break
                elif key == ord('p'):
                    self.ROIs.pop()
                elif key == ord('l'):
                    self._load_roi_as_pkl()
                elif key == ord('s'):
                    self._save_roi_as_pkl()


    def _select_roi(self):
        while True:
            key = cv2.waitKey(500)
            if key == ord('q'):
                break
            ROI = cv2.selectROI("image", self.frame, showCrosshair=False, fromCenter=False)
            self.ROIs.append(ROI)
            self._draw_ROIs()
            cv2.imshow('image', self.frame)

    def _draw_ROIs(self):
        if self.ROIs:
            for ROI in self.ROIs:
                x, y, w, h = ROI
                cv2.rectangle(self.frame, (x, y), (x + w, y + h), color=(255, 255, 0), thickness=2)

    def _save_roi_as_pkl(self, name="rois.pkl"):
        with open(name, "wb") as f:
            pickle.dump(self.ROIs, f)

    def _load_roi_as_pkl(self, name="rois.pkl"):
        if os.path.exists(name):
            with open(name, "rb") as f:
                self.ROIs = pickle.load(f)


if __name__ == '__main__':
    static_ROI = ROISelector()
    cv2.destroyAllWindows()