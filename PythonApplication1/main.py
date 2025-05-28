import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageDraw, ImageOps
import numpy as np
import tensorflow as tf

# Load model
try:
    model = tf.keras.models.load_model('mnist_cnn_model.keras')
except Exception as e:
    print("Error loading model:", e)
    exit()

# Global variable to store current drawing for debugging
current_prediction_data = {}

# Preprocess image
def prepare_image(img):
    # Resize to 28x28
    img = img.resize((28, 28))
    
    # Convert to grayscale
    img = img.convert('L')
    
    # Invert colors (black-on-white like MNIST)
    img = ImageOps.invert(img)
    
    # Thresholding: remove noise by making pixels either black or white
    img = img.point(lambda x: 0 if x < 200 else 255, '1')
    
    # Normalize and reshape
    img = np.array(img).astype('float32') / 255.0
    img = img.reshape(1, 28, 28)  # Add batch dimension
    
    return img

# Reset all values after prediction
def reset_prediction():
    global current_prediction_data
    current_prediction_data = {}  # Clear any stored data
    print("Prediction state reset.")

# Predict digit (called each time "Predict" is clicked)
def predict_digit():
    # Create blank image
    img = Image.new("RGB", (200, 200), "white")
    draw = ImageDraw.Draw(img)

    # Redraw all items from canvas
    for item in canvas.find_all():
        coords = canvas.coords(item)
        x1, y1, x2, y2 = coords
        fill_color = canvas.itemcget(item, "fill")
        if not fill_color:
            fill_color = "black"
        draw.ellipse([x1, y1, x2, y2], fill=fill_color)

    # Prepare and predict
    processed_img = prepare_image(img)
    
    prediction = model.predict(processed_img)
    predicted_digit = np.argmax(prediction)
    confidence = np.max(prediction) * 100

    # Update label
    label.config(text=f"Predicted Digit: {predicted_digit} ({confidence:.2f}%)")

    # Store for debugging (optional)
    current_prediction_data['image'] = img
    current_prediction_data['prediction'] = predicted_digit
    current_prediction_data['confidence'] = confidence

    # Reset internal state
    reset_prediction()

# Draw on canvas
def paint(event):
    x1, y1 = (event.x - 7), (event.y - 7)
    x2, y2 = (event.x + 7), (event.y + 7)
    canvas.create_oval(x1, y1, x2, y2, fill="black", width=8)

# Clear canvas
def clear_canvas():
    canvas.delete("all")
    label.config(text="Predicted Digit: ")

# Setup GUI
window = tk.Tk()
window.title("Handwritten Digit Recognizer")

canvas = Canvas(window, width=200, height=200, bg="white")
canvas.grid(row=0, column=0, pady=2, sticky="W")

label = tk.Label(window, text="Predicted Digit: ", font=("Helvetica", 16))
label.grid(row=0, column=1, padx=10)

predict_button = tk.Button(window, text="Predict", command=predict_digit, bg="lightblue")
predict_button.grid(row=1, column=1)

clear_button = tk.Button(window, text="Clear", command=clear_canvas, bg="lightgreen")
clear_button.grid(row=1, column=0)

canvas.bind("<B1-Motion>", paint)

window.mainloop()