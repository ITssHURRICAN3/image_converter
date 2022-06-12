from PIL import Image

image_1 = Image.open(r'C:\Users') #path to the image
im_1 = image_1.convert('RGB')
im_1.save(r'C:\Users\your_username\Desktop') #path where you want the image to get saved
