import cv2
import sys
#tar = 'datasets/JPEGImages/img_00100.png '

im = cv2.imread(sys.argv[1])
cascade = cv2.CascadeClassifier('result/cascade.xml')
faces = cascade.detectMultiScale(im, 1.1, 3)

for (x, y, w, h) in faces:
    cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),3)
    print  sys.argv[1]  +  " {0} {1} {2} {3}".format(x,y,w,h)

out_path = 'result_img/' + sys.argv[1].split("/")[-1]
print("make : " + out_path)
cv2.imwrite(out_path, im)
