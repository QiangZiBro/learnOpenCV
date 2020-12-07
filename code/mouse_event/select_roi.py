# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：learnOpenCV -> select_roi
@IDE    ：PyCharm
@Author ：QiangZiBro
@Date   ：2020/12/6 8:54 下午
@Desc   ：
=================================================='''
import cv2

if __name__ == '__main__' :
    im = cv2.imread("image.jpg")

    # 从一张图片选取若干ROI
    rects = []
    fromCenter = False
    # 是否显示网格
    showCrosshair = False
    # 如果为Ture的话 , 则鼠标的其实位置就作为了roi的中心
    # False: 从左上角到右下角选中区域
    ROI = cv2.selectROI("Image", im, showCrosshair, fromCenter)
    print(ROI)
    # 画出ROI
    (x, y, w, h) = ROI
    cv2.rectangle(im, (x,y), (x+w, y+h), color=(255, 255, 0), thickness=2)

    # Display cropped image
    cv2.imshow("Result image", im)
    cv2.waitKey(0)
