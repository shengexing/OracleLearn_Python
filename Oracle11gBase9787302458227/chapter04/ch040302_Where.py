" 章节4.3.3 分组查询"

import cx_Oracle as cx

# 连接 Oracle 数据库
con_scott = cx.connect('scott', 'tiger', '127.0.0.1:1521/orcl')


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
sqlCase4_24 = "select empno, ename, job from emp where job like 'S%'"\

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
              "where dname like 'IT^_%' escape '^'" # 这里不使用 \ 来转义，因为字符串中 \ 也有转义的含义，需要写为 \\


cursor = con_scott.cursor()  # 创建游标
print(tableHead4_27) # 打印表头
cursor.execute(sqlCase4_27)  # 执行sql语句，可以替换不同的例子（93710）

# 遍历游标，打印数据
for result in cursor:
    print(result)

cursor.close()  # 关闭游标
con_scott.close()  # 关闭数据库连接