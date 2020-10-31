#import imutils
#import cv2
#redLower = (157, 93, 203)
#redUpper = (179, 255, 255)
#camera = cv2.Video

#facedrecogintion
import cv2, numpy, os

alg = 'haarcascade_frontalface_default.xml'
haar = cv2.CascadeClassifier(alg)
dataset = 'dataset'
(images, labels, names, id) = ([], [], {}, 0)

for (subdirs, dirs, files) in os.walk(dataset):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(dataset, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            label = id
            images.append(cv2.imread(path, 0))
            labels.append(int(label))
            #print(labels)
        id += 1

(width, height) = (130, 100)

(images, labels) = [numpy.array(lis) for lis in [images, labels]]
#print(images, labels)
#model = cv2.face.FisherFaceRecognizer_create()
model = cv2.face.LBPHFaceRecognizer_create()

model.train(images, labels)

print("Training Completed")


cam = cv2.VideoCapture(0)
cnt = 0
while True:
    (_,img) = cam.read()
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = haar.detectMultiScale(grayImg, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        onlyFace = grayImg[y:y+h, x:x+w]
        face_resize = cv2.resize(onlyFace, (width, height))
        prediction = model.predict(face_resize)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if prediction[1]<800:
            cv2.putText(img, '%s - %.0f' % (names[prediction[0]], prediction[1]), (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255))
            print(names[prediction[0]])
            cnt = 0
        else:
            cnt += 1
            cv2.putText(img, 'Unknown', (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
            if(cnt>100):
                print("Unknown Person")
                cv2.imwrite("input.jpg", img)
                cnt = 0
        cv2.imshow('OpenCV', img)
        key = cv2.waitKey(10)
        if key == 27:
            break

cam.release()
cv2.destroyAllWindows()
