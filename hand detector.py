# ================================== dependencies =================================================
import cv2
import mediapipe as mp
import time

class All(): 

    def __init__(self):
        # mediapipe variables
        mpDraw = mp.solutions.drawing_utils
        mpPose = mp.solutions.pose
        pose = mpPose.Pose(enable_segmentation=True)
        
        self.mpDraw = mpDraw        
        self.mpPose = mpPose
        self.pose = pose
        
        # local variables
        landmarklist = []
        pTime = 0

        self.landmarklist = landmarklist
        self.pTime = pTime

    # ========================== finding landmarks position ===============================
    def find_position(self, img, draw=False):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape

                cx, cy = int(lm.x * w), int(lm.y * h)
                self.landmarklist.append([id, cx, cy])

                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

        return self.landmarklist

# ============================== finding pose using landmarks =============================
    def find_pose(self, img, draw=False):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    
    def destroy(self):
            cv2.destroyAllWindows()
            for _ in range (1,5):
                cv2.waitKey(1)
            return

    def start(self):    
        # =================================== infinite while loop ===================================
        while True:
            cap = cv2.VideoCapture(0)
            success, img = cap.read()

        # ======================================= fps =========================================
            cTime = time.time()
            fps = 1 / (cTime - self.pTime)
            self.pTime = cTime
            cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

            self.find_position(img, True)

            cv2.imshow("img", img)
            cv2.waitKey(1)
        return