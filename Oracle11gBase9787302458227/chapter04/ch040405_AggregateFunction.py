""" 章节4.4.5 聚合类函数 """

import cx_Oracle as cx
from Oracle11gBase9787302458227.chapter04 import OptOracle

# 连接 Oracle 数据库
con_scott = cx.connect('scott', 'tiger', '127.0.0.1:1521/orcl')  # SCOTT 模式

# exp4_76：
# 【例 4.76】 在 SCOTT 模式下，使用 count() 函数计算员工总数，使用 avg() 函数计算平均工资
tableHead4_76 = ['员工总数', '平均工资']
sqlCase4_76 = "select count(EMPNO) as 员工总数, round(avg(sal), 2) as 平均工资 from EMP"

OptOracle.printData(con_scott, tableHead4_76, sqlCase4_76)  # 执行 exp4_76
