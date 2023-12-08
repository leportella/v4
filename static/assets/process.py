from os import listdir
from PIL import Image

files = listdir('/Users/leportella/src/lele/v4/static/assets/_img')

for file in files:
    filename = file.split(".")[0]
    print(f"Processing file {filename}")
    im = Image.open(f"/Users/leportella/src/lele/v4/static/assets/_img/{file}")

    im.thumbnail((500, 500))
    im.save(f"/Users/leportella/src/lele/v4/static/assets/img/cover/{filename}_thumb.jpg")
    print(f'Saved {filename}_thumb.jpg')

    im.thumbnail((1000, 600))
    im.save(f"/Users/leportella/src/lele/v4/static/assets/img/cover/{filename}_thumb@2x.jpg")
    print(f'Saved {filename}_thumb@2x.jpg')
