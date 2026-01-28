'''
打开文件
使用readline读取文件第一行
while readline返回的不是一个空字符串时，打印该行内容，并继续读取下一行
    处理从文件中刚刚读取的数据项
    使用readline从文件中读取下一行
关闭文件
'''

def main():
    sales_file = open("sales.txt", "r")

    line = sales_file.readline()

    while line != "":
        amount = float(line)

        print(f'{amount:.2f}')
        line = sales_file.readline()
    sales_file.close()

if __name__=="__main__":
    main()