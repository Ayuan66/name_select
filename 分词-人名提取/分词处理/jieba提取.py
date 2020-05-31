import jieba.posseg as pseg
import time

time_start = time.time()
print('开始运行')
name = []
with open('分词处理/人民的名义.txt') as file:
    for line in file.readlines():
        poss = pseg.cut(line)
        for word in poss:
            if word.flag == 'nr':
                name.append(word)
    file.close()

name = list(set(name))
new_file = open('jieba.txt', 'w', encoding='utf-8')
for i in range(len(name)):
    new_file.write(str(name[i]) + '\n')
new_file.close()
time_end = time.time()
print('总共耗时:', str(time_end-time_start) + 's')
print('运行结束')