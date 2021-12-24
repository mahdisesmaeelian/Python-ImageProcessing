## Sudoku detector using opencv 

◾Using GaussianBlur for decrease noises

◾Adaptive threshold to obtain binary image

◾Find contours and filter for largest contour

◾Find shape with 4 points by approxPolyDP

◾Draw contours around the sudoku table 

◾Crop the table and save it as a jpg image




```shell
cd <ByteTrack_HOME>
python3 tools/track.py -f exps/example/mot/yolox_x_mix_mot20_ch.py -c pretrained/bytetrack_x_mot20.pth.tar -b 1 -d 1 --fp16 --fuse --match_thresh 0.7 --mot20
python3 tools/interpolation.py
```
