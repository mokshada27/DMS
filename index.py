from tkinter import *
from flask import Flask,redirect, url_for,render_template,request
import os

def d_dtcn():
	root = Tk()
	root.configure(background = "white")

	def function1(): 
		os.system("python main.py")
		exit()

	def function3():
		os.system("python EmotionDetection.py")
		exit()

	def function4():
		os.system("python HRate.py")
		exit()

	root.title("DISTRACTION DETECTION")
	Label(root, text="DISTRACTION DETECTION",font=("times new roman",20),fg="black",bg="aqua",height=2).grid(row=2,rowspan=2,columnspan=5,sticky=N+E+W+S,padx=5,pady=10)
	Button(root,text="Face Recognition and Drowsiness Detection",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1).grid(row=5,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)
	#Button(root, text="Drowsiness Detection", font=("times new roman", 20), bg="#0D47A1", fg='white',command=function2).grid(row=7, columnspan=5, sticky=W + E + N + S, padx=5, pady=5)
	Button(root, text="Emotion Detection", font=("times new roman", 20), bg="#0D47A1", fg='white',command=function3).grid(row=7, columnspan=5, sticky=W + E + N + S, padx=5, pady=5)
	Button(root, text="Check Drowsiness using Heart Rate", font=("times new roman", 20), bg="#0D47A1", fg='white', command=function4).grid(row=9, columnspan=5, sticky=W + E + N + S, padx=5, pady=5)
	Button(root,text="Exit",font=("times new roman",20),bg="#0D47A1",fg='white',command=root.destroy).grid(row=11,columnspan=5,sticky=W+E+N+S,padx=5,pady=5)

	root.mainloop()