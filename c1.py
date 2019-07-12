#import tkintter
from tkinter import *
from tkinter.font import Font
#Create window
root = Tk()

#window title
root.title("Pacific College Of Engineering Attendance System")

#Create topframe with top side
topframe=Frame(root)
#create coustom font for my company
my_font=Font(family="Times New Roman",size=30,weight="bold",slant="italic")
#create label on root window
label=Label(topframe,text="Pacific College Of Engineering Attendance System",font=my_font,foreground="#283142")
label.pack()
#pack topframe on top side
topframe.pack(side=TOP)

#Create bottomframe with bottom side
bottomframe=Frame(root)

#Create leftframe in bottomframe with  left side
leftframe=Frame(bottomframe,bg='black')


#create a canvas for image on leftframe
canvas=Canvas(leftframe,width=1200,height=650)
canvas.pack()

#photo for canvas with photo path
photo=PhotoImage(file='/home/prem/Desktop/college/latest.png')
#create position of canvas and image start at NW
canvas.create_image(0,0,image=photo,anchor=NW)

leftframe.pack(side=LEFT)


#Create rightframe in bottomframe with right side
rightframe=Frame(bottomframe,padx=50)

#create all image path for buttons and checkbox images
photo1=PhotoImage(file='//home//prem//Desktop//college//add.png')
photo2=PhotoImage(file='/home/prem/Desktop/college/start.png')
photo3=PhotoImage(file='/home/prem/Desktop/college/stop.png')
photo4=PhotoImage(file='/home/prem/Desktop/college/file.png')
photo5=PhotoImage(file='/home/prem/Desktop/college/exit.png')
#photo6=PhotoImage(file='/home/prem/Desktop/college/.png')
#photo7=PhotoImage(file='/home/prem/Desktop/college/latest6.png')

#button bt1 for add new entry
Bt1=Button(rightframe,text="New Entry",image=photo1,activebackground="green", bd=0,width=10)
Bt1.pack(fill=X)

#button bt2 for start webcam
Bt2=Button(rightframe,text="Start",image=photo2,activebackground="green", bd=0)
Bt2.pack(fill=X,pady=10)

##button bt3 for stop camera
Bt3=Button(rightframe,text="Stop(Press'Q')",image=photo3,activebackground="green", bd=0)
Bt3.pack(fill=X,pady=10)

##button bt4 for seen files
Bt4=Button(rightframe,text="files",width=10,image=photo4,activebackground="green", bd=0)
Bt4.pack(fill=X,pady=10)
 
##button bt5 for Exit programme
Bt5=Button(rightframe,text="EXIT",image=photo5,activebackground="green", bd=0)
Bt5.pack(fill=X,pady=10)
'''
#check_bt for set time period in minutes
h=StringVar()
check_bt=Checkbutton(rightframe,text="Set Time",variable=h, offvalue="uncheck",onvalue="check",activeforeground="green",width=120,image=photo6,compound=TOP)
check_bt.pack(side=LEFT)

#check_bt2 for upload images if person(student notpresent ) or offline making data 
M=StringVar()
check_bt2=Checkbutton(rightframe,text="Upload Image",variable=M, offvalue="uncheck",onvalue="check",activeforeground="green",width=120,image=photo7,compound=TOP)
check_bt2.pack(side=LEFT)


'''

rightframe.pack(side=RIGHT)
bottomframe.pack()
#Set window geometry width 1210 and height 750 and open position on screen left to 150 and top to 150
root.geometry("1210x750+150+150")
#stable main window on infinity time
root.mainloop()

