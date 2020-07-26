import requests
import json
import base64

# 一、先使用easyDl得到弹窗中是哪类文字
url_token = "https://aip.baidubce.com/oauth/2.0/token"
data_token = {"grant_type":"client_credentials","client_id":"T781GL1xnxsk0jU6Mq6BXyZy","client_secret":"c24FbnnhndTQ5YfPbZIWH4WpnPNf9DUp"}
#由于post请求的习惯是在body中放入要传给服务器的数据，因此，这里的post方法采用了data参数，而不是params参数。然而，采用params参数也是可以的
resp = requests.post(url_token,data = data_token)
#resp是一个http响应对象，resp.text则是一个json格式的字符串.json.loads()方法可以将json字符串转为字典。
resp_dict = json.loads(resp.text)
#转为字典之后的好处就是，可以直接从键索引出值，access_token的获取相比用字符串处理要方便得多
access_token = resp_dict["access_token"]
print('access_token:    ',access_token)
#url_app = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/ios_update_word"
request_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/ios_update_word" + "?access_token=" + access_token


img=open("D:/转转/picture_set/ios_update/good/3_(480,854).jpg","rb").read()
img_str = base64.b64encode(img).decode()
# read()方法读取文件对象，读取的结果是二进制数据。
# base64是一种用64个可打印字符表示二进制数据的编码方式（但是这不意味着编码后的结果就变成了字符串。实际上，仍然是字节类型的二进制数据，
# 只不过用字符表示而已）因此，用b64encode()方法对上述文件流数据进行b64编码后，得到的结果数据类型是"bytes"，不是"str"。
# 要将base64编码之后的数据转成字符串，需要将其解码。而decode()方法能够对二进制数进行解码，将其转为字符串数据。
# img_str就是base64编码的字符串表示
#设置请求头的Content-Type参数为application/json这是easyDL的API要求的格式
head = {"Content-Type":"application/json"}
#easyDL的API要求post请求的数据格式必须是json字符串数据，因此，在正式请求之前，必须用json.dumps()方法将data_app这个字典转化为json字符串
data_app = {"image":img_str}
data_app_json = json.dumps(data_app)
response = requests.post(request_url,data = data_app_json,headers = head)
#print(response.text)

resp_dict=eval(response.text)
assisgned_pic_cate=resp_dict['results'][0]['name']

print('assisgned_pic_cate:  ',assisgned_pic_cate)

# 二、通过ocr找到对应文字的坐标





