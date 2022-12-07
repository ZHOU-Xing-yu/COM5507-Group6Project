import jieba
import wordcloud
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS

import matplotlib.pyplot as plt # 图像展示库
with open("详情页文本（clean).txt", encoding="utf-8") as f:
    s = f.read()
print(s)
ls = jieba.lcut(s)  # 生成分词列表
text = ' '.join(ls)  # 连接成字符串

stopwords ={ 'where', 'again', 'some', 'myself', 'whom', 'nor', "there's", 'if', 'against', "he'll", 'it', 'to', "we're", "they're", "we'd", 'and', 'or', 'hers', 'them', "isn't", "i'd", 'a', 'this', 'should', 'himself', 'shall', 'each', 'had', "who's", 'could', "don't", 'doing', 'of', 'be', "why's", 'other', 'have', 'http', 'otherwise', 'her', 'very', 'being', 'was', "where's", 'any', 'the', 'like', 'down', "i'm", 'both', "he's", 'just', 'at', 'you', 'during', "we'll", 'since', 'over', "she's", 'no', 'until', 'on', "couldn't", 'having', "hadn't", 'more', 'do', 'itself', 'same', "she'd", "weren't", "i'll", 'their', 'him', 'but', 'then', 'under', "that's", 'before', "he'd", 'up', 'after', 'out', "i've", "it's", 'because', 'his', 'we', "mustn't", 'they', "aren't", "won't", "wouldn't", 'are', "can't", "they've", 'for', 'why', 'am', "you'd", "here's", 'further', 'she', "you'll", "let's", "we've", 'those', 'yourselves', 'by', 'can', 'however', 'k', 'themselves', "doesn't", "haven't", 'only', 'from', "she'll", 'above', "shouldn't", 'than', 'too', 'did', 'your', 'ours', 'ought', 'with', 'into', 'ever', 'been', 'i', 'theirs', 'ourselves', "didn't", 'our', 'all', 'so', 'while', 'once', 'few', 'yourself', 'get', 'my', 'an', "they'd", 'herself', 'cannot', "you're", 'were', 'not', 'would', 'below', 'has', "they'll", 'does', 'that', 'most', 'also', 'he', 'com', 'these', 'who', "hasn't", 'what', 'as', 'me', 'else', "how's", 'in', 'own', 'through', "you've", 'therefore', 'when', 'between', "when's", 'there', 'off', 'such', "wasn't", 'which', 'www', 'yours', 'its', 'hence', "shan't", "what's", 'here', 'how', 'about', 'is','spam','now','applying','read','mention','see','post','completely',
             'avoid','applicants','candyshop','huamn','beta','feature','show','work','team','experience','company','companies','RNIEuOTMuMS4yMzUM','job','will','search','find','word','people','remote','RNjEUOTMuMS4yMZUM','xao','set','positon','human','teams','Apply','xa0','Requirement','knowledge','required','help'}

wc = wordcloud.WordCloud(font_path="/System/Library/Fonts/Helvetica.ttc",
                         width=1920,
                         height=1080,
                         stopwords=stopwords,
                         background_color = 'white',
                         max_words=200)
# msyh.ttc电脑本地字体，写可以写成绝对路径
wc.generate(text)  # 加载词云文本
wc.to_file("核心能力词云.png")  # 保存词云文件





