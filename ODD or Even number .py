import tkinter as tk
from tkinter import ttk
#import ttkbootstrap as ttk

def rezultat():
    item = entryInt.get()
    if item % 2 != 0:
        output_string.set("impar")
    else:
        output_string.set("par")



#print(entryInt.get())
# output_string.set("TEST")



root = tk.Tk()
root.title('par sau impar')
root.geometry('300x110')
root.resizable(False, False)

title_label = tk.Label(root, text='Par sau impar')
title_label.pack()


input_frame=ttk.Frame(root)
entryInt = tk.IntVar()
input_text1 = tk.Entry(input_frame, textvariable=entryInt)
button_text1 = tk.Button(input_frame, text='Testeaza',command=rezultat)
input_text1.pack(side=tk.LEFT, padx =10)
button_text1.pack(side=tk.LEFT)
input_frame.pack(pady = 10)


output_string = tk.StringVar()
text_rezultat = tk.Label(root,text = "rezultat", font="Verdana 12 ", textvariable = output_string)
text_rezultat.pack(pady = 5)


root.mainloop()