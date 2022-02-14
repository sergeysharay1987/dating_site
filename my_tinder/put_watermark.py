from PIL import Image
from dating_site.settings import MEDIA_ROOT

image_path = F'{MEDIA_ROOT}/photos/%Y/%m/%d/%'


def put_watermark(image_path, watermark_path):
    global n
    base_image = Image.open(image_path)
    watermark_image = Image.open(watermark_path).convert('RGBA')
    datas = watermark_image.getdata()
    newData = []

    for item in datas:

        if 50 <= item[0] <= 255 and 50 <= item[1] <= 255 and 50 <= item[1] <= 255:

            newData.append((item[0], item[1], item[1], 0))
        else:

            newData.append((item[0], item[1], item[1], 150))
        n += 1


    watermark_image.putdata(newData)
    base_image.paste(watermark_image, box=(0, 150), mask=watermark_image)
    base_image.save(f'{os.getcwd()}/new_Screenshot_{n}.jpg')

put_watermark(image_path, f'{os.getcwd()}/имени-1.jpg')
