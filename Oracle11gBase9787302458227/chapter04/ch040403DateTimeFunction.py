""" 章节4.4.3 时间日期类函数 """

import cx_Oracle as cx
from Oracle11gBase9787302458227.chapter04 import OptOracle

# 连接 Oracle 数据库
con_scott = cx.connect('scott', 'tiger', '127.0.0.1:1521/orcl')  # SCOTT 模式

# exp4_72：
# 【例 4.72】 使用 sysdate() 函数返回系统当前的日期
tableHead4_72 = ['系统时间']
sqlCase4_72 = "select sysdate as 系统时间 from dual"

# exp4_73：
# 【例 4.73】 使用 ADD_MONTHS 函数在当前的日期下加上6个月，并显示其值
tableHead4_73 = ['add_months(sysdate, 6)']
sqlCase4_73 = "select add_months(sysdate, 6) from dual"

OptOracle.printData(con_scott, tableHead4_73, sqlCase4_73)  # 执行 exp4_73
