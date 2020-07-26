# import sys
# sys.path.append("/Users/xiaoheng/Downloads/meituan/ImageRecognitionAndClassification")
from ImageRecognition.get_color import get_main_tonal_value

#
image_path="/Users/xiaoheng/Downloads/meituan/kl_depth_performance_android/webview-tools/workspace/loadPics/iOS_支付页/2.png"
clusters=1

main_tonal_color = get_main_tonal_value(image_path, clusters)
