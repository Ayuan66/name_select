# -*- coding: utf-8 -*-

import xmnlp
import time

time_start = time.time()

print("开始处理")
persons = []
with open('分词处理/人民的名义.txt') as f1:
    chapter = f1.read()
    for word, tag in xmnlp.tag(chapter):
        if tag == "nr":
            print(word)
            persons.append(word)
f1.close()

persons = list(set(persons))
with open('xmnlp.txt', "w") as wf:
    for word in persons:
        wf.writelines("{}\n".format(word))
wf.close()
time_end = time.time()
print('总共耗时:', str(time_end-time_start) + 's')
print('处理完成!')




