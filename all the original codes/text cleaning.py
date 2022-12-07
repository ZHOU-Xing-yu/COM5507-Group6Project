import string
import os
import demoji
import re
import pandas as pd

def replacetext(search_text, replace_text):
    # 以读写模式打开文件
    with open('详情页文本.txt', 'r+') as f:
        # 读取文件数据并将其存储在文件变量中
        file = f.read()
        # 用文件数据中的字符串替换模式
        file = re.sub(search_text, replace_text, file)
        # 设置位置到页面顶部插入数据
        f.seek(0)
        # 在文件中写入替换数据
        f.write(file)
        # 截断文件大小
        f.truncate()
    # 返回“文本已替换”字符串
    return "文本已替换"
# 创建一个变量并存储我们要搜索的文本
search_text = "When applying, mention the word CANDYSHOP when applying to show you read the job post completely. This is a beta feature to avoid spam applicants. Companies can search these words to find applicants that read this and see they are human RNjEuOTMuMS4yMzUMApply now:"
# 创建一个变量并存储我们要更新的文本
replace_text = ""
# 调用replacetext函数并打印返回的语句
print(replacetext(search_text, replace_text))
pattern = re.compile(u'| · | • |• |')#\t|\n|
# 将符合模式的字符去除，re.sub代表替换，把符合pattern的替换为空
punctuation_string = string.punctuation
file_path = "详情页文本.txt"
final_file = "详情页文本（clean).txt"
# 如果final_file文件存在，则删除
if os.path.exists(final_file):
    os.remove(final_file)

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # 替换表情符号为 空
        rap_line = demoji.replace(line, "")
        for i in punctuation_string:
            rap_line = rap_line.replace(i, '')
        rap_line = re.sub(pattern, '', rap_line)
        # 写入文件
        with open(final_file, 'a', encoding='utf-8') as f:
            f.write(rap_line)








