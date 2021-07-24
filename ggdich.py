from googletrans import Translator
from tkinter import *
from PIL import Image,ImageTk


root = Tk()
root.title("Make by Hiesu")
root.geometry("900x300")
root.iconbitmap('images.ico')


loadbk = Image.open('black.jpg')
render = ImageTk.PhotoImage(loadbk)
img = Label(root,image=render)
img.place(x=0,y=0)



name = Label(root,text = "Google Translate" ,fg="#e6ffff", bg="#000000")
name.config(font=("Comic Sans MS",30))
name.place(x= 320,y= 5)
#Khai bao bat dau
ngonngu = "en"
ngonngu1 = "vi"
box = Text(root,width="38",height="7",font=("Time New Roman",13))
box.place(x = 15,y=125)
box1 = Text(root,width="38",height="7",font=("Time New Roman",13))
box1.place(x = 540,y = 125)





def clear():
	box.delete(1.0,END)
	box1.delete(1.0,END)
def trans():
	nhap = box.get(1.0,END)
	print(ngonngu)
	print(ngonngu1)
	try:
		translator = Translator()
		a = translator.translate(nhap,src=ngonngu,dest=ngonngu1)
		b=a.text
	except Exception as e:
		b=nhap
	
	box1.delete(1.0,END)
	box1.insert(END,b)
# def tran(event):
# 	nhap = box.get(1.0,END)	
# 	try:
# 		translator = Translator()
# 		a = translator.translate(nhap,src=ngonngu,dest=ngonngu1)
# 		b=a.text
# 	except Exception as e:
# 		b=nhap
	
# 	box1.delete(1.0,END)
# 	box1.insert(END,b)	


button = Frame(root).pack(side=BOTTOM)	
clear_button = Button(button,text="CLEAR", font=(("Time New Roman"),10,"bold"),bg="#303030",fg ="#ffffff",command = clear)
clear_button.place(x= 430 , y = 135)

trans_button = Button(button,text="ENTER", font=(("Time New Roman"),10,"bold"),bg="#303030",fg ="#ffffff",command = trans)
trans_button.place(x = 430 , y = 175)


vn_button = Button(button,text="VN", font=(("Time New Roman"),10,"bold"),bg="#303030",fg ="#ffffff" ) 
vn_button.place(x = 15, y = 99)
vn1_button = Button(button,text="VN", font=(("Time New Roman"),10,"bold"),bg="#303030",fg ="#ffffff") 
vn1_button.place(x = 540, y = 99)

eng_button = Button(button,text="ENG", font=(("Time New Roman"),10,"bold"),bg="#303030",fg ="#ffffff") 
eng_button.place(x = 50, y = 99)
eng1_button = Button(button,text="ENG", font=(("Time New Roman"),10,"bold"),bg="#303030",fg ="#ffffff" )
eng1_button.place(x = 575, y = 99)	


# root.bind('<Control_L>', tran)
# root.bind('<Control_R>', tran)
root.mainloop()