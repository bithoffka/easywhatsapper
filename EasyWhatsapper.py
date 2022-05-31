'''
EasyWhatsapper
made by bithoffka
https://github.com/bithoffka
'''

import webbrowser as wb
from tkinter import *

#Main function

def contactPerson():
    clearNumber = numberEntry.get()
    link = 'https://wa.me/' + clearNumber + '/'
    print('Number: ' + clearNumber)
    print('Link: ' + link)
    wb.open(link)

#Window parameters

root = Tk()
root.title('EasyWhatsapper')
root.minsize(width=500, height=500)
root.maxsize(width=500, height=650)

label = Label(root, font=('Verdana', 32), text='EasyWhatsapper')
label.pack(side='top')

#Label(root, text='\n\n\n').pack(side='top') is for making new line
#Design XD

Label(root, text='\n\n\n').pack(side='top')

#Basic controls

numberLabel = Label(root, text='Enter your phone number:')
numberEntry = Entry(root, bg='#d19696')
button = Button(root, text='Contact person', command=contactPerson)
numberSubLabel = Label(root, text='Phone number example:\n79197581615', font=('Verdana', 15))

#Packing basic controls

numberLabel.pack()
numberEntry.pack()
Label(root, text='\n\n').pack()
button.pack()
Label(root, text='\n').pack()
numberSubLabel.pack()

#Making simple copyright

copyright = Label(root, font=('Verdana', 14), fg='gray')
copyright.config(text='                                           Made by bithoffka')
copyright.pack(side='bottom')

#Looping the window

root.mainloop()