from PIL import Image, ImageEnhance, ImageFilter

import os
from tqdm import tqdm

# folder path
dir_path = r"./data/coco"
readpath = dir_path+"/val2014/"
writepath = dir_path+"/val2014(1)/"
# list to store files
res = []
# Iterate directory
for file in os.listdir(readpath):
    # check only text files
    if file.endswith('.jpg'):
        res.append(file)



for file in tqdm(res):
    img = Image.open(readpath + file)
    filter = ImageEnhance.Brightness(img)
    img2 = filter.enhance(1.5)
    name = file.split(".jpg")
    name = name[0]
    img2.save(writepath + name + "_bright.jpg") 
    img2 = filter.enhance(0.5)
    img2.save(writepath + name + "_dark.jpg")
    img2 = img.rotate(45)
    img2.save(writepath + name + "_rotated1.jpg")
    img2 = img.rotate(315)
    img2.save(writepath + name + "_rotated2.jpg")
    img.save(writepath + name + '.jpg')


# rotate image
# img2 = img.rotate(45)
# img2.save("rotate.jpg")


#img2.show()

