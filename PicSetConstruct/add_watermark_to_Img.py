from PIL import Image


watermark = Image.open("D:/pythonProject/ImageRecognitionAndClassification/UnitTest/ImgReco/watermark.jpg")
imageFile = Image.open("D:/pythonProject/ImageRecognitionAndClassification/UnitTest/ImgReco/small_tool_1.png")
layer = Image.new('RGBA', imageFile.size, (0,0,0,0))  #使用给定的变量mode和size生成新的图像
print('layer:   ',layer)
layer.paste(watermark, (imageFile.size[0]-500, imageFile.size[1]-100))  #将watermark粘贴在layer上
out=Image.composite(layer,imageFile,layer)  #复合类使用给定的两张图像及mask图像作为透明度，插值出一张新的图像。变量mask图像的模式可以为“1”，“L”或者“RGBA”。所有图像必须有相同的尺寸。
out.save(r"D:/pythonProject/ImageRecognitionAndClassification/UnitTest/ImgReco/watermark_res.png")