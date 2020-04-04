""" 章节4.4.1 字符类函数 """

import cx_Oracle as cx
from Oracle11gBase9787302458227.chapter04 import OptOracle

# 连接 Oracle 数据库
con_scott = cx.connect('scott', 'tiger', '127.0.0.1:1521/orcl')  # SCOTT 模式
con_hr = cx.connect('hr', 'hr', '127.0.0.1:1521/orcl')  # HR 模式

# exp4_59：
# 【例 4.59】 分别求得字符“Z、H、D和空格”的 ASCII 值
tableHead4_59 = ['Z', 'H', 'D', 'SPACE']
sqlCase4_59 = "select ascii('Z') Z, ascii('H') H, ascii('D') D, ascii(' ') space " \
              "from DUAL"

# exp4_60：
# 【例 4.60】 对于例 4.59 中求得的 ASCII 值， 使用 CHR 函数再返回其对应的字符
tableHead4_60 = ['CH', 'CH', 'CH', 'S']
sqlCase4_60 = "select chr(90), chr(72), chr(68), chr(32) S from DUAL"

# exp4_61：
# 【例 4.61】 使用 concat() 函数连接 “Hello” 和 “World” 两个字符串
tableHead4_61 = ['information']
sqlCase4_61 = "select concat('Hello ', 'World!') information from DUAL"

# exp4_62：
# 【例 4.62】 使用 initcap() 函数转换字符串 "oh my god! " 的输出
tableHead4_62 = ['information']
sqlCase4_62 = "select initcap('oh my god! ') information from DUAL"

# exp4_63：
# 【例 4.63】 在字符串 “oracle 11g” 中，从第3个字符开始查询字符串 “1” 第2次出现的位置
tableHead4_63 = ['information']
sqlCase4_63 = "select instr('oracle 11g', '1', 3, 2) information from DUAL"

# exp4_64：
# 【例 4.64】 在 SCOTT 模式下，通过使用 length() 函数返回雇员名称长度大于5的雇员信息及所在部门信息
tableHead4_64 = ['e.EMPNO', 'e.ENAME', 'd.DNAME']
sqlCase4_64 = "select e.EMPNO, e.ENAME, d.DNAME " \
              "from EMP e inner join DEPT d " \
              "on e.DEPTNO = d.DEPTNO " \
              "where length(e.ENAME) > 5"

# exp4_65：
# 【例 4.65】 在 HR 模式下，在 employees 表中检索雇员名称以字母 “a” 开头的员工信息，并将 first_name 字段的值转换为小写，
# 将 last_name 字段的值转换为大写
tableHead4_65 = ['EMPLOYEE_ID', 'FIRST_NAME', 'LAST_NAME']
sqlCase4_65 = "select EMPLOYEE_ID, lower(FIRST_NAME), upper(LAST_NAME) " \
              "from employees " \
              "where lower(FIRST_NAME) like 'a%'"

# exp4_66：
# 【例 4.66】 使用 LTRIM、LTRIM 和 TRIM 函数分别去掉字符串 “####East####”、“East    ” 和 “####East###”
# 中左侧 “#”、右侧 空格 和左右两侧的 ”#“
tableHead4_66 = ['ltrim(\'####East####\', \'#\')', 'rtrim(\'East    \')', 'trim(\'#\' from \'####East###\')']
sqlCase4_66 = "select ltrim('####East####', '#'), rtrim('East    '), trim('#' from '####East###') from dual"

# exp4_67：
# 【例 4.67】 使用 replace() 函数吧字符串 ”Bad Luck Bad Gril“ 中的 ”Bad“ 字符串用 ”Good“ 替换掉
tableHead4_67 = ['replace(\'Bad Luck Bad Gril\', \'Bad\', \'Good\')']
sqlCase4_67 = "select replace('Bad Luck Bad Gril', 'Bad', 'Good') from dual"

# exp4_68：
# 【例 4.68】 使用 substr() 函数在字符串 ”MessageBox“ 中从第8个位置截取长度为3的子字符串
tableHead4_68 = ['substr(\'MessageBox\', 8, 3)']
sqlCase4_68 = "select substr('MessageBox', 8, 3) from dual"

OptOracle.printData(con_hr, tableHead4_65, sqlCase4_65)  # 执行 exp4_65
OptOracle.printData(con_scott, tableHead4_68, sqlCase4_68)  # 执行 exp4_67
