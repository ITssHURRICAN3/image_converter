from PIL import Image

image_1 = Image.open(r'C:\Users') #path alla foto
im_1 = image_1.convert('RGB')
im_1.save(r'C:\Users\Simone\Desktop\carta_identità.pdf') #path dove vuoi che vernga salvata la foto