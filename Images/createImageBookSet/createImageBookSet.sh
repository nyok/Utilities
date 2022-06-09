#!/bin/bash

let IMG_WIDTH=480
let IMG_HEIGHT=720
let TRANS=210

let CROP_WIDHT=160
let CROP_INDENT=IMG_WIDTH-CROP_WIDHT # 480-160=320

FILES=(1 2 3)


for i in ${FILES[@]};
do
	convert ./pages/page$i.jpg \
	-matte \
	-virtual-pixel transparent \
	-distort Perspective \
	"0,0 0,$TRANS 0,$IMG_HEIGHT 0,$IMG_HEIGHT $IMG_WIDTH,$IMG_HEIGHT $IMG_WIDTH,$IMG_HEIGHT $IMG_WIDTH,0 $IMG_WIDTH,0" \
	-crop $CROP_WIDHT'x'$IMG_HEIGHT'+'$CROP_INDENT'+0' \
	./pages_out/page_out_$i.png;
done

convert +append ./pages/cover.jpg $(for i in ${FILES[@]}; do echo "./pages_out/page_out_$i.png";done) -resize 'x'$IMG_HEIGHT ./result/conbined.png