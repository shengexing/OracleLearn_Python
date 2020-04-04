""" 章节4.4.2 数字类函数 """

import cx_Oracle as cx
from Oracle11gBase9787302458227.chapter04 import OptOracle

# 连接 Oracle 数据库
con_scott = cx.connect('scott', 'tiger', '127.0.0.1:1521/orcl')  # SCOTT 模式

# exp4_69：
# 【例 4.69】 使用 cell() 函数返回3个指定小数的整数值
tableHead4_69 = ['ceil(7.3)', 'ceil(7)', 'ceil(-7.3)']
sqlCase4_69 = "select ceil(7.3), ceil(7), ceil(-7.3) from dual"

# exp4_70：
# 【例 4.70】 使用 round() 函数返回 PI 为两位小数的值
tableHead4_70 = ['round(3.1415926, 2)']
sqlCase4_70 = "select round(3.1415926, 2) from dual"

# exp4_71：
# 【例 4.71】 使用 power() 函数计算2的3次方的值
tableHead4_71 = ['power(2, 3)']
sqlCase4_71 = "select power(2, 3) from dual"

OptOracle.printData(con_scott, tableHead4_71, sqlCase4_71)  # 执行 exp4_71
