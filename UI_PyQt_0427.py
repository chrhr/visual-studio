from PyQt5.QtWidgets import *
import sys
import cv2 as cv
import numpy as np
import winsound
import os

class MINI_UI(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.setWindowTitle('표지판 식별하기')
        self.setGeometry(200, 200, 900, 200)

        signButton=QPushButton('표지판 등록', self)
        roadButton=QPushButton('도로 영상 불러오기', self)
        recognitionButton=QPushButton('인식하기', self)
        quitButton=QPushButton('나가기', self)
        self.label=QLabel('안녕하세요', self)

        signButton.setGeometry(10, 10, 200, 30)
        roadButton.setGeometry(210, 10, 250, 30)
        recognitionButton.setGeometry(460, 10, 200, 30)
        quitButton.setGeometry(670, 10, 200, 30)
        self.label.setGeometry(10, 40, 1000, 170)

        signButton.clicked.connect(self.signFunction)
        roadButton.clicked.connect(self.roadFunction)
        recognitionButton.clicked.connect(self.recognitionFunction)
        quitButton.clicked.connect(self.quitFunction)

        current_path = os.path.dirname(os.path.abspath(__file__))

        self.signFiles = [
            [os.path.join(current_path, 'child.jpg'), '어린이'],
            [os.path.join(current_path, 'elder.png'), '노인'],
            [os.path.join(current_path, 'disabled.jpg'), '장애인']
        ]
        self.signImgs = []
        self.roadImg = None

    def signFunction(self) :
        self.label.clear()
        self.label.setText('교통약자 표지판을 등록함')

        for fname,_ in self.signFiles:
            self.signImgs.append(cv.imread(fname))
            cv.imshow(fname,self.signImgs[-1])

    def roadFunction(self) :
        if self.signImgs==[] :
            self.label.setText('표지판을 먼저 등록 바람')
        
        else :
            fname=QFileDialog.getOpenFileName(self, '파일 읽기', './')
            self.roadImg=cv.imread(fname[0])
            if self.roadImg is None: sys.exit('파일을 찾을 수 없음')

            cv.imshow('Road scene', self.roadImg)

    def recognitionFunction(self) :
        if self.roadImg is None :
            self.label.setText('도로 영상을 먼저 입력 바람')
        
        else :
            sift=cv.SIFT_create()

            KD=[]
            for img in self.signImgs:
                gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
                KD.append(sift.detectAndCompute(gray, None))
            
            grayRoad=cv.cvtColor(self.roadImg,cv.COLOR_BGR2GRAY)
            road_kp,road_des=sift.detectAndCompute(grayRoad, None)

            matcher=cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)
            GM=[]

            for sign_kp, sign_des in KD :
                knn_match=matcher.knnMatch(sign_des, road_des, 2)
                T = 0.7
                good_match=[]
                
                for nearest1, nearest2 in knn_match :
                    if (nearest1.distance/nearest2.distance)<T :
                        good_match.append(nearest1)
                GM.append(good_match)

            best=GM.index(max(GM, key=len))

            if len(GM[best])<10 :
                self.label.setText('표지판이 없음')
            else :
                sign_kp=KD[best][0]
                good_match=GM[best]

                points1=np.float32([sign_kp[gm.queryIdx].pt for gm in good_match])
                points2=np.float32([road_kp[gm.trainIdx].pt for gm in good_match])

                H,_=cv.findHomography(points1, points2, cv.RANSAC)

                h1, w1 = self.signImgs[best].shape[0], self.signImgs[best].shape[1]

                h2, w2 = self.roadImg.shape[0],self.roadImg.shape[1]

                box1=np.float32([[0,0], [0,h1-1], [w1-1, h1-1], [w1-1, 0]]).reshape(4,1,2)
                box2=cv.perspectiveTransform(box1, H)
                
                self.roadImg=cv.polylines(self.roadImg,[np.int32(box2)], True, (0,255,0), 4)

                img_match=np.empty((max(h1, h2), w1+w2, 3), dtype=np.uint8)
                cv.drawMatches(self.signImgs[best], sign_kp, self.roadImg, road_kp, good_match, img_match,
                               flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
                cv.imshow('Matches and Homography', img_match)

                self.label.setText(self.signFiles[best][1]+ '보호구역입니다. 30km로 서행하세요.')
                winsound.Beep(3000, 500)

    def quitFunction(self) :
        cv.destroyAllWindows()
        self.close()

app=QApplication(sys.argv)
win=MINI_UI()
win.show()
app.exec_()