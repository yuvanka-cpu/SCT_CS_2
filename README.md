Image Encryption Using XOR Pixel Manipulation
This project implements an image encryption and decryption system based on the XOR operation performed on each pixel.
The goal is to securely transform an image into a scrambled version that cannot be recognized without the correct key, and then reverse the process to get the original image back.

This task is part of SkillCraft Technology Internship – Task 2.

🔐 How the Encryption Works
Digital images consist of pixels, and each pixel stores three color values:

We use the XOR (Exclusive OR) operation to modify each color channel:

To decrypt, we apply XOR again with the same key:
XOR is reversible, meaning the same key must be used to decrypt successfully.

This causes the encrypted image to appear fully scrambled and unreadable.

📂 Project File Structure
mage-encryption/ │ ├── encrypt.py # Encrypts the image using XOR key ├── decrypt.py # Decrypts the encrypted image ├── original.png # Example input image (you can use your own) └── README.md # Project documentation (this file)

✅ Requirements
Make sure you have:

Python 3 installed
Install Pillow (Python Imaging Library):

If you're using a virtual environment (recommended):
🛠 Setup (Mac / Windows / Linux)
Place your input image (e.g., original.png) in the project folder.
Ensure encrypt.py and decrypt.py are saved in the same folder.
Open Terminal / CMD inside the project directory.
Run the scripts as shown below.
▶️ Usage Instructions
1) Encrypt an Image
Run the encryption script:

You will be prompted to enter:

Prompt	Meaning	Example Input
Input image path	The image you want to protect	original.png
Output encrypted image name	Name for the scrambled image	encrypted.png
Encryption key (0–255)	A secret number used to lock & unlock image	120
After running, you will get an encrypted (scrambled) image that cannot be understood by viewing.

2) Decrypt an Image
Run the decryption script:

You will be prompted to enter:

Prompt	Meaning	Example Input
Encrypted image path	The scrambled image	encrypted.png
Output decrypted image name	Name for restored image	decrypted.png
Same encryption key	Must match the key used during encryption	120
When the correct key is used, the original image will be restored perfectly.

✅ Summary
Action	Command	Result
Encrypt Image	python3 encrypt.py	Produces encrypted.png
Decrypt Image	python3 decrypt.py	Produces decrypted.png
⚠️ Important Notes
The same key must be used for both encryption and decryption.
Key range: 0–255
Works with PNG, JPG, JPEG, BMP, etc.
If the key is forgotten, image cannot be restored.
🎯 Purpose of Project
Understanding pixel-level image processing.
Learning reversible cryptographic transformations.
Implementing basic security concepts in Python.
🧑‍💻 Author / Internship Info
This project is completed as part of:

SkillCraft Technology Internship — Task 2
