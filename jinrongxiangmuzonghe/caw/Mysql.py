'''
数据库的操作
'''
import pymysql

class Mysql:
    def connect(self,db):
        '''
        连接数据库
        :param db:
        :return:
        '''
        ip=db['ip']
        port=int(db['port'])
        name=db['name']
        user=db['user']
        pwd=db['pwd']

        try:
            conn = pymysql.connect(host=ip, port=port, password=pwd, user=user,charset='utf8', database=name)
            print(f"连接数据库{ip}·{port}成功")
            return conn
        except Exception as e:
            print(f"连接数据库异常处理,异常信息为{e}")
    def execute(self,conn,sql):
        try:
            cursor=conn.cursor()
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            print(f"执行sql语句{sql}")
        except Exception as e:
         print(f"执行sql语句异常，异常信息为{e}")
    def disconnect(self,conn):
        '''
        断开连接
        :return:
        '''
        try:
            conn.close()
        except Exception as e:
            print(f"断开数据库异常,异常信息为{e}")

if __name__ == '__main__':
    db={"ip":"192.168.150.52","port":"3306","name":"apple","user":"root","pwd":"123456"}
    mysql=Mysql()
    conn=mysql.connect(db)
    mysql.execute(conn,"delete from member where mobilephone=18563120032 ")
    mysql.disconnect(conn)


