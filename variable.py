import os
from PIL import ImageTk,Image
img_list=[]
img_files=('.jpeg','.jpg','.png','.gif')
for file in os.listdir():
	 if file.endswith(img_files):
	 	img_list.append(file)
	

title_height=26
frame_ratio=0.4
start_x=100
start_y=100
LGRAY="#3e4042"
DGRAY="#25292e"
RGRAY="#10121f"
rel=0.33
img_label=[]
top_margin=26
image_frame_ratio=3.25
