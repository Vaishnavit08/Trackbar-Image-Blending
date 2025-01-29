
# 🖼 Image Blending with Trackbars

## 🌟 Overview
This project demonstrates image blending using OpenCV and trackbars. Users can dynamically adjust the alpha value to blend two images using OpenCV's cv2.addWeighted() function.

## ✨ Features
- 📷 Load and resize two images (krishna.jpg and radha.jpg).
- 🖥 Display both images separately.
- 🎛 Use a trackbar to control the blending ratio between the two images.
- 🔄 Implement an ON/OFF switch for blending.
- ⏹ Press 'v' to exit the application.

## 🛠 Requirements
Ensure you have the following dependencies installed before running the script:

- 🐍 Python 3.x
- 🖼 OpenCV (cv2)
- 🔢 NumPy (numpy)

You can install them using:
```bash
pip install opencv-python numpy
```

## 🚀 Usage
1. 📂 Place krishna.jpg and radha.jpg in the same directory as the script.
2. ▶ Run the script:
   ```bash
   python script.py
   ```
3. 🎚 Adjust the blending effect using the trackbar:
   - Move the alpha trackbar to change the blending ratio.
   - Use the switch trackbar to enable/disable blending.
4. 🏁 Press 'v' to close the application.

## 📝 Code Explanation
- *📥 Loading Images:* The script loads two images and resizes them to the same dimensions.
- *⚙ Trackbars:* A trackbar is created to control the alpha value (blending ratio) and a switch to enable or disable blending.
- *🖌 Blending Operation:* When the switch is ON, cv2.addWeighted() blends the images based on the alpha value.
- *❌ Exit Condition:* Pressing 'v' closes the OpenCV windows.

## 📸 Screenshots
![image](https://github.com/user-attachments/assets/2ae48c49-25a5-43b6-97c3-bb0a2360712e)


## 🤝 Contributing
Feel free to fork the repository and submit pull requests for improvements! 🚀

## 📜 License
This project is licensed under the MIT License.
```

