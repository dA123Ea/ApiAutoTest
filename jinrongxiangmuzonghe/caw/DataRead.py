'''
读写文件的类
'''
import configparser

import os

import yaml


class DataRead:
    def get_project_path(self):
        '''
        获取当前工程路径
        :return:
        '''
        curent_file_path=os.path.realpath(__file__)  #获取绝对路径
        dir_name=os.path.dirname(curent_file_path)   #获取到文件前
        dir_name = os.path.dirname(dir_name)    #获取到

        return  dir_name + "\\"

    def read_ini(self,file_path,key):
        '''
        读取ini文件，返回key 返回的value
        :param file_path:    文件路径
        :param key:
        :return:    key 对应的value
        '''
        real_file_path=self.get_project_path() +file_path
        config=configparser.ConfigParser()
        config.read( real_file_path)    #读取ini文件
        value=config.get("env",key)   #读取【env】里面的key
        return value
    def read_yaml(self,file_path):
        '''
        读取yaml文件
        :param file_path:  yaml 文件路径
        :return:
        '''
        real_file_path=self.get_project_path() +file_path
        with open (real_file_path,"r",encoding='utf-8')as f:
            file_content=f.read()

            #用yaml的Load方法把文班的文件转换成字典

            content=yaml.load(file_content,Loader=yaml.FullLoader)
            return content

#测试代码：用完可以删除
if __name__ == '__main__':
    #
    value=DataRead().read_ini(r"data_env\env.ini","url")
    print(value)
    print(DataRead().get_project_path())
    print(DataRead().read_yaml(r"data_case\zc_shibai.yaml"))