import tkinter as tk
from random import randint

class ClickerGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Clicker Game")

        self.points = 0

        self.points_label = tk.Label(master, text="Points: 0")
        self.points_label.pack()

        self.button = tk.Button(master, text="", command=self.click, bg="red", width=10, height=5)
        self.button.pack(pady=20)

    def click(self):
        self.points += 1
        self.update_points_label()

    def update_points_label(self):
        self.points_label.config(text=f"Points: {self.points}")

if __name__ == "__main__":
    root = tk.Tk()
    game = ClickerGame(root)
    root.mainloop()
