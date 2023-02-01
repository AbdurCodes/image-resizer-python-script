from PIL import Image #pip install Pillow

def resize_your_image(width, height):
      
      image_address = "absolute or relative address of the image along with extension"
      image = Image.open(image_address)
      print("The original size of your image is",image.size)

      image_resize = image.resize((width, height))
      print("Image successfully resized to",image_resize.size)
      image_resize.save(f"r-img-{image_resize.size}.jpg")
      print("Image successfully saved")
      
print("Welcome to Image Resizer!")  

width=int(input("Plz enter the required width: "))
height=int(input("Plz enter the required height: "))

resize_your_image(width, height)
