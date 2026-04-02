# Bone-fracture-detection-ml
A machine learning-based system for detecting bone fractures from X-ray images using CNN-based feature extraction and Random Forest classification.

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
- X-ray image classification using machine learning  
- CNN-based feature extraction  
- Random Forest classifier (200 estimators)  
- Image preprocessing (resizing, normalization)  
- Feature vector generation (3072 features)  
- Achieved ~84% accuracy  
- GUI-based prediction system using Tkinter
  
## 📁 Project Structure

```
bone-fracture-detection-ml/
│
├── main.py
├── BoneClassification.py
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
│
├── requirements.txt
├── README.md
└── .gitignore
```
## ⚙️ Prerequisites

- Python (3.x recommended)  
- pip  

---

## 🛠️ Setup Instructions
### Backend

1. Open a terminal and navigate to the project directory:
   cd bone-fracture-detection-ml
2. Install dependencies:
   pip install -r requirements.txt
   
---

## ▶️ Running the Application

Run the main file:python main.py
---

## 📊 Dataset

- Dataset used: MURA dataset  
- Total images available: 40,000+  
- Subset used: ~200+ images  
- Includes bone types such as:
  - Finger  
  - Wrist  
  - Elbow  
  - Shoulder
  - Hand
  - Head
  - Chest

---

## ⚠️ Troubleshooting

- Ensure all dependencies are installed correctly  
- Check if model files are present in the `model/` folder  
- Verify image path while testing  
- Ensure Python version compatibility  

---

## 📄 License

This project is for educational purposes.

