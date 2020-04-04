""" 章节4.4.4 转换类函数 """

import cx_Oracle as cx
from Oracle11gBase9787302458227.chapter04 import OptOracle

# 连接 Oracle 数据库
con_scott = cx.connect('scott', 'tiger', '127.0.0.1:1521/orcl')  # SCOTT 模式

# exp4_74：
# 【例 4.74】 使用 to_char() 函数转换系统日期为 “YYYY-MM-DD” 格式
tableHead4_74 = ['默认格式日期', '转换后日期']
sqlCase4_74 = "select sysdate as 默认格式日期, to_char(sysdate, 'YYYY-MM-DD, hh24:mi:ss') as 转换后日期 from dual"

# exp4_75：
# 【例 4.75】 使用 to_number() 函数把十六进制数 “18f” 转换为十进制数
tableHead4_75 = ['to_number(\'18f\', \'xxx\')']
sqlCase4_75 = "select to_number('18f', 'xxx') as 十进制数 from dual"

OptOracle.printData(con_scott, tableHead4_75, sqlCase4_75)  # 执行 exp4_75
