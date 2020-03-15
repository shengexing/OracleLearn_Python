""" 操作 Oracle 数据库的文件 """


# 连接数据库，执行 SELECT 语句，打印数据
def printData(connect, tableHead, sqlCase):
    cursor = connect.cursor()  # 创建游标
    print(tableHead)  # 打印表头
    cursor.execute(sqlCase)  # 执行sql语句，可以替换不同的例子（93710）

    # 遍历游标，打印数据
    for result in cursor:
        print(result)

    cursor.close()  # 关闭游标
    connect.close()  # 关闭数据库连接
