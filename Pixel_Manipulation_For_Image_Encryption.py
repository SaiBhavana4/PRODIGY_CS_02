from PIL import Image
import numpy as np

def modify_pixels(image_array, key, mode='encrypt'):
    """
    Modifies the pixel values of the image for encryption or decryption.

    Args:
        image_array: Numpy array of the image pixel values.
        key: An integer key used to shift pixel values.
        mode: 'encrypt' or 'decrypt' to specify the operation.

    Returns:
        modified_array: Numpy array of the modified pixel values.
    """
    if mode == 'encrypt':
        modified_array = (image_array + key) % 256  # For encryption, add the key
    elif mode == 'decrypt':
        modified_array = (image_array - key) % 256  # For decryption, subtract the key

    return modified_array

def process_image(image_path, key, mode):
    """
    Loads the image, processes the pixel values (encrypt or decrypt), and returns the result.

    Args:
        image_path: Path to the image file.
        key: Key to modify pixel values.
        mode: 'encrypt' or 'decrypt' to specify the operation.

    Returns:
        Image object with modified pixel values.
    """
    image = Image.open(image_path)  # Open image
    image_array = np.array(image)  # Convert to array

    # Modify the pixels based on the mode
    modified_array = modify_pixels(image_array, key, mode)
    
    # Convert back to an image object
    processed_image = Image.fromarray(modified_array.astype(np.uint8))
    
    return processed_image

def save_processed_image(image, file_path):
    """
    Saves the processed image to the specified file path.

    Args:
        image: The image object to be saved.
        file_path: Path to save the processed image.
    """
    image.save(file_path)
    print(f"Image successfully saved to {file_path}")

def main():
    """
    Main function to handle user input and perform image encryption or decryption.
    """
    print("=== Image Encryption/Decryption ===")
    action = input("Would you like to (1) Encrypt or (2) Decrypt an image? Enter 1 or 2: ")

    if action not in ['1', '2']:
        print("Invalid option. Exiting.")
        return

    image_path = input("Enter the path to the image: ")
    key = int(input("Enter the encryption/decryption key (integer): "))

    if action == '1':
        mode = 'encrypt'
        result_image = process_image(image_path, key, mode)
        save_path = input("Enter the path to save the encrypted image: ")
    else:
        mode = 'decrypt'
        result_image = process_image(image_path, key, mode)
        save_path = input("Enter the path to save the decrypted image: ")

    # Save the processed image
    save_processed_image(result_image, save_path)

if __name__ == "__main__":
    main()
