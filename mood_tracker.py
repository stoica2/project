import os, matplotlib as plt, time, numpy as np, pandas as pd
import tkinter as tk

def main():
	root = tk.Tk()
	root.title("Mood Tracker")
	root.geometry('600x600')
	GUI(root)
	root.mainloop()

def GUI(root):
	open_text1 = tk.Label(root, justify=tk.CENTER, text="Welcome to the Mood Tracker!", font="Helvetica 25")
	open_text1.place(x=300, y=150, anchor=tk.CENTER)
	open_text2 = tk.Label(root, justify=tk.CENTER, text="Select one of the options below to get started.", font="Helvetica 15")
	open_text2.place(x=300, y=200, anchor=tk.CENTER)
	input_button = tk.Button(root, text="Input Data", bd='5', font="Helvetica 15", command= lambda: input_data1(root, open_text1, open_text2, input_button, view_button))
	input_button.place(x=150, y=450, anchor=tk.CENTER)
	view_button = tk.Button(root, text="View Data", bd='5', font="Helvetica 15", command= lambda: view_data(root, open_text1, open_text2, input_button, view_button))
	view_button.place(x=450, y =450, anchor=tk.CENTER)

def input_data1(root, open_text1, open_text2, input_button, view_button):
	open_text1.destroy()
	open_text2.destroy()
	input_button.destroy()
	view_button.destroy()
	text1 = tk.Label(root, justify=tk.CENTER, text="Please input today's date.", font="Helvetica 15")
	text1.place(x=300, y=150, anchor=tk.CENTER)
	# input date
	next_button = tk.Button(root, text="Next", bd='5', font="Helvetica 15", command= lambda: input_data2(root, text1, next_button))
	next_button.place(x=550, y =550, anchor=tk.CENTER)

def input_data2(root, text1, next_button):
	text1.destroy()
	next_button.destroy()
	text2 = tk.Label(root, justify=tk.CENTER, text="Please input the intensity of each emotion on a scale of 1-5, \n 1 being minimal and 5 being maximal. \n If no number is provided, it will default to 0 \n and be registered as an unexperienced emotion for the day.", font="Helvetica 15")
	text2.place(x=300, y=150, anchor=tk.CENTER)
	# input mood numbers
	# return button to main screen

def view_data(root, open_text1, open_text2, input_button, view_button):
	open_text1.destroy()
	open_text2.destroy()
	input_button.destroy()
	view_button.destroy()
	text = tk.Label(root, justify=tk.CENTER, text="Here is a visual demonstration of your moods the past week.", font="Helvetica 15")
	text.place(x=300, y=150, anchor=tk.CENTER)

if __name__ == '__main__':
    main()