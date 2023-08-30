import tkinter as tk
import tkinter.messagebox as mb
import tkinter.ttk as ttk

def print_details():
    print(first_name_var.get(), last_name_var.get())
    mb.showinfo(title="Details", message=first_name_var.get() +" "+ last_name_var.get() + "\n" + " {} is a really good choice! ".format(fav_food_var.get()))


root = tk.Tk()


left_frame = tk.Frame(root)
left_frame.grid(row=0,column=0)


first_name_var = tk.StringVar()
first_name_label = tk.Label(left_frame, text="First Name")
first_name_label.grid(row=0, column = 0)
first_name_entry = tk.Entry(left_frame, textvariable=first_name_var)
first_name_entry.grid(row=0, column=1)


last_name_var = tk.StringVar()
last_name_label = tk.Label(left_frame, text="last name")
last_name_label.grid(row=1, column = 0)
last_name_entry = tk.Entry(left_frame, textvariable=last_name_var)
last_name_entry.grid(row=1, column=1)


fast_food_options = ["KFC", "McDonalds", "Hungry Jacks", "Dominos"]
fav_food_var = tk.StringVar()
fav_food_label=tk.Label(left_frame, text ="Favorite food")
fav_food_label.grid(row=2,column=0)
fav_food_entry = ttk.Combobox(left_frame, textvariable=fav_food_var, values=fast_food_options)
fav_food_entry.grid(row=2,column=1)
 
button_frame =tk.Frame(root)
button_frame.grid(row=1, column=0, columnspan=2, sticky=tk.W+tk.E)

print_button = tk.Button(button_frame, text="Print", command=print_details)
print_button.grid(row=0, column=0,padx=5, pady=5)

quit_button = tk.Button(button_frame, text="Quit")
quit_button.grid(row=0,column=1, ipadx=5, ipady=5)

root.mainloop()