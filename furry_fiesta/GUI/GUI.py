# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 16:10:12 2019

@author: benjaminl2
"""

from tkinter import Tk, Label, Button, Frame, Entry
top = Tk()
top.title('Test Gui')
top.geometry('500x500')



T= Label(top, text = "Fury Fiesta GUI")
T.config(font=("Courier", 28))
T.place(relx = 0.5, rely = 0.1, anchor = 'center')



b1 = Button(top, text="One")
b1.place(relx = 0.5, rely = 0.25, anchor = "center")

b2 = Button(top, text="Two")
b2.place(relx = 0.5, rely = 0.5, anchor = "center")

l= Label(top, text = "This is a Label")
l.place(relx = 0.5, rely = 0.75, anchor = "center")


#------ Frame for entering your age ---------

age_l = Frame( master = top, width =150, height = 150, bg = '#F0F0F0')
age_l.place(relx=0.25, rely=0.25, anchor ='center')


l2= Label(age_l, text = "Enter your Age")
l2.grid(row = 0, column = 0)

i_age = Entry(top)
a = Entry(age_l, textvariable=i_age)
a.grid(row =1, column = 0)

#------ Frame for entering your gender ---------

gender_l = Frame( master = top, width =150, height = 150, bg = '#F0F0F0')
gender_l.place(relx=0.25, rely=0.5, anchor ='center')


l3= Label(gender_l, text = "Enter your Gender")
l3.grid(row = 0, column = 0)

i_gender = Entry(top)
g = Entry(gender_l, textvariable=i_gender)
g.grid(row =1, column = 0)


#------ Frame for entering your ticket price ---------

ticket_l = Frame( master = top, width =150, height = 150, bg = '#F0F0F0')
ticket_l.place(relx=0.25, rely=0.75, anchor ='center')


l3= Label(ticket_l, text = "Enter your Ticket price")
l3.grid(row = 0, column = 0)

i_ticket = Entry(top)
t = Entry(ticket_l, textvariable=i_ticket)
t.grid(row =1, column = 0)



top.mainloop()