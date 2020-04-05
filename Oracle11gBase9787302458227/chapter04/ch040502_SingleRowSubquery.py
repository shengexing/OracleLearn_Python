""" 章节4.5.2 单行子查询 """

import cx_Oracle as cx
from Oracle11gBase9787302458227.chapter04 import OptOracle

# 连接 Oracle 数据库
con_scott = cx.connect('scott', 'tiger', '127.0.0.1:1521/orcl')  # SCOTT 模式

# exp4_78：
# 【例 4.78】 在 emp 表中，查询出既不是最高工资，也不是最低工资的员工信息
tableHead4_78 = ['EMPNO', 'ENAME', 'SAL']
sqlCase4_78 = "select EMPNO, ENAME, SAL from EMP " \
              "where SAL > (select min(SAL) from EMP) " \
              "and SAL < (select max(SAL) from EMP)"

OptOracle.printData(con_scott, tableHead4_78, sqlCase4_78)  # 执行 exp4_78
