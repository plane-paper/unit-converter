from tkinter import *
# Create a GUI window
window = Tk()
window.title("Lenght Converter")
window.geometry("500x300+550+355")
def lengthconv():
     
    km = float(e2_value.get())/1000
    mm = float(e2_value.get())*1000
    cm = float(e2_value.get())*100
    mile=float(e2_value.get())*0.000621371
    yard=float(e2_value.get())*1.09361296
    inch=float(e2_value.get())*39.3701
    foot=float(e2_value.get())*3.28084
    dm=float(e2_value.get())*10
    
    t1.delete("1.0", END)
    t1.insert(END,km)
     
    t2.delete("1.0", END)
    t2.insert(END,mm)
     
    t3.delete("1.0", END)
    t3.insert(END,cm)
    
    t4.delete("1.0", END)
    t4.insert(END,mile)
   
    t5.delete("1.0", END)
    t5.insert(END,yard)
    
    t6.delete("1.0", END)
    t6.insert(END,inch)
    
    t7.delete("1.0", END)
    t7.insert(END,foot)
    
    t8.delete("1.0", END)
    t8.insert(END,dm)
    
# Creating Label widgets
e1 = Label(window, text = "Enter length in meters",bg="light gray")
e2_value = StringVar()
e2 = Entry(window, textvariable = e2_value)
e3 = Label(window, text = 'km',bg="light gray")
e4 = Label(window, text = 'mm',bg="light gray")
e5 = Label(window, text = 'cm',bg="light gray")
e6 = Label(window, text = 'mile',bg="light gray") 
e7 = Label(window, text = 'yard',bg="light gray") 
e8 = Label(window, text = 'inch',bg="light gray") 
e9 = Label(window, text = 'foot',bg="light gray") 
e10 = Label(window, text = 'dm',bg="light gray") 
# Creating Text Widgets
t1 = Text(window, height = 1, width = 15)
t2 = Text(window, height = 1, width = 15)
t3 = Text(window, height = 1, width = 15)
t4 = Text(window, height = 1, width = 15) 
t5 = Text(window, height = 1, width = 15) 
t6 = Text(window, height = 1, width = 15)
t7 = Text(window, height = 1, width = 15)
t8 = Text(window, height = 1, width = 15)
# Creating  Button Widget
b1 = Button(window, text = "Convert", command = lengthconv)
 
e1.grid(row = 0, column = 0,padx=10,pady=10)
e2.grid(row = 0, column = 1,pady=10,padx=10)
e3.grid(row = 4, column = 0,pady=10,padx=10)
e4.grid(row = 2, column = 0,pady=10,padx=10)
e5.grid(row = 3, column = 0,pady=10,padx=10)
e6.grid(row = 2, column = 2,pady=10,padx=10)
e7.grid(row = 4, column = 2,pady=10,padx=10)
e8.grid(row = 3, column = 2,pady=10,padx=10)
e9.grid(row = 5, column = 0,pady=10,padx=10)
e10.grid(row = 5, column = 2,pady=10,padx=10)
t1.grid(row = 4, column = 1,pady=10,padx=10)
t2.grid(row = 2, column = 1,pady=10,padx=10)
t3.grid(row = 3, column = 1,pady=10,padx=10)
t4.grid(row = 2, column = 3,pady=10,padx=10)
t5.grid(row = 4, column = 3,pady=10,padx=10)
t6.grid(row = 3, column = 3,pady=10,padx=10)
t7.grid(row = 5, column = 1,pady=10,padx=10)
t8.grid(row = 5, column = 3,pady=10,padx=10)
b1.grid(row = 1, column = 1,padx=10,pady=10)
 
exit_button = Button(window, text="Exit", command=window.destroy) 
exit_button.place(x=450,y=255)

window.mainloop()