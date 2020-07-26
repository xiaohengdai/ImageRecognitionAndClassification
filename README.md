# **ImageRecognitionAndClassification**
##### **- ImageRecognition**
- 方法return_coor_by_img
  - 入参
    - param operating_system:哪一端的图片（android or ios）
    - widget_img_path:基准图（控件图）
    - param discern_img_path:全局图片（图片上是否有指定控件）的路径
    - param assign_area:为了提高识别率，可以指定将全局图片裁剪的一个区域
    - param confidence:指定识别的置信率
  - 出参
    - discern_img_can_recogn:图片是否能识别
    - rec_confidence:识别出来的置信度
    - position_x, position_y:识别出来后可点击的位置

 