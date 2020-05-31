import time
import time

time_start = time.time()

from aip import AipNlp


def get_chinese_name(text):
    """
    :param text: 中文字符串
    :return: 人名
    """

    """识别人名"""
    APP_ID = '20091238' # 服务器名称
    API_KEY = 'dekcbm5ZUP6iXn29BkfWDGvv' # 服务器序号
    SECRET_KEY = '1MOLtq8PvU15Qrtz5UGiyR7v0MWSkS1S' # 服务器密码

    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

    text = str(text.encode('gbk', 'ignore'), encoding='gbk')  # ignore忽略无法编码的字符,如果不加这个会报错。

    # 设置请求间隔,免费版的QPS限制为2
    time.sleep(1)

    # 调用词法分析的返回结果
    # print(client.lexer(text))

    """ 调用词法分析 """
    for i in client.lexer(text)['items']:
        # 若字符串中有人名就返回人名
        if i['ne'] == 'PER':
            return i['item']

    return i['item']

# text = "侯亮平得知航班无限期延误，急得差点跳起来。他本打算坐最后一班飞机赶往H省，协调指挥抓捕京州市副市长丁义珍的行动，这下子计划全落空了。"

print('开始运行')

with open('分词处理/人民的名义.txt') as file:
    text = file.readlines()
    lines = []
    name = []
    for line in text:
        if line != '\n':
            lines.append(line)
    # print(lines)
    for i in range(len(lines)):
        result = get_chinese_name(lines[i])
        print(result)
        name.append(result)
name = list(set(name))
print(name)
new_file = open('baidu.txt', 'w', encoding='utf-8')
for i in range(len(name)):
    new_file.write(str(name[i]) + '\n')
new_file.close()
# print(get_chinese_name(text))
time_end = time.time()
print('总共耗时:', str(time_end-time_start) + 's')
print('运行结束')
