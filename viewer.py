from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hi')
root.iconbitmap('/Users/Casa/desktop/PythonCourse/apple.icns')

#define image and then put in variable
my_img1 = ImageTk.PhotoImage(Image.open("images/redaustralianshep.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/redhusky.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/rednewfoundland.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/greatpyr.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/redgsd.jpg"))


#put images into python list
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]


status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

#put image in something else
my_label = Label(image=my_img1)
#put something else on the screen for STARTING IMAGE
my_label.grid(row=0, column=0,columnspan=3)



def forward(image_number):
	global my_label
	global button_forward
	global button_back

	#take image that is already there and get rid of it
	my_label.grid_forget()
	#redefine label and reference the next item on the list
	my_label = Label(image=image_list[image_number-1])
	#update buttons
	button_forward = Button(root, text=">>",command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))

	if image_number == len(image_list):
		button_forward = Button(root,text=">>",state=DISABLED)

	#put on the screen
	my_label.grid(row=0, column=0,columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)
	
	#put status on screen and update
	status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
	status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>",command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))

	if image_number == 1:
		button_back = Button(root,text="<<",state=DISABLED)

	#put on the screen
	my_label.grid(row=0, column=0,columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)

	#put status on screen and update
	status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
	status.grid(row=2, column=0, columnspan=3, sticky=W+E)


#back button
button_back = Button(root, text="<<", command=back, state=DISABLED)
#forward button
button_forward = Button(root, text=">>", command=lambda: forward(2))
#exit button
button_exit = Button(root, text="Exit Program", command=root.quit)


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()

