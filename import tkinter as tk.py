import tkinter as tk
from tkinter import messagebox

class ShoppingList:
    def __init__(self, master):
        self.master = master
        self.master.title('Shopping List')
        
        # Title Label and Entry
        self.titleLabel = tk.Label(master, text="Title of Shopping List:")
        self.titleLabel.pack(pady=10)
        
        self.titleEntry = tk.Entry(master)
        self.titleEntry.pack(pady=10)
        
        # Checkbuttons with associated costs
        self.items = {
            "Nick": 60.00,
            "Max": 61.00,
            "Hemanth": 52.00,
            "Adyan": 52.75
        }

        self.vars = {}
        for item, cost in self.items.items():
            self.vars[item] = tk.IntVar()
            chk = tk.Checkbutton(master, text=f"{item} - ${cost}", variable=self.vars[item])
            chk.pack(anchor='w', padx=20)
        
        # Calculate Button
        self.calcButton = tk.Button(master, text="Calculate", command=self.calculate_cost)
        self.calcButton.pack(pady=20)
        
    def calculate_cost(self):
        total_cost = sum(cost * self.vars[item].get() for item, cost in self.items.items())
        messagebox.showinfo("Total Cost", f"The total cost is: ${total_cost:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingList(master=root)
    root.mainloop()
