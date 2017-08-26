# -*- coding: utf-8 -*-
import numpy as np
import cv2
import sys

# 回転させたい角度（正の値は反時計回り）
degree = 18

def rotate_reverse(in_image_path, out_image_dir):
    
    # 回転させたい角度（正の値は反時計回り）
    angle = degree * 1.0

    # 画像読み込み(alphaチャンネル有り)
    src_mat = cv2.imread(in_image_path, cv2.IMREAD_UNCHANGED)

    # 画像サイズの取得(横, 縦)
    size = tuple([src_mat.shape[1], src_mat.shape[0]])

    # dst 画像用意
    dst_mat = np.zeros(( size[1], size[0], 4), np.uint8)

    # 画像の中心位置(x, y)
    center = tuple([int(size[0]/2), int(size[1]/2)])


    # 回転変換行列の算出
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)

    # アフィン変換
    img_dst = cv2.warpAffine(src_mat, rotation_matrix, size, dst_mat,
                             flags=cv2.INTER_LINEAR,
                             borderMode=cv2.BORDER_CONSTANT)

    # 出力画像ファイル名生成
    tokens = in_image_path.split("/")
    out_image_path = out_image_dir + "/" + "o_" + tokens[-1]
    print(in_image_path + " -> " + out_image_path)

    # 書き出し
    cv2.imwrite(out_image_path, img_dst)

    return out_image_path


if len(sys.argv) != 3:
    print("argument error")
    print("Usage : python rotate_reverse.py (input image path) (out dir)")
    sys.exit(1)

in_image_path = sys.argv[1]
out_image_dir = sys.argv[2]

out_image_path = rotate_reverse(in_image_path, out_image_dir)

