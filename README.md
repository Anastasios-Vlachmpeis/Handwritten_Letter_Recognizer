# Handwritten Letter Recognizer
#### Video Demo:  <URL HERE>
#### Description:
The Handwritten Letter Recognizer is an interactive desktop application, that can identify handwritten letters from A to Z.\
It provides the user a digital canvas to draw a letter. After the user draws a letter and presses the "Predict" button,\
the application uses a Convolutional Neural Network to analyze the shape, curves, and strokes of the user's drawing, as to\
determine which letter of the English alphabet it is most likely to represent.

**This project (built solely using Python and four external libraries) demonstrates the integration of deep learning models with a GUI, focusing on the precise data preprocessing required for accurate machine learning predictions.**

### How the Application Works
The project functions through a pipeline of user input, image transformation, and neural network classification.

#### The GUI
The interface is built using *tkinter* and centered around a small 280x280 pixel canvas. It employs a *dual-layer* drawing system:\
The Visible Layern, which draws a black oval on the screen for real-time user feedback\
The Processing Layer, which draws the user's strokes on a background PIL image object at the same time, which will be analyzed by the model.

#### The Neural Network Logic
The application’s "brain" is a CNN trained on the Letters split of the EMNIST dataset, which contains thousands of handwritten examples.\
The model identifies characters by breaking down the image into numerical patterns-detecting edges, curves, and junctions that define letters like "A", "B" or "Z".

### Main Challenges and Solutions
#### Several technical problems were resolved to make sure that human handwriting matches the model's training data:

- The Orientation Problem -- A major challenge was that the EMNIST dataset stores characters in a modified format.\
To a standard model, the drawn letter "N" looks like an "Z" because the data is sideways and mirrored.\
    *Solution: I implemented a transformation in the pre function that rotates the image and mirrors it. This aligns the user's drawing with what the model expects.*\

- Performance Optimization -- Loading a neural network model is computationally expensive and caused the GUI to freeze for a few seconds.\
    *Solution: I moved the model loading process to the global scope at the top of the script. This ensures the model is loaded only once when the application starts, resulting in instant predictions.*

### Limitations and Proposed Future Enhancements
The current version of the application can successfully identify single uppercase letters. Still, there are a few areas where it could be enhanced:
- Expanded Character Set: Currently, the model can predict only capital letters from A to Z. Future versions could be trained to recognize lowercase letters, numbers, punctuation and special characters.
- Word and Sentence Recognition: The current GUI is designed for a single character at a time. An enhancement would be for the application to recognize entire words or sentences.
- Real-time Prediction: Instead of the "Predict" button, the model could be refined to run every time a user lifts their mouse.

### File structure:
- [project.py](project.py) : The main script containing the mainApp class, the UI layout, and the image processing pipeline.
- [model_training.py](model_training.py) : A script used to get the EMNIST dataset, define the CNN architecture, and train the model.
- [test_project.py](test_project.py) : The project's test that uses pytest to verify that character mapping, image resizing, and orientation corrections are working as intended.
- [simple_model.h5](simple_model.h5) : The saved neural network containing the trained weights for uppercase character recognition.
- [requirements.txt](requirements.txt) : Lists necessary libraries: tensorflow, Pillow, numpy, and pytest.

### How to Run the Project on your device!
1) Install Dependencies: Run *pip install tensorflow pillow numpy pytest*

2) Generate the Model: Run *python model_training.py* to generate the model. No need to take this action more than once per project.

2) Launch the App: Run *python project.py*

3) Draw and Predict: Draw a large capital letter. Click "Predict" to see the character classification result.

4) Run Tests: Type *pytest test_project.py* to confirm the logic functions correctly.
# Handwritten Letter Recognizer
#### Video Demo:  <URL HERE>
#### Description:
The Handwritten Letter Recognizer is an interactive desktop application, that can identify handwritten letters from A to Z.\
It provides the user a digital canvas to draw a letter. After the user draws a letter and presses the "Predict" button,\
the application uses a Convolutional Neural Network to analyze the shape, curves, and strokes of the user's drawing, as to\
determine which letter of the English alphabet it is most likely to represent.

**This project (built solely using Python and four external libraries) demonstrates the integration of deep learning models with a GUI, focusing on the precise data preprocessing required for accurate machine learning predictions.**

### How the Application Works
The project functions through a pipeline of user input, image transformation, and neural network classification.

#### The GUI
The interface is built using *tkinter* and centered around a small 280x280 pixel canvas. It employs a *dual-layer* drawing system:\
The Visible Layern, which draws a black oval on the screen for real-time user feedback\
The Processing Layer, which draws the user's strokes on a background PIL image object at the same time, which will be analyzed by the model.

#### The Neural Network Logic
The application’s "brain" is a CNN trained on the Letters split of the EMNIST dataset, which contains thousands of handwritten examples.\
The model identifies characters by breaking down the image into numerical patterns-detecting edges, curves, and junctions that define letters like "A", "B" or "Z".

### Main Challenges and Solutions
#### Several technical problems were resolved to make sure that human handwriting matches the model's training data:

- The Orientation Problem -- A major challenge was that the EMNIST dataset stores characters in a modified format.\
To a standard model, the drawn letter "N" looks like an "Z" because the data is sideways and mirrored.\
    *Solution: I implemented a transformation in the pre function that rotates the image and mirrors it. This aligns the user's drawing with what the model expects.*\

- Performance Optimization -- Loading a neural network model is computationally expensive and caused the GUI to freeze for a few seconds.\
    *Solution: I moved the model loading process to the global scope at the top of the script. This ensures the model is loaded only once when the application starts, resulting in instant predictions.*

### Limitations and Proposed Future Enhancements
The current version of the application can successfully identify single uppercase letters. Still, there are a few areas where it could be enhanced:
- Expanded Character Set: Currently, the model can predict only capital letters from A to Z. Future versions could be trained to recognize lowercase letters, numbers, punctuation and special characters.
- Word and Sentence Recognition: The current GUI is designed for a single character at a time. An enhancement would be for the application to recognize entire words or sentences.
- Real-time Prediction: Instead of the "Predict" button, the model could be refined to run every time a user lifts their mouse.

### File structure:
- [project.py](project.py) : The main script containing the mainApp class, the UI layout, and the image processing pipeline.
- [model_training.py](model_training.py) : A script used to get the EMNIST dataset, define the CNN architecture, and train the model.
- [test_project.py](test_project.py) : The project's test that uses pytest to verify that character mapping, image resizing, and orientation corrections are working as intended.
- [simple_model.h5](simple_model.h5) : The saved neural network containing the trained weights for uppercase character recognition.
- [requirements.txt](requirements.txt) : Lists necessary libraries: tensorflow, Pillow, numpy, and pytest.

### How to Run the Project on your device!
1) Install Dependencies: Run *pip install tensorflow pillow numpy pytest*

2) Generate the Model: Run *python model_training.py* to generate the model. No need to take this action more than once per project.

2) Launch the App: Run *python project.py*

3) Draw and Predict: Draw a large capital letter. Click "Predict" to see the character classification result.

4) Run Tests: Type *pytest test_project.py* to confirm the logic functions correctly.