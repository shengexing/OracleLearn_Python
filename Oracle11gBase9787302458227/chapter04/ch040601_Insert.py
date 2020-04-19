""" 章节4.6.1 插入数据 """

from Oracle11gBase9787302458227.chapter04 import OptOracle
import os

# 连接 Oracle 数据库
db_scott = OptOracle.connectDatabase('orcl', 'scott', 'tiger')  # SCOTT 模式
db_hr = OptOracle.connectDatabase('orcl', 'hr', 'hr')  # SCOTT 模式

# exp4_83：
# 【例 4.83】 在 dept 表中，使用 INSERT 语句添加一条记录
sqlSelect4_83 = "select * from DEPT where DEPTNO = 88"
sqlUpdate4_83 = "insert into DEPT(DEPTNO, DNAME, LOC) " \
                "values(88, 'design', 'beijing')"

# exp4_84：
# 【例 4.84】 在 HR 模式下，使用 desc 命令查看 jobs 表的结构和列的定义顺序，然后使用 insert 语句插入一条记录
sqlSelect4_84 = "select * from JOBS where JOB_ID = 'PRO'"
sqlUpdate4_84 = "insert into JOBS values('PRO','程序员', 5000, 10000)"

# exp4_85：
# 【例 4.85】 使用特定格式插入日期值
sqlSelect4_85 = "select * from EMP where EMPNO = 1356"
sqlUpdate4_85 = "insert into EMP(EMPNO, ENAME, JOB, HIREDATE) " \
                "values(1356, 'MARY', 'CLERK', to_date('1983-10-20', 'YYYY-MM-DD'))"

# exp4_86：
# 【例 4.86】 使用特定格式插入日期值
sqlSelect4_86 = "select * from DEPT where DEPTNO = 60"
sqlUpdate4_86 = "insert into DEPT values(60, 'MARKET', default)"

# 执行 exp4_86
print("exp4_86：更新数据之前")
OptOracle.printResult(OptOracle.selectDB(db_scott, sqlSelect4_86))
OptOracle.dmlDB(db_scott, sqlUpdate4_86)
print("exp4_86：更新数据之后")
OptOracle.printResult(OptOracle.selectDB(db_scott, sqlSelect4_86))

# 关闭数据库连接
db_scott.close()
db_hr.close()
