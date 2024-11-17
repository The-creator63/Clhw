#importing the libraries
from tkinter import*
import calendar
import random
r = random.randint(1,255)
g = random.randint(1,255)
b = random.randint(1,255)
#Functions for showing the calendar
def show_cal():
    global r
    global g
    global b
    new_root = Tk()
    new_root.config(background = (r,g,b))
    new_root.title("calendar")
    new_root.geometry("550x600")

    get_year = int(year.get())
    cal_content = calendar.calendar(get_year)
    cal_year = Label(new_root,text = cal_content,font = ("Consolas 10 bold"))
    cal_year.grid(row = 5,column = 1,padx = 20)
    new_root.mainloop()

#create the main window
if __name__ == "__main__":
    root = Tk()
    root.config(background = (r,g,b))
    root.title("CALENDAR")
    root.geometry("250x180")
    cl = Label(root,text = "CALENDAR",bg = "yellow", fg = "black", font = ("Times", 25, "bold"))
    year_lbl = Label(root,text = "Enter Year",bg = "black",fg = "yellow", font = ("Times", 18, "bold"))
    year = Entry(root) 
    cal_btn = Button(root,text = "Show Calendar",bg = "red",fg = "black",font = ("Times",16,"bold"),command = show_cal)
    exit_btn = Button(root,text = "Exit",bg = "red",fg = "black",font = ("Times", 14,"bold"),command = exit)
    cl.pack()
    year_lbl.pack()
    year.pack()
    cal_btn.pack()
    exit_btn.pack()                                      
    root.mainloop()