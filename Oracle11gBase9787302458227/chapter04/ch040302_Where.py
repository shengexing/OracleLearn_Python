""" 章节4.3.3 分组查询 """

import cx_Oracle as cx
from Oracle11gBase9787302458227.chapter04 import OptOracle

# 连接 Oracle 数据库
con_scott = cx.connect('scott', 'tiger', '127.0.0.1:1521/orcl')  # SCOTT 模式
con_hr = cx.connect('hr', 'hr', '127.0.0.1:1521/orcl')  # HR 模式

# exp4_22：
# 【例 4.22】 在 SCOOT 模式下，查询 emp 表中工资（sal）大于 1500 的数据记录
tableHead4_22 = ['empno', 'ename', 'sal']
sqlCase4_22 = "select empno, ename, sal from emp where sal > 1500"

# exp4_23：
# 【例 4.23】 在 SCOOT 模式下，使用 all 关键字过滤工资（sal）同时不等于 3000、950 和 800 的员工记录
tableHead4_23 = ['empno', 'ename', 'sal']
sqlCase4_23 = "select empno, ename, sal from emp where sal <> all(3000, 950, 800)"

# exp4_24：
# 【例 4.24】 在 emp 表中，使用 LIKE 关键字匹配以字母 S 开头的任意长度的员工名称
tableHead4_24 = ['empno', 'ename', 'job']
sqlCase4_24 = "select empno, ename, job from emp where job like 'S%'" \
 \
    # exp4_25：
# 【例 4.25】 在 emp 表中，查询工作是 SALESMAN 的员工姓名，但是不记得 SALESMAN 的准确拼写，
# 但还记得它的第一个字符是 S ，第三个字符是 L ，第五个字符是 S
tableHead4_25 = ['empno', 'ename', 'job']
sqlCase4_25 = "select empno, ename, job from emp where job like 'S_L_S%'"

# exp4_26：
# 【例 4.26】 在 emp 表中，要显示在 1981 年雇用的所用员工的信息
tableHead4_26 = ['empno', 'ename', 'job', 'hiredate']
sqlCase4_26 = "select empno, ename, job, hiredate " \
              "from emp " \
              "where hiredate like '%81'"

# exp4_27：
# 【例 4.27】 在 emp 表中，要显示在 1981 年雇用的所用员工的信息
tableHead4_27 = ['deptno', 'dname', 'loc']
sqlCase4_27 = "select * " \
              "from dept_temp " \
              "where dname like 'IT^_%' escape '^'"  # 这里不使用 \ 来转义，因为字符串中 \ 也有转义的含义，需要写为 \\

# exp4_28：
# 【例 4.28】 在 emp 表中，使用 IN 关键字查询职务为 PRESIDENT、MANAGER 和 ANALYST 中任意一种员工信息
tableHead4_28 = ['empno', 'ename', 'job']
sqlCase4_28 = "select empno, ename, job from emp where job in ('PRESIDENT', 'MANAGER', 'ANALYST')"

# exp4_29：
# 【例 4.29】 在 emp 表中，使用 NOT IN 关键字查询职务不在指定目标列表 (PRESIDENT, MANAGER, ANALYST) 范围内的员工信息
tableHead4_29 = ['empno', 'ename', 'job']
sqlCase4_29 = "select empno, ename, job from emp where job not in ('PRESIDENT', 'MANAGER', 'ANALYST')"

# exp4_30：
# 【例 4.30】 在 emp 表中，使用 BETWEEN...AND 关键字查询工资（sal）在 2000 到 3000 之间的员工信息
tableHead4_30 = ['empno', 'ename', 'sal']
sqlCase4_30 = "select empno, ename, sal from emp where sal between 2000 and 3000"

# exp4_31：
# 【例 4.31】 在 emp 表中，使用 NOT...BETWEEN...AND 关键字查询工资（sal）不在 1000 到 3000 之间的员工信息
tableHead4_31 = ['empno', 'ename', 'sal']
sqlCase4_31 = "select empno, ename, sal from emp where sal not between 1000 and 3000"

# exp4_32：
# 【例 4.32】 在 HR 模式下，使用 IS NULL 关键字过滤出 locations 表中省份或州（state_province）的名称为空值的街道地址信息
tableHead4_32 = ['street_address']
sqlCase4_32 = "select street_address from locations where state_province is null"

# exp4_33：
# 【例 4.33】 在 emp 表中，使用 AND 运算符查询工资（sal）在 2000 到 3000 之间的员工信息
tableHead4_33 = ['empno', 'ename', 'sal']
sqlCase4_33 = "select empno, ename, sal from emp where sal >= 2000 and sal <= 3000"

# exp4_34：
# 【例 4.34】 在 emp 表中，使用 OR 运算符查询工资（sal）小于 2000 或工资大于 3000 的员工信息
tableHead4_34 = ['empno', 'ename', 'sal']
sqlCase4_34 = "select empno, ename, sal from emp where sal < 2000 or sal > 3000"


OptOracle.printData(con_scott, tableHead4_34, sqlCase4_34)  # 执行 exp4_34
