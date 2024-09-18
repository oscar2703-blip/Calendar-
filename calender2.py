from tkinter import*
import calender

def showCal():
    new_gui = Tk()
    new_gui.config(background="cyan")
    new_gui.title("CALENDAR")
    new_gui.geometry("200x200")
    fetch_year=int(year_field.get())
    cal_content = calender.calender(fetch_year)
    cal_year.grid(row=5,column=1,padx=20)
    new_gui.mainloop()
    
if __name__ == "__main__":
    gui = Tk()
    gui.config(background="white")
    gui.title("CALENDAR")
    gui.geometry("200x200")

    cal = Label(gui,text="Calender",bg="red",font=("times",28,"bold"))
    year = Label(gui,text="Year",bg="red",font=("times",28,"bold"))
    year_field=Entry(gui)
    show_year=Button(gui,text="Show Year",fg="green",bg="purple",command=showCal)
    exit=Button(gui,text="Exit",fg="green",bg="purple",command=exit)
    
    cal.grid(row=1,column=1)
    year.grid(row=2,column=1)
    year_field.grid(row=3,column=1)
    show_year.grid(row=4,column=1)
    exit.grid(row=5,column=1)

    gui.mainloop()