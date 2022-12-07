import openpyxl
import pandas as pd
stu_num=[]
workbook1=openpyxl.load_workbook(r'/Users/zhouxingyu/Desktop/results/joblinks.xlsx')
#选定目标sheet
worksheet1 = workbook1.active
for cell in worksheet1['A']:
    #print(cell.value)
    stu_num.append(cell.value)
    for item in stu_num:
          if "URLS" in item:
             stu_num.remove(item)
#print(stu_num)#这里用循环把A列每个cell的值写入开始定义的空列表
se = 'https://web3.career'+pd.Series(stu_num)
print(se)
se.to_excel('/Users/zhouxingyu/Desktop/PYTHONSTUDY/joblinksnew.xlsx',index=True,header=None)



