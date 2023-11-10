import pytesseract
import PIL.Image as Image
import pyautogui

image_path = r"C:\Users\Jana\Pictures\Test Text.PNG"

def copy_text_from_image(image_path):
    """Copies text from an image.
    Args:
        image_path: The path to the image file.
    Returns:
        A string containing the text extracted from the image.
    """
    with Image.open(image_path) as image:
        text = pytesseract.image_to_string(image)
    return text
with Image.open(image_path.encode("utf-8"), "r") as image:
    text = pytesseract.image_to_string(image)

text = copy_text_from_image(image_path)

print(text)