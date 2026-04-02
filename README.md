# Bone-fracture-detection-ml
A machine learning-based system for detecting and classifying bone fractures from X-ray images using CNN-based feature extraction and Random Forest classification.

## 📑 Table of Contents

- Features  
- Project Structure  
- Prerequisites  
- Setup Instructions  
  - Backend  
- Running the Application  
- Dataset  
- Performance Metrics  
- Troubleshooting  
- License

## 🚀 Features

- End-to-end computer vision pipeline for X-ray bone classification  
- CNN-based feature extraction to capture spatial patterns from medical images  
- Random Forest classifier with 200 estimators for robust prediction  
- Image preprocessing including resizing (32×32) and normalization  
- High-dimensional feature vector generation (3072 features per image)  
- Achieved ~84% accuracy on unseen test data
- Model evaluation using precision, recall, F1-score, and accuracy  
- Tkinter-based GUI for instant X-ray image prediction  
  
## 📁 Project Structure

```
📁 bone-fracture-detection-ml/
├── main.py
├── BoneClassification.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── model/
│   ├── model.txt
│   ├── model_backup.txt
│   ├── X.txt.npy
│   └── Y.txt.npy
│
├── TestImages/
│   ├── sample1.png
│   └── sample2.png
```
## ⚙️ Prerequisites

Ensure the following are installed on your system:

- Python 3.x  
- pip (Python package manager)  
- Required libraries: NumPy, OpenCV, Scikit-learn, Keras, TensorFlow, Matplotlib  
> Recommended: Python 3.10 (for TensorFlow compatibility), Use a virtual environment for dependency management.

---

## 🛠️ Setup Instructions
### Backend

1. Open a terminal and navigate to the project directory:
   ```
   cd bone-fracture-detection-ml
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   
---

## ▶️ Running the Application

Run the main file:
```
python main.py
```
---

> Note: Ensure all required model files are present before running the application.

## 📈 Performance Metrics

- Accuracy: ~84%  
- Precision: ~0.85 (weighted) 
- Recall: ~0.84 (weighted) 
- F1-score: ~0.83 (weighted)
  
## 📊 Dataset

- Dataset used: MURA (Musculoskeletal Radiographs Dataset)  
- Total images available: 40,000+  
- Subset used: ~200+ images  

🔗 Dataset Link: https://stanfordmlgroup.github.io/competitions/mura/

Includes bone types such as:
- Finger  
- Wrist  
- Elbow  
- Shoulder  
- Hand
- Head
- Chest
 > Note: Due to computational constraints, a subset of the dataset was used for training and evaluation.

---

## ⚠️ Troubleshooting

- Ensure all required dependencies are installed using `pip install -r requirements.txt`  
- Verify that all model files (`model.txt`, `X.txt.npy`, `Y.txt.npy`) are present inside the `model/` directory  
- Check image file paths and ensure supported formats (JPG, PNG)
- Ensure input images are properly preprocessed (resized to 32×32 and normalized)  
- If prediction errors occur, confirm that the feature vector shape matches the trained model input (3072 features)  
- Ensure compatible Python version (Python 3.x recommended)

  > Tip: Most issues arise from incorrect file paths, missing model files, or mismatched input dimensions.
---

## 📄 License

This project is for educational purposes.

