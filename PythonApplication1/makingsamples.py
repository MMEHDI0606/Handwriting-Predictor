import tkinter as tk
from tkinter import Canvas, simpledialog
from PIL import Image, ImageDraw, ImageOps
import os

# Create save directory
save_dir = "custom_digits"
os.makedirs(save_dir, exist_ok=True)

# Setup GUI
window = tk.Tk()
window.title("Handwritten Digit Collector")

canvas = Canvas(window, width=200, height=200, bg="white")
canvas.grid(row=0, column=0, pady=2, sticky="W")

label = tk.Label(window, text="Draw a digit and click 'Save'", font=("Helvetica", 14))
label.grid(row=0, column=1, padx=10)

# Create PIL image and draw object
image_draw = Image.new("RGB", (200, 200), "white")
draw = ImageDraw.Draw(image_draw)

def paint(event):
    x1, y1 = (event.x - 7), (event.y - 7)
    x2, y2 = (event.x + 7), (event.y + 7)
    canvas.create_oval(x1, y1, x2, y2, fill="black", width=8)
    draw.ellipse([x1, y1, x2, y2], fill="black")

canvas.bind("<B1-Motion>", paint)

# Save drawing
def save_digit():
    global image_draw
    digit = simpledialog.askstring("Input", "Enter the digit you drew (0-9):")
    if digit is not None and digit.isdigit() and len(digit) == 1:
        digit_class = digit
        filename = f"{digit_class}_{len(os.listdir(os.path.join(save_dir, digit_class)))}.png" if os.path.exists(os.path.join(save_dir, digit_class)) else f"{digit_class}_0.png"
        path = os.path.join(save_dir, digit_class)
        os.makedirs(path, exist_ok=True)
        image_draw.save(os.path.join(path, filename))
        label.config(text=f"Saved {digit} as {filename}")
    else:
        label.config(text="Invalid input. Please enter a digit between 0 and 9.")

save_button = tk.Button(window, text="Save Digit", command=save_digit, bg="lightgreen")
save_button.grid(row=1, column=0)

clear_button = tk.Button(window, text="Clear", command=lambda: [canvas.delete("all"), draw.rectangle([0, 0, 200, 200], fill="white")], bg="orange")
clear_button.grid(row=1, column=1)

window.mainloop()