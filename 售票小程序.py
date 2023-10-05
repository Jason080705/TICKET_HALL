import random
import tkinter as tk
from tkinter import messagebox

def generate_ticket():
    #获取用户名字并介绍售票员
    name = name_entry.get()
    ticket_officers = ['Eric Matthes', 'Amy Wells', 'Thando Smith', 'Stephanie Wu']
    chosen_officer = random.choice(ticket_officers)

    #获取购票人数量
    number_of_people = people_entry.get()

    try:
        num_of_tickets = int(number_of_people)
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter a valid number.")
        return

    #判断是1个人还是多人，并生成票价
    if num_of_tickets == 1:
        price_of_tickets = 10
        result_text.set(f"Only yourself? That's {price_of_tickets} Dollars.")
    else:
        price_of_tickets = num_of_tickets * 10
        result_text.set(f"OK! That's {price_of_tickets} Dollars.")

    #询问预订参观日期
    date_of_visit = date_entry.get()

    #显示结果
    messagebox.showinfo("Ticket Information", f"Buyer's Name: {name}\nTicket Officer: {chosen_officer.title()}\nPrice of tickets: {price_of_tickets}\nNumber of visitors: {number_of_people}\nDate of Visit: {date_of_visit}")

#创建GUI窗口
window = tk.Tk()
window.title("Ticket Booking")
window.geometry("400x300")

#用户名字标签和输入框
name_label = tk.Label(window, text="Hello! Welcome to the Yellowstone National Park. May I ask who you are?")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

#购票人数量标签和输入框
people_label = tk.Label(window, text="How many people are coming with you?")
people_label.pack()
people_entry = tk.Entry(window)
people_entry.pack()

#预订参观日期标签和输入框
date_label = tk.Label(window, text="Please enter your desired date of visit (YYYY/MM/DD):")
date_label.pack()
date_entry = tk.Entry(window)
date_entry.pack()

#生成票价按钮
generate_button = tk.Button(window, text="Generate Ticket", command=generate_ticket)
generate_button.pack()

#显示结果的标签
result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text)
result_label.pack()

#运行GUI窗口
window.mainloop()
