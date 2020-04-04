""" 章节4.3.5 多表关联查询 """

import cx_Oracle as cx
from Oracle11gBase9787302458227.chapter04 import OptOracle

# 连接 Oracle 数据库
con_scott = cx.connect('scott', 'tiger', '127.0.0.1:1521/orcl')

# exp4_51：
# 【例 4.51】 在 SCOTT 模式下，通过 DEPTNO（部门号）列来关联 emp 表和 dept 表，并检索这两个表中相关字段的信息
tableHead4_51 = ['员工编号', '员工名称', '部门']
sqlCase4_51 = "select e.empno as 员工编号, e.ename as 员工名称, d.dname as 部门 " \
              "from emp e, dept d " \
              "where e.deptno = d.deptno " \
              "and e.job = 'MANAGER'"

# exp4_52：
# 【例 4.52】 在 SCOTT 模式下，通过 deptno 字段来内连接 emp 表和 dept 表，并检索这两个表中相关字段的信息
tableHead4_52 = ['员工编号', '员工名称', '部门']
sqlCase4_52 = "select e.empno as 员工编号, e.ename as 员工名称, d.dname as 部门 " \
              "from emp e inner join dept d " \
              "on e.deptno = d.deptno"

# exp4_53：
# 【例 4.53】 首先使用 INSERT 语句在 emp 表中插入新记录（注意没有为 deptno 和 dname 列插入值，即它们的值为 null），
# 然后实现 emp 表和 dept 表之间通过 deptno 列进行左外连接
tableHead4_53 = ['empno', 'ename', 'job', 'deptno', 'dname']
sqlCase4_53 = "select e.empno, e.ename, e.job, d.deptno, d.dname " \
              "from emp e left join dept d " \
              "on e.deptno = d.deptno"

# exp4_54：
# 【例 4.54】 在 SCOTT 模式下，实现 emp 表和 dept 表之间通过 deptno 列进行右外连接
tableHead4_54 = ['empno', 'ename', 'job', 'deptno', 'dname']
sqlCase4_54 = "select e.empno, e.ename, e.job, d.deptno, d.dname " \
              "from emp e right join dept d " \
              "on e.deptno = d.deptno"

# exp4_55：
# 【例 4.55】 在 SCOTT 模式下，实现 emp 表和 dept 表之间通过 deptno 列进行完全连接
tableHead4_55 = ['empno', 'ename', 'job', 'deptno', 'dname']
sqlCase4_55 = "select e.empno, e.ename, e.job, d.deptno, d.dname " \
              "from emp e full join dept d " \
              "on e.deptno = d.deptno"

# exp4_56：
# 【例 4.56】 在 emp 表中检索工资（sal 字段）大于 2000 的记录，并实现 emp 表与 dept 表的自然连接
tableHead4_56 = ['empno', 'ename', 'job', 'dname']
sqlCase4_56 = "select empno, ename, job, dname " \
              "from emp natural join dept " \
              "where sal > 2000"

# exp4_57：
# 【例 4.57】 在 SCOTT 模式下，查询所用管理者所管理的下属员工信息
tableHead4_57 = ['上层管理者', '下属员工']
sqlCase4_57 = "select em2.ename 上层管理者, em1.ename as 下属员工 " \
              "from emp em1 left join emp em2 " \
              "on em1.mgr=em2.empno " \
              "order by em1.mgr"

# exp4_58：
# 【例 4.58】 在 SCOTT 模式下，通过交叉连接 dept 表和 emp 表，计算出查询结果的行数
tableHead4_58 = ['count(*)']
sqlCase4_58 = "select count(*) " \
              "from dept cross join emp"


OptOracle.printData(con_scott, tableHead4_58, sqlCase4_58)  # 执行 exp4_58
