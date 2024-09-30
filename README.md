# Image Encryption and Decryption Tool

This Python project demonstrates a simple yet effective image encryption and decryption tool that manipulates pixel values. It allows users to encrypt and decrypt images by applying a mathematical transformation (shift) to each pixel based on a user-defined key.

Features

Image Encryption: The program encrypts an image by shifting pixel values using a user-supplied key.

Image Decryption: The tool can decrypt an encrypted image by reversing the pixel shift using the same key.

Handles images in a variety of formats such as PNG, JPEG, and BMP.

Ensures pixel values remain within the valid range [0-255] to avoid color distortion.

How It Works

Encryption:

The image encryption process adds the key to each pixel's value (in RGB format) and ensures the values wrap around within the 0-255 range using the modulo operation.

Decryption:

To decrypt an encrypted image, the program subtracts the key from each pixel's value and applies the modulo operation to maintain valid pixel values.

Example:
Assume an image pixel has a value of (150, 100, 50) and the key is 10:

Encryption: The new pixel values will be (160, 110, 60).

Decryption: Reversing the operation returns the pixel values to (150, 100, 50).

# Installation

1)Clone the repository to your local machine:

git clone https://github.com/your-username/Pixel_Manipulation_For_Image_Encryption.git

2)Install the required dependencies using pip:

pip install pillow numpy

3)Navigate to the project directory:

cd Pixel_Manipulation_For_Image_Encryption
