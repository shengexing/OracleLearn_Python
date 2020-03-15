""" 章节4.3.3 分组查询 """

import cx_Oracle as cx
from Oracle11gBase9787302458227.chapter04 import OptOracle

# 连接 Oracle 数据库
con_scott = cx.connect('scott', 'tiger', '127.0.0.1:1521/orcl')

# exp4_35：
# 【例 4.35】 在 emp 表中，按照部门编号（deptno）和职务（job）列进行分组
tableHead4_35 = ['deptno', 'job']
sqlCase4_35 = "select deptno,job from emp group by deptno, job order by deptno"

# exp4_36：
# 【例 4.36】 在 emp 表中，使用 GROUP BY 子句对工资记录进行分组，
# 并计算平均工资（AVG）、所用工资的总和（SUM）以及最高工资（MAX）和各组的行数（COUNT）
tableHead4_36 = ['job', 'avg(sal)', 'sum(sal)', 'max(sal)', 'count(job)']
sqlCase4_36 = "select job, avg(sal), sum(sal), max(sal), count(job) from emp group by job"


OptOracle.printData(con_scott, tableHead4_36, sqlCase4_36)  # 执行 exp4_36
