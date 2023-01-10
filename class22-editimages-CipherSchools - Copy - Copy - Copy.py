
# from pil import Image
img1=Image.open('"R:\CAMERA PICS\chotu_anime.jpg"')
enhancer=ImageEnhance.Sharpness(img1)
enhancer.enhance()
# img1.save("chotu.png")
# img1.show()
# MAX_SIZE =(250,250)
# img1.thumbnail(MAX_SIZE)
# img1.save("dog1small.jpg")

# for item in os.listdir():
          # if item.endswith(".jpg"):
                    # img1=Image.open(item)
                    # filename,extension = os.path.splitext(item)
                    # img1.save(f"{filename}")