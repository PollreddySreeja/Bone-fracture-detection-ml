from tkinter import *
from tkinter import filedialog
import numpy as np
import cv2
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

main = Tk()
main.title("CLASSIFICATION OF FRACTURED BONES USING MACHINE LEARNING")
main.geometry("1300x1200")

global filename, X, Y, X_train, X_test, y_train, y_test, classifier
labels = ['Chest', 'Elbow', 'Finger', 'Hand', 'Head', 'Shoulder', 'Wrist']

def uploadDataset():
    global filename
    filename = filedialog.askdirectory(initialdir=".")
    pathlabel.config(text=filename)
    text.insert(END, filename + ' dataset loaded\n')

def featuresExtraction():
    global X, Y
    text.delete('1.0', END)
    X = np.load('model/X.txt.npy')
    Y = np.load('model/Y.txt.npy')
    text.insert(END, "Available Bones: " + str(labels) + "\n")
    text.insert(END, "Total images: " + str(X.shape[0]) + "\n")
    text.insert(END, "Features per image: " + str(X.shape[1]) + "\n")
    test = X[3].reshape(32, 32, 3)
    test = cv2.resize(test, (250, 250))
    cv2.imshow("Sample Image", test)
    cv2.waitKey(0)

def trainTestGenerator():
    global X_train, X_test, y_train, y_test
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
    text.insert(END, "Train size: " + str(X_train.shape[0]) + "\n")
    text.insert(END, "Test size: " + str(X_test.shape[0]) + "\n")

def randomForest():
    global classifier
    if os.path.exists('model/model.txt'):
        with open('model/model.txt', 'rb') as file:
            classifier = pickle.load(file)
    else:
        classifier = RandomForestClassifier(n_estimators=200, random_state=0)
        classifier.fit(X_train, y_train)
        with open('model/model.txt', 'wb') as file:
            pickle.dump(classifier, file)

    predict = classifier.predict(X_test)
    acc = accuracy_score(y_test, predict) * 100
    text.insert(END, f"Accuracy: {acc:.2f}%\n\n")
    text.insert(END, "Classification Report:\n")
    text.insert(END, classification_report(y_test, predict) + "\n")

def predict():
    global classifier
    test_file = filedialog.askopenfilename(initialdir="testImages")
    img = cv2.imread(test_file)
    img = cv2.resize(img, (32, 32))
    test = img.astype('float32') / 255.0
    test = test.flatten().reshape(1, -1)
    pred = classifier.predict(test)[0]
    img = cv2.resize(img, (400, 400))
    cv2.putText(img, 'Predicted: ' + labels[pred], (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    cv2.imshow("Result", img)
    cv2.waitKey(0)

font = ('times', 16, 'bold')
Label(main, text='CLASSIFICATION OF FRACTURED BONES USING MACHINE LEARNING',
      bg='dark goldenrod', fg='white', font=font, height=3, width=120).place(x=0, y=5)

font1 = ('times', 13, 'bold')
Button(main, text="Dataset Collection or Upload", command=uploadDataset, font=font1).place(x=700, y=100)
pathlabel = Label(main, bg='lawn green', fg='white', font=font1)
pathlabel.place(x=700, y=150)
Button(main, text="Features Extraction", command=featuresExtraction, font=font1).place(x=700, y=200)
Button(main, text="Train & Test Data Generator", command=trainTestGenerator, font=font1).place(x=700, y=250)
Button(main, text="Build Random Forest Model", command=randomForest, font=font1).place(x=700, y=300)
Button(main, text="Upload Test Image & Classify Bone", command=predict, font=font1).place(x=700, y=350)

text = Text(main, height=30, width=80, font=('times', 12, 'bold'))
text.place(x=10, y=100)

main.config(bg='RoyalBlue2')
main.mainloop()
