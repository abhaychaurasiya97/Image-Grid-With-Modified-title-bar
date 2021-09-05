from variable import *
from tkinter import *
import sys
from PIL import ImageTk,Image

def create_window(root):
	root.overrideredirect(True)
	root.geometry(f"{int(root.winfo_screenwidth()*frame_ratio)}x{int(root.winfo_screenheight()*frame_ratio)}+{start_x}+{start_x}")
	root.config(bg=DGRAY)
	
	
	root.maximized=False

	def maximize_window():
		for img in img_label:
			img.place_forget()
		img_label.clear()
		
		if root.maximized==False:
			
			root.normal_size=root.geometry()
			expand_button.config(text='  □  ')
			
			#this line is written for showing the taskbar of linux
			
			if sys.platform=='linux': 
				root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+25")
			root.maximized=not root.maximized
			k=0
			for i in range(3):
				for j in range(3):
					width=int(root.winfo_screenwidth()/image_frame_ratio)
					height=int(root.winfo_screenheight()/image_frame_ratio)
					x=i*width+2*i
					y=j*height+top_margin+2*j
					img=ImageTk.PhotoImage(Image.open(img_list[k]).resize((width,height)))
					a=Label(image=img)
					a.place(x=x,y=y,width=width,height=height)
					img_label.append(a)
					k+=1
			
		else:	
			k=0
			root.geometry(root.normal_size)
			root.maximized=not root.maximized
			for i in range(3):
				for j in range(3):
					width=int(root.winfo_screenwidth()*frame_ratio/image_frame_ratio)
					height=int(root.winfo_screenheight()*frame_ratio/image_frame_ratio)
					x=i*width+2*i
					y=j*height+top_margin+2*j
					img=ImageTk.PhotoImage(Image.open(img_list[k]).resize((width,height)))
					a=Label(image=img)
					a.place(x=x,y=y,width=width,height=height)
					img_label.append(a)
					k+=1
	title_bar=Frame(root,bd=0,bg=RGRAY,relief='raised')
	title_bar.pack(fill=X,side='top')
	close_button=Button(title_bar,text='  x  ',command=root.quit,bg=RGRAY,padx=2,pady=2,font=('calibri',13),bd=0,fg='white',highlightthickness=0)
	expand_button=Button(title_bar,text='  □  ',command=maximize_window,bg=RGRAY,padx=2,pady=2,font=('calibri',13),bd=0,fg='white',highlightthickness=0)
	
	title=Label(title_bar,text=' Project ',bg=RGRAY,padx=2,pady=2,font=('helvetica',13),fg='white',highlightthickness=0)
	
	close_button.pack(side="right")
	expand_button.pack(side="right")
	title.pack(side="left")
	k=0
	for i in range(3):
		for j in range(3):
			width=int((root.winfo_screenwidth()*frame_ratio)/image_frame_ratio)
			height=int((root.winfo_screenheight()*frame_ratio)/image_frame_ratio)
			x=i*width+2*i
			y=j*height+top_margin+2*j
			img=ImageTk.PhotoImage(Image.open(img_list[k]).resize((width,height)))
			a=Label(image=img)
			a.place(x=x,y=y,width=width,height=height)
			img_label.append(a)
			k+=1
			

			
