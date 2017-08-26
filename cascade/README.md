
 opencv_createsamples -info info.dat -vec kawaii.vec -num 199

 opencv_traincascade -data result/ -vec kawaii.vec -bg bg.txt -numPos 172 -numNeg 27 -featureType HAAR -mode ALL

