""" 章节4.5.3 多行子查询 """

import cx_Oracle as cx
from Oracle11gBase9787302458227.chapter04 import OptOracle

# 连接 Oracle 数据库
con_scott = cx.connect('scott', 'tiger', '127.0.0.1:1521/orcl')  # SCOTT 模式

# exp4_79：
# 【例 4.79】 在 emp 表中，查询不是销售部门（SALES）的员工信息
tableHead4_79 = ['EMPNO', 'ENAME', 'JOB']
sqlCase4_79 = "select EMPNO, ENAME, JOB " \
              "from EMP where DEPTNO IN " \
              "(select DEPTNO from DEPT where DNAME<>'SALES')"

# exp4_80：
# 【例 4.80】 在 emp 表中，查询工资大于10号部门的任意一个员工工资的其它部门的员工信息
tableHead4_80 = ['DEPTNO', 'ENAME', 'SAL']
sqlCase4_80 = "select DEPTNO, ENAME, SAL from EMP where SAL > any " \
              "(select SAL from EMP where DEPTNO = 10) and DEPTNO <> 10"

# exp4_81：
# 【例 4.81】 在 emp 表中，查询工资大于10号部门的任意一个员工工资的其它部门的员工信息
tableHead4_81 = ['DEPTNO', 'ENAME', 'SAL']
sqlCase4_81 = "select DEPTNO, ENAME, SAL from EMP where SAL > all " \
              "(select SAL from EMP where DEPTNO = 30)"

OptOracle.printData(con_scott, tableHead4_81, sqlCase4_81)  # 执行 exp4_81
