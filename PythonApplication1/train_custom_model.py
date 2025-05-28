import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models, Input, callbacks
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Directories
data_dir = "custom_digits"

# Image size
img_size = 28

# Batch size
batch_size = 32

# Data generator with augmentation
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

train_gen = datagen.flow_from_directory(
    data_dir,
    target_size=(img_size, img_size),
    color_mode='grayscale',
    batch_size=batch_size,
    class_mode='categorical',
    subset='training',
    shuffle=True
)

val_gen = datagen.flow_from_directory(
    data_dir,
    target_size=(img_size, img_size),
    color_mode='grayscale',
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'
)

# Build CNN model using Input() layer
model = models.Sequential([
    Input(shape=(img_size, img_size, 1)),
    
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Add callbacks
early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
checkpoint = callbacks.ModelCheckpoint('custom_digit_model.keras',  # Save as .keras
                                      monitor='val_accuracy',
                                      save_best_only=True,
                                      mode='max')

# Train model for 25 epochs
history = model.fit(
    train_gen,
    epochs=75,
    validation_data=val_gen,
    callbacks=[early_stop, checkpoint]
)

# Print final results
print("Training complete.")
print(f"Final Validation Accuracy: {max(history.history['val_accuracy']) * 100:.2f}%")