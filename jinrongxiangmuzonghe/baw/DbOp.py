'''

'''
from jinrongxiangmuzonghe.caw.Mysql import Mysql
class DbOp:
    def delete_user(self,db,mobilephone):
        mysql = Mysql()
        conn = mysql.connect(db)
        mysql.execute(conn, f"delete from member where mobilephone={mobilephone} ")
        mysql.disconnect(conn)
