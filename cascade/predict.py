#
# for fn in `find input_dir/`
#   do python $fn out_dir
# done
#
#
# http://shkh.hatenablog.com/entry/2012/11/03/052251
import cv2
import sys

if len(sys.argv) != 3:
    print("argument error")
    print("Usage : python predict.py (input image path) (output dir)")
    sys.exit(1)

model = 'model/cascade.xml'
in_image_path = sys.argv[1]
out_image_dir = sys.argv[2]

im = cv2.imread(in_image_path)
cascade = cv2.CascadeClassifier(model)
faces = cascade.detectMultiScale(im, 1.1, 3)

for (x, y, w, h) in faces:
    cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),3)
    print  sys.argv[1]  +  " {0} {1} {2} {3}".format(x,y,w,h)

out_path = out_image_dir + '/' + sys.argv[1].split("/")[-1]
print("make : " + out_path)
cv2.imwrite(out_path, im)
