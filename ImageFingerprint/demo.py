from PIL import Image

import imagehash


def img(img_path):
    """
    图片哈希（类似：4f999cc90979704c）
    :param img_path: 图片路径
    :return: <class 'imagehash.ImageHash'>
    """
    img1 = Image.open(img_path)
    res = imagehash.dhash(img1)
    return res


def hamm_img(res1, res2):
    """
    汉明距离，汉明距离越小说明越相似，等 0 说明是同一张图片，大于10越上，说明完全不相似
    :param res1:
    :param res2:
    :return:
    """
    str1 = str(res1)  # <class 'imagehash.ImageHash'> 转成 str
    str2 = str(res2)
    num = 0  # 用来计算汉明距离
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            num += 1
    return num


if __name__ == '__main__':
    img_path1 = '/Users/xiaoheng/Downloads/meituan/ImageRecognitionAndClassification/ImageFingerprint/standard.jpg'
    img_path2 = '/Users/xiaoheng/Downloads/meituan/ImageRecognitionAndClassification/ImageFingerprint/standard2.jpg'
    # print("")
    d_img_path1=img(img_path1)
    d_img_path2=img(img_path2)
    print("d_img_path1:"+str(d_img_path1))
    print("d_img_path2:" + str(d_img_path2))
    res = hamm_img(d_img_path1,d_img_path2 )
    print('汉明距离是:', res)
