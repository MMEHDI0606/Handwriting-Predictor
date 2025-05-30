
# 📝 Handwritten Digit Recognizer

A simple GUI-based application that recognizes handwritten digits (0–9) using a custom-trained deep learning model.

Built with:
- Python
- TensorFlow/Keras
- Tkinter GUI
- PIL / NumPy / Matplotlib

---

## 🔍 Overview

This project allows users to draw digits using their mouse and get real-time predictions from a neural network trained on **custom handwriting samples**.

The model is saved in `.keras` format and runs locally — no internet required!

---

## 🧠 Features

- Draw digits using your mouse
- Predict digit using a trained CNN model
- Clear canvas and try again
- Show random MNIST sample for comparison
- Reset internal state after each prediction

---

## 📁 Folder Structure

```
digit_recognizer/
│
├── main.py               # GUI application
├── train_custom_model.py # Model training script
├── custom_digit_model.keras  # Trained model file
├── custom_digits/        # (Optional) Your collected digit images
│   ├── 0/
│   ├── 1/
│   └── ...
└── README.md             # This file
```

---

## 🚀 How to Run

### 1. Clone or download the project
```bash
git clone https://github.com/yourusername/digit-recognizer.git
cd digit-recognizer
```

### 2. Install dependencies
Make sure you have Python 3.x installed.

```bash
pip install tensorflow pillow numpy matplotlib
```

> Note: If you're retraining the model, also install `tensorflow`.

### 3. Train the model (optional)
To train a new model on your own handwriting:

```bash
python train_custom_model.py
```

> Make sure you've added your drawings to the `custom_digits/` folder.

### 4. Run the GUI App
```bash
python main.py
```

You’ll see a small window where you can draw and predict digits.

---

## 🧪 How It Works

1. You draw a digit inside the canvas.
2. The app captures your drawing as an image.
3. The image is preprocessed to match MNIST style (resize, invert, threshold).
4. The model predicts the digit and shows the result with confidence.
5. All values are reset so you can draw again!

---

## 🛠️ Technologies Used

| Tool/Library | Purpose |
|-------------|---------|
| `TensorFlow/Keras` | Deep learning model |
| `Tkinter` | GUI interface |
| `PIL (Pillow)` | Image processing |
| `NumPy` | Array manipulation |
| `Matplotlib` | Visualizing MNIST samples |

---

## ✅ Requirements

- Python 3.8+
- Windows, macOS, or Linux
- Mouse or touchpad for drawing

---

## 📦 Want to Package as .exe?

You can turn this into a standalone desktop app using **PyInstaller**:

```bash
pip install pyinstaller
pyinstaller --onefile main.py
```

---

## 💬 Feedback & Contributions

Contributions, issues, and feature requests are welcome!

Let me know if you'd like help:
- Improving accuracy
- Adding webcam support
- Packaging as mobile/web app
- Training with more advanced models

---

## 👨‍💻 Developed by  
[Your Name or GitHub Handle]  
📅 Date: April 2025

---

Let me know if you want this in a downloadable `.md` file or formatted for GitHub/GitLab! 😊
