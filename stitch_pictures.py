from os import listdir
from PIL import Image


def stitch_pictures():
    # 获取当前文件夹中所有png图像
    im_list = [Image.open(fn) for fn in listdir() if fn.endswith('.png')]
    # 图片转化为相同的尺寸并存放到列表ims中
    ims = []
    for i in im_list:
        new_img = i.resize((1000, 667))
        ims.append(new_img)
    # 单幅图像尺寸
    width, height = ims[0].size
    # 创建空白长图
    result = Image.new(ims[0].mode, (width * len(ims), height))
    # 拼接图片
    for i, im in enumerate(ims):
        result.paste(im, box=(i * width, 0))
    # 保存图片
    result.save('res1.png')


if __name__ == '__main__':
    stitch_pictures()