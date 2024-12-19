#这里的代码是登录相关的case
import pytest
import requests

#跨文件夹的导入方式
import os,sys
sys.path.append(os.getcwd())
from utils.filetools import save_file
from utils.exceltools import my_read_excel #调用read excel 方法 用于读取数据

def test_01_login_success():
    #登录成功的测试用例
    data_res = my_read_excel() #调取read_excel 的方法，读取数据，data/测谈网测试用例.xlsx为文件的相对路径，登录为页面的名字
    url = data_res[0][2] #读取上行取出来的值中的地址
    header = eval(data_res[0][3])#读取出来的值中的请求头，用eval 强转为字典
    data = eval(data_res[0][4]) #读取出来的值中的参数，读出来的数据是字符串，所以用eval 强转为字典
    res =requests.post(url=url,json=data,headers=header)# print(res.text)#可以打印查询到内容
    assert res.status_code == 200
    assert res.json()["status"]== 200   
    #测试用例(方法的结果):成功 F:失败了(代码报错，断言失败)
    # 保存最后一次登录的token
    # 先取出token token 传参
    token = res.json()["data"]["token" ]
    save_file(token=token)

test_01_login_success()

