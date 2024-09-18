from tkinter import*


root = Tk()
root.geometry('300x300')

# creating Widgets
cal=Label(root,text="Calender")
year=Label(root,text="Year")
year_field = Entry(root)
show_button=Button(root,text="Show Year")
exit=Button(root,text="Exit")

# placing widgets in the grid
cal.grid(row=1,column=1)
year.grid(row=2,column=1)
year_field.grid(row=3,column=1)
show_button.grid(row=4,column=1)
exit.grid(row=5,column=1)
root.mainloop()