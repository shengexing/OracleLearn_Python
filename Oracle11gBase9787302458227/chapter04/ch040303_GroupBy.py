" 章节4.3.3 分组查询"

import cx_Oracle as cx

''' 【例 4.35】 在 emp 表中，按照部门编号（deptno）和职务（job）列进行分组 '''


def case4_35():
    sqlStr = "select deptno,job from emp group by deptno, job order by deptno"
    return sqlStr


''' 主逻辑-执行 SQL 语句 '''

# 连接 Oracle 数据库
con = cx.connect('scott', 'tiger', '127.0.0.1:1521/orcl')

cursor = con.cursor()  # 创建游标
cursor.execute(case4_35())  # 执行sql语句，可以替换不同的例子（93710）

# 遍历游标，打印数据
for result in cursor:
    print(result)

cursor.close()  # 关闭游标
con.close()  # 关闭数据库连接
