""" 章节4.5.4 关联子查询 """

import cx_Oracle as cx
from Oracle11gBase9787302458227.chapter04 import OptOracle

# 连接 Oracle 数据库
con_scott = cx.connect('scott', 'tiger', '127.0.0.1:1521/orcl')  # SCOTT 模式

# exp4_82：
# 【例 4.82】 在 emp 表中，使用 “关联子查询” 检索工资大于同职位的平均工资的员工信息
tableHead4_82 = ['EMPNO', 'ENAME', 'SAL']
sqlCase4_82 = "select EMPNO, ENAME, SAL " \
              "from EMP e " \
              "where SAL > (select avg(SAL) from EMP where JOB = e.JOB) " \
              "order by JOB"

OptOracle.printData(con_scott, tableHead4_82, sqlCase4_82)  # 执行 exp4_82
