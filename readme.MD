<h1 align="center">Image Comparer</h1>
<h2>What is Image Comparer?</h2>
<p>Image Comparer is a code that will take two images that you give it, get all the pixels, then get the rgb color for 
every pixel. After it has done that it will compare every pixel. If it finds that the pixel is not the same it will
color that one pixel completely red it will then save the new images to files
<br><br>
first image
<br>
<img src="test1.png">
<br>
second image
<br>
<img src="test2.png">
<br>
results
<br>
<img src="img1.png">
<br>
the pixels surrounding the letters have turned red because they are different in the two images
</p>
<h2>How to download</h2>
<p>1: make sure you have python installed
<br>
windows
</p>

`python --version`
<p> linux / mac</p>

`python3 --version`
<p>2: install packages
<br>
windows
</p>

`pip install pillow`

linux / mac

```
sudo apt update 
sudo apt install python3-tk
sudo apt install python3-pil
sudo apt-get -y install python3-pil.imagetk
```