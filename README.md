# 🎯 Python-Based Object Detector using OpenCV

A **Python-based object detection** application for images and videos using the **OpenCV Deep Neural Networks (DNN) module** with **GoogLeNet** and **YOLOv3** for real-time, high-accuracy detection.  
This project leverages **deep learning inference** to classify and detect objects with bounding boxes and probability scores, using pre-trained models on the **COCO dataset**.

---

## 🧠 Features

- 🖼 **Image Object Detection** – Detects multiple objects in an image and displays their bounding boxes with confidence scores.  
- 🎥 **Video Object Detection** – Detects objects frame-by-frame with probability scores.  
- 🧮 **Color Channel Analysis** – Displays different color channels from the image.  
- ⚡ **YOLOv3 Neural Network** – Divides images into regions and predicts bounding boxes and class probabilities for each region.  
- 📦 **Pre-Trained Models** – Uses GoogLeNet & YOLOv3 models trained on the COCO dataset.  

---

## 🛠 Tech Stack

| Component         | Technology |
|------------------|------------|
| **Language**     | Python |
| **Core Library** | OpenCV |
| **Deep Learning** | OpenCV DNN module |
| **Models Used**  | GoogLeNet, YOLOv3 |
| **Dataset**      | COCO dataset |

---

## 📚 Learning Objectives

- Deep learning for OpenCV  
- Viewing images and videos in OpenCV  
- Working with **blobs** in the DNN module  
- Image classification & video classification  
- YOLOv3-based object detection  

---

## 🗂 Folder Structure
```plaintext
/opencv-object-detector
│
├── /models            # Pre-trained YOLOv3 & GoogLeNet models
├── /images            # Sample images for detection
├── /videos            # Sample videos for detection
├── detector.py        # Main Python script for object detection
├── requirements.txt   # Python dependencies
└── README.md
```
## 🚀 Getting Started

**1️⃣ Clone the Repository**
```bash
git clone https://github.com/Iamdk25/opencv-object-detector.git
cd opencv-object-detector
```
**2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```
**3️⃣ Download Pre-Trained Models**
	•	YOLOv3 Weights
	•	YOLOv3 Config
	•	GoogLeNet pre-trained model from the OpenCV model zoo

Place these files inside the /models directory.

**4️⃣ Run Object Detection on an Image**
```bash
python detector.py --image images/sample.jpg
```
**5️⃣ Run Object Detection on a Video**
```bash
python detector.py --video videos/sample.mp4
```

## 🏆 Completed Functionality
	•	✅ Detect objects in images & display color channels
	•	✅ Detect objects in videos with probability scores
	•	✅ YOLOv3-based custom object detection
	•	✅ Bounding box & confidence prediction per region
	•	✅ Inference-based classification for images & videos

⸻

## 📜 License**

This project is licensed under the MIT License – see the LICENSE file for details.

⸻

## 👨‍💻 Author

## 👨‍💻 Author

**Divyarajsinh Karmariya**  
💼 Computer Science Student @ University of South Florida  
🔗 [Portfolio](https://iamdk25.github.io/3d_personal_portfolio/) • 🧠 [GitHub](https://github.com/Iamdk25) • 💼 [LinkedIn](https://www.linkedin.com/in/dkarmariya/)

[![GitHub stars](https://img.shields.io/github/stars/Iamdk25/Open-CV-Python-project?style=social)](https://github.com/Iamdk25/Open-CV-Python-project/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Iamdk25/Open-CV-Python-project?style=social)](https://github.com/Iamdk25/Open-CV-Python-project/network/members)
[![GitHub last commit](https://img.shields.io/github/last-commit/Iamdk25/Open-CV-Python-project)](https://github.com/Iamdk25/Open-CV-Python-project/commits/main)
![GitHub top language](https://img.shields.io/github/languages/top/Iamdk25/Open-CV-Python-project)
![License](https://img.shields.io/github/license/Iamdk25/Open-CV-Python-project)
