import tkinter as tk
from PIL import Image, ImageOps, ImageDraw
import numpy as np
import tensorflow as tf

mp = "simple_model.h5"
model = tf.keras.models.load_model(mp)

class mainApp:
    def __init__(self,root):
        self.root = root
        self.root.title("ML based Text Recognizer")
        #canvas creation
        self.canvas = tk.Canvas(self.root, width=280, height=280, bg="white", cursor="cross")
        self.canvas.grid(row=0, column=0, pady=10, padx=10, columnspan=2)
        self.canvas.bind("<B1-Motion>", self.paint)
        #creation of the image that the CNN will process, and the image's 'drawing' object
        self.image = Image.new("L", (280, 280), "white")
        self.draw = ImageDraw.Draw(self.image)
        #'Predict' button
        self.pred_b = tk.Button(self.root, text="Predict", command=self.predict)
        self.pred_b.grid(row=1, column=0, sticky="ew")
        #'Clear' button
        self.cl_b = tk.Button(self.root, text="Clear", command=self.clear)
        self.cl_b.grid(row=1, column=1, sticky="ew")
        #prediction result text
        self.pred_txt = tk.Label(self.root, text="Draw a letter (A-Z)", font=("Inter", 18))
        self.pred_txt.grid(row=2, column=0, columnspan=2, pady=10)

    #mouse drawing both on the actual canvas, and the PIL image
    def paint(self, event):
        x1, y1 = (event.x - 8), (event.y - 8)
        x2, y2 = (event.x + 8), (event.y + 8)
        self.canvas.create_oval(x1, y1, x2, y2, fill="black", width=15)
        self.draw.line([x1, y1, x2, y2], fill="black", width=15)

    #clear the canvas
    def clear(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (280, 280), "white")
        self.draw = ImageDraw.Draw(self.image)
        self.pred_txt.config(text="Draw a letter (A-Z)")

    #text drawing processing and result text update
    def predict(self):
        self.image.save("letter.png")
        prediction = im_pred(model, "letter.png")
        self.pred_txt.config(text=f"Result: {prediction}")

#The following functions will be necessary for the test_main test

#model loading and character acquisition
def im_pred(model, image_path):
    img = Image.open(image_path).convert("L")
    processed_img = pre(img)
    prediction = model.predict(processed_img)
    index = np.argmax(prediction)
    return map_label(index)

#EMNIST appropriate image resizing, invertion and normalisation for the CNN
def pre(img):
    img = img.resize((28, 28))
    img = ImageOps.invert(img)
    img = img.rotate(-90)
    img = ImageOps.mirror(img)
    img_array = np.array(img) / 255.0
    return img_array.reshape(1, 28, 28, 1)

#map the number output to a letter (A-Z,1-26)
def map_label(index):
    if 1 <= index <= 26:
        return chr(ord('A') + index - 1)
    return "?"

def main() :
    root = tk.Tk()
    app = mainApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
