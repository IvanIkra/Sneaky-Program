import tkinter as tk
import random


class ValentineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Valentine's Day")
        self.root.geometry("600x600")
        self.root.configure(bg="white")

        self.canvas = tk.Canvas(self.root, width=600, height=600, bg="white", highlightthickness=0)
        self.canvas.place(x=0, y=0)

        self.hearts = []
        for _ in range(12):
            x = random.randint(20, 580)
            y = random.randint(-300, 0)
            heart = self.canvas.create_text(x, y, text="❤️", font=("Arial", 30))  
            self.hearts.append(heart)

        self.animate_hearts()

        self.canvas.create_text(300, 100, text="Will u be my Valentine?", font=("Arial", 20), fill="black")

        button_width = 80
        button_spacing = 20
        center_x = (600 - (button_width * 2 + button_spacing)) // 2

        self.button_yes = tk.Button(self.root, text="Yes", font=("Arial", 16), command=self.show_second_screen)
        self.button_yes.place(x=center_x, y=300, width=button_width, height=50)

        self.button_no = tk.Button(self.root, text="No", font=("Arial", 16), command=self.move_no_button)
        self.button_no.place(x=center_x + button_width + button_spacing, y=300, width=button_width, height=50)

        self.no_clicks = 0

    def move_no_button(self):
        self.no_clicks += 1

        if self.no_clicks >= 10:
            self.button_no.config(text="Yes", command=self.show_second_screen)
        else:
            new_x = random.randint(150, 450)
            new_y = random.randint(250, 450)
            self.button_no.place(x=new_x, y=new_y)

    def animate_hearts(self):
        for heart in self.hearts:
            self.canvas.move(heart, 0, 5)
            x, y = self.canvas.coords(heart)
            if y > 600:
                self.canvas.move(heart, 0, -650)
        self.root.after(50, self.animate_hearts)

    def show_second_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.configure(bg="red")

        label1 = tk.Label(self.root, text="I knew you would say yes.", font=("Arial", 20), bg="red", fg="white")
        label1.pack(pady=100)

        label2 = tk.Label(self.root, text="I'll see you on the 14th at 20:30", font=("Arial", 20), bg="red", fg="white")
        label2.pack()

        label3 = tk.Label(self.root, text="Arbat St", font=("Arial", 20), bg="red", fg="white")
        label3.pack(pady=10)

        label4 = tk.Label(self.root, text="Love, Ivanikra", font=("Arial", 14), bg="red", fg="white")
        label4.place(x=10, y=570)


if __name__ == "__main__":
    root = tk.Tk()
    app = ValentineApp(root)
    root.mainloop()