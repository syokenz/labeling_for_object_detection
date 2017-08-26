## OpenCV付属のカスケード分類で手牌の位置をあてる　

参考  http://shkh.hatenablog.com/entry/2012/11/03/052251

### 入力のテキストファイルから学習セットを作る

```
opencv_createsamples -info info.dat -vec kawaii.vec -num 199
```

199は画像の総数

出力はkawaii.vec

### 学習する

```
opencv_traincascade -data model/ -vec kawaii.vec -bg bg.txt -numPos 172 -numNeg 27 -featureType HAAR -mode ALL
```

- info.datは物体がある場合(ポジティブ)の学習データ
- bg.txtは物体がない場合(ネガティブ)の学習データ
- numPosは物体がある場合の数
