# 安装：pip install googletrans==4.0.0-rc1
from googletrans import Translator

def x(a):
    translator = Translator()
    c = translator.translate(a, dest='en').text
    # 转换为蛇形命名：sales total -> sales_total
    return c.lower().replace(' ', '_')

print(x("销售总额"))  # sales_total
print(x("用户列表"))  # user_list