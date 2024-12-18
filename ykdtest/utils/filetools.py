#1.保存信息到文件
def save_file(file_path="./conf/token.txt", token=""):
     #(file_path=然认/conf/token.txt,token=默认为空
     #到文件中以写入的模式把token写入token.txt 中
    with open(file_path,"w")as f:# 新建一个文件保存在 conf 中
        f.writelines(token)
#2.读取txt 文件
def read_file(file_path="./conf/token.txt"):
    with open(file_path,"r")as f: #r表示只读模式
        token =f.read()
        return token # 返回数据