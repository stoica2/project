import os, matplotlib.pyplot as plt, time, numpy as np, pandas as pd
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import *
import csv
import pandas as pd

# creates the GUI canvas
def main():
	global row
	row = [0]
	# open('projecttest.csv', 'w+')
	# df = pd.read_csv('projecttest.csv')
	root = tk.Tk()
	root.title("Mood Tracker")
	root.geometry('600x600')
	root.configure(bg = "gray70")
	GUI(root)
	root.mainloop()

# creates main screen and buttons for two main options.
def GUI(root):
#starting text
	open_text1 = tk.Label(root, justify=tk.CENTER, text="Welcome to the Mood Tracker!", 
								font="Helvetica 25 bold", bg = "gray70", fg = "darkorchid3")
	open_text1.place(x=300, y=150, anchor=tk.CENTER)
	open_text2 = tk.Label(root, justify=tk.CENTER, text="Select one of the options below to get started.", 
								font="Helvetica 15", bg = "gray70")
	open_text2.place(x=300, y=200, anchor=tk.CENTER)
#buttons
	input_button = tk.Button(root, text="Input Data", bd='5', font="Helvetica 15", 
								activebackground="darkorchid3", activeforeground= "white", 
								command= lambda: input_data1(root, open_text1, open_text2, input_button, view_button))
	input_button.place(x=150, y=450, anchor=tk.CENTER)
	view_button = tk.Button(root, text="View Data", bd='5', font="Helvetica 15", 
								activebackground="darkorchid3", activeforeground= "white", 
								command= lambda: view_data(root, open_text1, open_text2, input_button, view_button))
	view_button.place(x=450, y =450, anchor=tk.CENTER)

# screen for inputting the date, includes a next button
def input_data1(root, open_text1, open_text2, input_button, view_button):
	open_text1.destroy()
	open_text2.destroy()
	input_button.destroy()
	view_button.destroy()
	text1 = tk.Label(root, justify=tk.CENTER, text="Please input today's date.", 
						font="Helvetica 15", bg = "gray70")
	text1.place(x=300, y=150, anchor=tk.CENTER)
#input date
	def get_date():
		date = cal.get_date()
		print(date)
		# date_label.config(text=f"Selected Date: {date}")
		return date
	cal = DateEntry(root, width=12, background="darkorchid3", foreground="white", borderwidth=2)
	cal.pack(padx=10, pady=180)
#save date
	def save(date1):
		with open(r"mood_data.csv", 'a') as file:
			global row
			date = date1.strftime("%m/%d/%y")
			print(date)
			row[0] = (date)
			# file.write(date + '\n')
#buttons
	next_button = tk.Button(root, text="Next", bd='5', font="Helvetica 15", activebackground="darkorchid3", activeforeground= "white", 
								command= lambda: (save(get_date()), input_data2(root, text1, next_button, cal)))
	next_button.place(x=550, y =550, anchor=tk.CENTER)

# screen for inputting emotion data, includes a save and back button
def input_data2(root, text1, next_button, cal):
	text1.destroy()
	next_button.destroy()
	cal.destroy()
	text2 = tk.Label(root, justify=tk.CENTER, text="Please input the intensity of each emotion on a scale of 1-5, \n 1 being minimal and 5 being maximal. \n If you feel the emotion was not experienced, enter 0.", font="Helvetica 13", bg = "gray70")
	text2.place(x=300, y=150, anchor=tk.CENTER)
	# input mood numbers
	emotion_list= ["Sadness", "Happiness", "Fear", "Anger", "Surprise", "Disgust"]
	row_counter = 0
	dist = 0
	labels = []
	text_boxes = []

	for emotion in emotion_list:
	    new_label = tk.Label(root, text=emotion, width=15, font="Helvetica 15", bg = "gray70")
	    new_label.pack()
	    new_label.place(x=180, y=200+dist)
	    text_box = Text(root, width=5, height=1, font="Helvetica 10")
	    text_box.pack()
	    text_box.place(x=320, y=205+dist)
	    text_boxes.append(text_box)
	    labels.append(new_label)
	    
	    row_counter += 1
	    dist += 30
	#save data

	def save(text_boxes):
		with open(r"mood_data.csv", 'a', newline='') as file:
			global row
				# for text_box in text_boxes:
				# 	writer = csv.writer(file)
				# 	text = [text_box.get("1.0", "end-1c")]
				# 	writer.writerows([text])
			writer = csv.writer(file)
			rowtemp = [text_box.get("1.0", "end-1c") for text_box in text_boxes]
			row[1:] = rowtemp
			writer.writerow(row)
		
		for text_box in text_boxes:
			text_box.destroy()
		for label in labels:
			label.destroy()
		text2.destroy()
		save_button.destroy()


# save & return button to main screen
	save_button = tk.Button(root, text="Save & Return", bd='5', font="Helvetica 15", activebackground="darkorchid3", 
								activeforeground= "white", command= lambda: ((save(text_boxes)), GUI(root)))
	save_button.place(x=500, y =550, anchor=tk.CENTER)
	# back button to input_data1

# screen for viewing data
def view_data(root, open_text1, open_text2, input_button, view_button):
	open_text1.destroy()
	open_text2.destroy()
	input_button.destroy()
	view_button.destroy()
	text = tk.Label(root, justify=tk.CENTER, text="A visual demonstration of your moods \n from your saved dates will open in a new window.", 
						font="Helvetica 15", bg = "gray70") 
	text.place(x=300, y=150, anchor=tk.CENTER)
	df = pd.read_csv("mood_data.csv", header=None)
	# print(df)
	# plot
	plt.plot(df[0], df[1], color="blue", label="Sadness")
	plt.plot(df[0], df[2], color="orange", label="Happiness")
	plt.plot(df[0], df[3], color="purple", label="Fear")
	plt.plot(df[0], df[4], color="red", label="Anger")
	plt.plot(df[0], df[5], color="pink", label="Surprise")
	plt.plot(df[0], df[6], color="green", label="Disgust")
	plt.legend() 
	plt.show()
	# return button
	
	return_button = tk.Button(root, text="Return to Home", bd='5', font="Helvetica 15", activebackground="darkorchid3", 
								activeforeground= "white", command= lambda: (text.destroy(), return_button.destroy(), GUI(root)))
	return_button.place(x=500, y =550, anchor=tk.CENTER)
	

if __name__ == '__main__':
    main()