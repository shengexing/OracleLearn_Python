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

# exp4_37：
# 【例 4.37】 在 emp 表中，显示按照职位（job）分类（job 并没有包含在 SELECT 子句中）的每类员工的平均工资，
# 并且显示的结果是按照职位由小到大排列的
tableHead4_37 = ['avg(sal)']
sqlCase4_37 = "select avg(sal) " \
              "from emp " \
              "group by job"

# exp4_38：
# 【例 4.38】 使用 GROUP BY 进行多列分组。查询 emp 表，显示每个部门每种岗位的平均工资和最高工资
tableHead4_38 = ['deptno', 'job', 'avg(sal)', 'max(sal)']
sqlCase4_38 = "select deptno, job, avg(sal), max(sal) " \
              "from emp " \
              "group by deptno, job"

# exp4_39：
# 【例 4.39】 查询 emp 表，显示每个部门的部门号及工资总额，而且工资总额降序排列
tableHead4_39 = ['deptno', 'sum(sal)']
sqlCase4_39 = "select deptno, sum(sal) " \
              "from emp " \
              "group by deptno " \
              "order by sum(sal) desc"

# exp4_40：
# 【例 4.40】 在 emp 表中，首先通过分组的方式计算出每个部门的平均工资，然后再通过 HAVING 子句过滤出平均工资大于 2000 的记录信息
tableHead4_40 = ['部门编号', '平均工资']
sqlCase4_40 = "select deptno as 部门编号, avg(sal) as 平均工资 " \
              "from emp " \
              "group by deptno " \
              "having avg(sal) > 2000"

# exp4_41：
# 【例 4.41】 在 emp 表中，使用 ROLLUP 操作符，显示各部门每岗位的平均工资、每部门的平均工资、所用雇员的平均工资
tableHead4_41 = ['部门编号', '岗位', '平均工资']
sqlCase4_41 = "select deptno as 部门编号, job as 岗位, avg(sal) as 平均工资 " \
              "from emp " \
              "group by rollup(deptno, job)"

# exp4_42：
# 【例 4.42】 在 emp 表中，使用 CUBE 操作符，显示各部门各岗位的平均工资、部门的平均工资、岗位平均工资、所用雇员的平均工资
tableHead4_42 = ['部门编号', '岗位', '平均工资']
sqlCase4_42 = "select deptno as 部门编号, job as 岗位, avg(sal) as 平均工资 " \
              "from emp " \
              "group by cube(deptno, job)"

# exp4_43：
# 【例 4.43】 在 emp 表中，使用 GROUPING 函数确定统计结果所使用的列
tableHead4_43 = ['deptno', 'job', 'sum(sal)', 'grouping(deptno)', 'grouping(job)']
sqlCase4_43 = "select deptno, job, sum(sal), grouping(deptno), grouping(job) " \
              "from emp " \
              "group by rollup(deptno, job)"

# exp4_44：
# 【例 4.44】 在 ROLLUP 操作符中使用复合列，在 emp 表中显示特定部门特定岗位的工资总额以及所有雇员的工资总额
tableHead4_44 = ['deptno', 'job', 'sum(sal)']
sqlCase4_44 = "select deptno, job, sum(sal) " \
              "from emp " \
              "group by rollup((deptno, job))"

# exp4_45：
# 【例 4.45】 在 CUBE 操作符中使用复合列，在 emp 表中显示特定部门特定岗位的工资总额以及所有雇员的工资总额
tableHead4_45 = ['deptno', 'job', 'sum(sal)']
sqlCase4_45 = "select deptno, job, sum(sal) " \
              "from emp " \
              "group by cube((deptno, job))"

# exp4_46：
# 【例 4.46】 在 emp 表中，显示部门平均工资和岗位平均工资
tableHead4_46 = ['deptno', 'job', 'avg(sal)']
sqlCase4_46 = "select deptno, job, avg(sal) " \
              "from emp " \
              "group by grouping sets(deptno, job)"


OptOracle.printData(con_scott, tableHead4_46, sqlCase4_46)  # 执行 exp4_46
