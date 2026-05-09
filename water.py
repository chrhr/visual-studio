from PyQt5.QtWidgets import *
import sys
import cv2 as cv
import numpy as np
import winsound
import os

class MINI_UI(QMainWindow):
    def __init__(self) :
        super().__init__()
        # 1. 창 제목 및 레이아웃 유지
        self.setWindowTitle('신호등 식별하기')
        self.setGeometry(200, 200, 900, 200)

        # 2. 버튼 명칭만 주제에 맞게 변경
        trafficLightButton=QPushButton('신호등 샘플 등록', self)
        roadButton=QPushButton('도로 영상 불러오기', self)
        recognitionButton=QPushButton('인식하기', self)
        quitButton=QPushButton('나가기', self)
        self.label=QLabel('안녕하세요', self)

        trafficLightButton.setGeometry(10, 10, 200, 30)
        roadButton.setGeometry(210, 10, 250, 30)
        recognitionButton.setGeometry(460, 10, 200, 30)
        quitButton.setGeometry(670, 10, 200, 30)
        self.label.setGeometry(10, 40, 1000, 170)

        trafficLightButton.clicked.connect(self.lightFunction)
        roadButton.clicked.connect(self.roadFunction)
        recognitionButton.clicked.connect(self.recognitionFunction)
        quitButton.clicked.connect(self.quitFunction)

        current_path = os.path.dirname(os.path.abspath(__file__))

        # 3. 신호등 종류별 파일 설정 (이미지 파일명이 일치해야 함)
        self.lightFiles = [
            [os.path.join(current_path, 'sign1.jpg'), '신호등1'],
            [os.path.join(current_path, 'sign2.png'), '신호등2'],
            [os.path.join(current_path, 'sign3.jpg'), '신호등3']
        ]
        self.lightImgs = []
        self.roadImg = None

    def lightFunction(self) :
        self.label.clear()
        self.label.setText('신호등 상태별 샘플을 등록함')
        self.lightImgs = [] # 리스트 초기화 추가

        for fname,_ in self.lightFiles:
            img = cv.imread(fname)
            if img is not None:
                self.lightImgs.append(img)
                cv.imshow(fname, self.lightImgs[-1])

    def roadFunction(self) :
        if self.lightImgs==[] :
            self.label.setText('신호등 샘플을 먼저 등록 바람')
        else :
            fname=QFileDialog.getOpenFileName(self, '파일 읽기', './')
            if fname[0]:
                self.roadImg=cv.imread(fname[0])
                if self.roadImg is None: sys.exit('파일을 찾을 수 없음')
                cv.imshow('Road scene', self.roadImg)

    def recognitionFunction(self) :
        if self.roadImg is None :
            self.label.setText('도로 영상을 먼저 입력 바람')
        else :
            sift=cv.SIFT_create()

            # 등록된 신호등 샘플 특징점 추출
            KD=[]
            for img in self.lightImgs:
                gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
                KD.append(sift.detectAndCompute(gray, None))
            
            # 현재 도로 영상 특징점 추출
            grayRoad=cv.cvtColor(self.roadImg,cv.COLOR_BGR2GRAY)
            road_kp, road_des=sift.detectAndCompute(grayRoad, None)

            matcher=cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)
            GM=[]

            for light_kp, light_des in KD :
                knn_match=matcher.knnMatch(light_des, road_des, 2)
                T = 0.7
                good_match=[]
                
                for nearest1, nearest2 in knn_match :
                    if (nearest1.distance/nearest2.distance)<T :
                        good_match.append(nearest1)
                GM.append(good_match)

            best=GM.index(max(GM, key=len))

            if len(GM[best])<20 :
                self.label.setText('인식 가능한 신호등이 없음')
            else :
                light_kp=KD[best][0]
                good_match=GM[best]

                points1=np.float32([light_kp[gm.queryIdx].pt for gm in good_match])
                points2=np.float32([road_kp[gm.trainIdx].pt for gm in good_match])

                # 호모그래피 및 RANSAC 적용
                H,_=cv.findHomography(points1, points2, cv.RANSAC)

                h1, w1 = self.lightImgs[best].shape[0], self.lightImgs[best].shape[1]
                h2, w2 = self.roadImg.shape[0], self.roadImg.shape[1]

                box1=np.float32([[0,0], [0,h1-1], [w1-1, h1-1], [w1-1, 0]]).reshape(4,1,2)
                box2=cv.perspectiveTransform(box1, H)
                
                self.roadImg=cv.polylines(self.roadImg,[np.int32(box2)], True, (0,255,0), 4)

                img_match=np.empty((max(h1, h2), w1+w2, 3), dtype=np.uint8)
                cv.drawMatches(self.lightImgs[best], light_kp, self.roadImg, road_kp, good_match, img_match,
                               flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
                cv.imshow('Matches and Homography', img_match)

                # 상태에 따른 메시지 출력
                status_msg = self.lightFiles[best][1]
                self.label.setText(f'현재 신호는 {status_msg}입니다. 신호에 따라 주행하세요.')
                winsound.Beep(2500, 500)

    def quitFunction(self) :
        cv.destroyAllWindows()
        self.close()

app=QApplication(sys.argv)
win=MINI_UI()
win.show()
app.exec_()