import logging   # 日志模块
import datetime   # 时间模块
import os

# 设置日志存放路径
path = '.\\log\\'
if(not os.path.exists(path)):
    os.mkdir(path)

# 获取今天的日期 格式2019-08-01
today_date = str(datetime.date.today())

# 定义日志
logging.basicConfig(filename = path + 'log_' + today_date + '.txt', level = logging.DEBUG, filemode = 'a', format = '【%(asctime)s】 【%(levelname)s】 >>>  %(message)s', datefmt = '%Y-%m-%d %H:%M')

# 清理上个月的日志
def clean_log():
    global path
    global today_date

    # 遍历目录下的所有日志文件 i是文件名
    for i in os.listdir(path):
        file_path = path + i    # 生成日志文件的路径

        # 获取日志的年月，和今天的年月
        today_m = int(today_date[5:7])   # 今天的月份
        m = int(i[9:11])   # 日志的月份
        print(m)
        today_y = int(today_date[0:4])   # 今天的年份
        y = int(i[4:8])   # 日志的年份
        print(y)

        # 对上个月的日志进行清理，即删除。
        if(m < today_m):
            if(os.path.exists(file_path)):   # 判断生成的路径对不对，防止报错
                os.remove(file_path)   # 删除文件
        elif(y < today_y):
            if(os.path.exists(file_path)):
                os.remove(file_path)
