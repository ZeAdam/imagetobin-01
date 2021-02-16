# imagetobin-01
![f.png](https://i.postimg.cc/6q0Pj22s/f.png)
A little Python program transforming an image into a 0 and 1 text file. 

## Requirements
- Python 3
- Opencv-python
- Pillow

## Setup and run
To use it, simply install "opencv-python" and "pillow" using Pip and open it:
```
pip install opencv-python
pip install Pillow
python3 img2bin.py
```
It will ask for the image's path and for scaling the output's width (default: 500):
```
Image file name: image.jpg
Width: 500
You can now find the output in "out.bin" folder.
```
**Note**: no need to have `img2bin.py` in order to use `img2bin_tk.py`.
