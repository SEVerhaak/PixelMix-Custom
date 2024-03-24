import matplotlib.pylab as plt
from API import transfer_style
from PIL import Image

# Path of the downloaded pre-trained model or 'model' directory
model_path = r"/Users/basverhaak/Documents/AI/PixelMix-main/model"

# NOTE : Works only for '.jpg' and '.png' extensions,other formats may give error
content_image_path = r"/Users/basverhaak/Documents/TEST IMAGES/frame-000000.jpg"
style_image_path = r"/Users/basverhaak/Downloads/Van_Gogh_-_Starry_Night_-_Google_Art_Project (1).jpg"

content_image_path = Image.open(content_image_path)
style_image_path = Image.open(style_image_path)

img = transfer_style(content_image_path,style_image_path,model_path)
# Saving the generated image
plt.imsave('stylized_image.jpeg',img)
plt.imshow(img)
plt.show()