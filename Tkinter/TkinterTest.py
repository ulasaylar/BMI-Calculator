import tkinter

w = tkinter.Tk()
w.title('BMI Calculator')
w_width = 300
w_height = 400
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
center_x = int(screen_width/2 - w_width / 2)
center_y = int(screen_height/2 - w_height / 2)
w.geometry(f'{w_width}x{w_height}+{center_x}+{center_y}')


def calculate():
    weight = eyw_entry.get()
    height = eyh_entry.get()

    if weight == '' or height == '':
        result_label.config(text='Enter Both Weight And Height!')
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number")


eyw = tkinter.Label(text='Enter Your Weight (KG)',font=('arial',15,'bold'),pady=20)
eyh = tkinter.Label(text='Enter Your Height (CM)',font=('arial',15,'bold'),pady=30)
eyw_entry = tkinter.Entry(width=35)
eyw_entry.place(x=40, y=50, height=25)
eyh_entry = tkinter.Entry(width=35)
eyh_entry.place(x=40, y=130, height=30)
eyw.pack()
eyh.pack()
calculate_button = tkinter.Button(text='Calculate',command= calculate)
calculate_button.place(x=120, y=190)

result_label = tkinter.Label(font=('arial',10,'bold'))
result_label.place(x=25,y=165)

def write_result(bmi):
    result_string = f"Your BMI is: {round(bmi,2)}. You are "
    if bmi <= 16:
        result_string += "severely thin!"
    elif 16 < bmi <= 17:
        result_string += "moderately thin!"
    elif 17 < bmi <= 18.5:
        result_string += "mild thin"
    elif 18.5 < bmi <= 25:
        result_string += "normal"
    elif 25 < bmi <= 30:
        result_string += "overweight"
    elif 30 < bmi <= 35:
        result_string += "obese class 1!"
    elif 35 < bmi <= 40:
        result_string += "obese class 2!"
    else:
        result_string += "obese class 3!"
    return result_string


w.mainloop()