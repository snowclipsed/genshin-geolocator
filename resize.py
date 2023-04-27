from PIL import Image
import os



# folders = ["images/starsnatch_cliff","images/stormbearer_mountains", "images/stormbearer_point", "images/thousand_winds_temple", "images/whispering_woods", "images/windrise"]
folders = ["images/starfell_lake"]
background = (255,255,255)

#resize function
class resize:
        
    def resize(folderlist, bgcolor = None, savepath = None):

        for folder in folderlist:
            for file in enumerate(os.listdir(folder)):
                path = f"{folder}/{file[1]}"
                print(path)
                image = Image.open(path)
                width, height = image.size

                if width == height:
                    image.save(f"{folder}/{file[1]}")
                
                elif width > height:
                    new_image = Image.new(image.mode, (width, width), bgcolor)
                    new_image.paste(image, (0, (width - height)//2 ))
                    new_image.save(f"{folder}/{file[1]}")
                
                else:
                    new_image = Image.new(image.mode, (height, height), bgcolor)
                    new_image.paste(image, (0, (height-width)//2 ))
                    new_image.save(f"{folder}/{file[1]}")

img = resize.resize(folders, background)
# img.save("images/falcon_coast/falcon_coast_1.png", quality = 95)