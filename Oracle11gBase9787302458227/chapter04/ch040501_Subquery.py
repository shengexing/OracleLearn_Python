""" 章节4.5.1 什么是子查询 """

import cx_Oracle as cx
from Oracle11gBase9787302458227.chapter04 import OptOracle

# 连接 Oracle 数据库
con_scott = cx.connect('scott', 'tiger', '127.0.0.1:1521/orcl')  # SCOTT 模式

# exp4_77：
# 【例 4.77】 在 SCOTT 模式下，使用 emp 表中查询部门名称（dname）为 “RESEARCH” 的员工信息
tableHead4_77 = ['员工总数', '平均工资']
sqlCase4_77 = "select empno, ename, job from EMP " \
              "where deptno=(select deptno from DEPT " \
              "where dname='RESEARCH')"

OptOracle.printData(con_scott, tableHead4_77, sqlCase4_77)  # 执行 exp4_77
