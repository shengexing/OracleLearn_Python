""" 操作 Oracle 数据库的文件 """
import cx_Oracle as cx


def connectDatabase(dbName='orcl', userName='scott', pwd='tiger'):  # 创建数据库连接，设置默认值
    dsn = cx.makedsn('127.0.0.1', '1521', dbName)
    db = cx.connect(userName, pwd, dsn)
    return db


def selectDB(db, sqlStr):  # 查询数据
    cursor = db.cursor()
    cursor.execute(sqlStr)
    result = cursor.fetchall()
    cursor.close()
    return result


def dmlDB(db, sql):  # 插入，更新，删除 数据
    cursor = db.cursor()
    cursor.execute(sql)
    cursor.close()
    db.commit()


def dmlDBWithPara(db, sql, para):  # 带参数的 插入，更新，删除 数据
    cursor = db.cursor()
    cursor.execute(sql, para)
    cursor.close()
    db.commit()


def ddlDB(db, sql):  # DDL 语句
    cursor = db.cursor()
    cursor.execute(sql)
    cursor.close()


def executeScriptsFromFile(db, filename):  # 执行 SQL 脚本
    cursor = db.cursor()
    filedb = open(filename, 'r', encoding='gbk')
    sqlFile = filedb.read()
    filedb.close()
    sqlCommands = sqlFile.split(';')

    print('Start: sql脚本执行开始')

    for command in sqlCommands:
        command = command.replace('\n', ' ')
        print(command)
        try:
            cursor.execute(command)
        except Exception as msg:
            print(msg)

    print('End: sql脚本执行完成')


def printResult(rs):  # 打印结果集
    for row in rs:
        print(row)


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
