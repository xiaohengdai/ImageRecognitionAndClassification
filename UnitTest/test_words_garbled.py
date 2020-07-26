# AI赋能一键自动检测：页面异常、控件异常、文本异常:https://blog.csdn.net/ciyiwa8779/article/details/100291057
#目前项目里的乱码识别主要是针对英文和字符类型，所以使用的是nltk库做分词，如果是主要对中文处理，使用结巴分词效果更好，或者用NLTK库中Sinica（中央研究院）提供的繁体中文语料库，from nltk.corpus import sinica_treebank 这样导入
import collections
from keras.models import Sequential

import nltk
# nltk.download('punkt')

maxlen = 0  # 句子最大长度 
word_freqs = collections.Counter()  # 词频 
num_recs = 0  #  样本数 
with open('/Users/xiaoheng/Downloads/meituan/ImageRecognitionAndClassification/UnitTest/WordsGarbled/train.txt', 'r+') as f:
    for line in f:
        print("line:",line)
        sentence=line
        # sentence = line.strip().split("t")
        # print("sentence:",sentence)
        words = nltk.word_tokenize(sentence.lower())
        print("words:",words)
        if len(words) > maxlen:
            maxlen=len(words)

        for word in words:
            word_freqs[word]+=1
            num_recs+=1



EMBEDDING_SIZE = 128
MAX_SENTENCE_LENGTH = 40
MAX_FEATURES = 2000
vocab_size = min(MAX_FEATURES,len(word_freqs)+2)

# model=Sequential()
# model.add(Embedding(vocab_size,EMBEDDING_SIZE,input_length=MAX_SENTENCE_LENGTH))
# model.add(LSTM(HIDDEN_LAYER_SIZE,dropout=0.2,recurrent_dropout=0.2))
# model.add(Dense(1) 
# model.add(Activation("sigmoid") 
# model.compile(loss="binary_crossentropy", optimizer="adam",metrics=["accuracy"]) 
# BATCH_SIZE = 32 
# NUM_EPOCHS = 10 
# model.fit(Xtrain, ytrain, batch_size=BATCH_SIZE, epochs=NUM_EPOCHS,validation_data=(Xtest, ytest) 
# model.save("garbled.h5");"