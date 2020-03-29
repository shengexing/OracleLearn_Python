""" 章节4.3.4 排序查询 """

import cx_Oracle as cx
from Oracle11gBase9787302458227.chapter04 import OptOracle

# 连接 Oracle 数据库
con_scott = cx.connect('scott', 'tiger', '127.0.0.1:1521/orcl')

# exp4_47：
# 【例 4.47】 在 SCOTT 模式下，检索 emp 表中的所有数据，并按照部门编号（deptno）、员工编号（empno）排序
tableHead4_47 = ['deptno', 'empno', 'ename']
sqlCase4_47 = "select deptno, empno, ename from emp order by deptno, empno"

# exp4_48：
# 【例 4.48】 查询 emp 表中员工的年工资，并按照年工资降序排列
tableHead4_48 = ['empno', 'ename', 'Annual Salary']
sqlCase4_48 = "select empno, ename, sal*12 \"Annual Salary\" " \
              "from emp " \
              "order by 3 desc"

# exp4_49：
# 【例 4.49】 使用非选择列表列进行排序的方法，按工资降序显示员工名
tableHead4_49 = ['ename']
sqlCase4_49 = "select ename from emp order by sal desc"

# exp4_50：
# 【例 4.50】 查询 emp 表，按照部门号升序工资降序显示雇员名、部门号和工资
tableHead4_50 = ['ename', 'deptno']
sqlCase4_50 = "select ename, deptno, sal " \
              "from emp " \
              "order by deptno, sal desc"


OptOracle.printData(con_scott, tableHead4_50, sqlCase4_50)  # 执行 exp4_50
