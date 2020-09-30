import requests
'''
投资人注册
借款人注册
获取用户列表
投资人登录
投资人充值
借款人登录
借款人提交借款申请材料，平台加贷款项目
获取标列表
平台人员审核1-运营人员审核（初审）
平台人员审核2-运营主管审核（复审）
平台人员审核3-运营总监审核（投标中状态)
投资人投标
    投标期限内达到借款总金额，即满标
	投标期限内未达到借款总金额，即流标，余额返回投资人账户
投资人获取投资记录
获取标的所有投资记录
生成借款人回款计划
'''
print("---------投资人注册--------")
url ="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone": "13227011051", "pwd": "1234567", "regname": "test"}
r = requests.post(url, data=canshu)
print(r.text)
print("---------借款人注册--------")
url ="http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone": "18709183931", "pwd": "1234567", "regname": "toox"}
r = requests.post(url, data=canshu)
print(r.text)
print("--------获取用户列表-------")
url ="http://192.168.150.222:8081/futureloan/mvc/api/member/list"
r = requests.post(url)
print(r.text)
print("--------投资人登录-------")
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
canshu = {"mobilephone": "13227011051", "pwd": "1234567"}
r = requests.post(url, data=canshu)
print(r.text)
print("--------投资人充值-------")
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/recharge"
canshu = {"mobilephone": "13568246798", "amount": "100000"}
r = requests.post(url, data=canshu)
print(r.text)
print("--------借款人登录-------")
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
canshu = {"mobilephone": "18709183931", "pwd": "1234567", "regname": "toox"}
r = requests.post(url, data=canshu)
print(r.text)
print("--------借款人提交借款申请材料，平台加贷款项目-------")
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
canshu = {
    "membeiId": "123", "title": "demo", "amount": "500","loanRate":"18","loanTerm":"6","loanDateType":"0","repaymemtWay":"1","biddingDays":"5"}
r = requests.post(url, data=canshu)        #项目ID    标题
print(r.text)
print("--------获取标列表-------")
url = "http://192.168.150.222:8081/futureloan/mvc/api/loan/getLoanList"
r = requests.post(url)
print(r.text)
print("--------平台人员审核1-运营人员审核（初审）-------")
url = "http://192.168.150.222:8081/futureloan/mvc/api/loan/audit"
canshu = {"id": "001", "status": "审核中"}       #项目ID
r = requests.post(url, data=canshu)
print(r.text)
print("--------平台人员审核2-运营主管审核（复审）-------")
url = "http://192.168.150.222:8081/futureloan/mvc/api/loan/audit"
canshu = {"id": "001", "status": "复审中 "}       #项目ID
r = requests.post(url, data=canshu)
print(r.text)
print("--------平台人员审核3-运营总监审核（投标中状态)-------")
url = "http://192.168.150.222:8081/futureloan/mvc/api/loan/audit"
canshu = {"id": "001", "status": "竞标中 "}
r = requests.post(url, data=canshu)    #项目ID
print(r.text)
print("--------投资人投标-------")
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/bidLoan"
canshu = {"memberId": "13227011051", "password": "1234567","loanId": "001", "amount": "1000"}
r = requests.post(url, data=canshu)    #用户ID   密码    标ID
print(r.text)
print("--------投资人获取投资记录-------")
url = "http://192.168.150.222:8081/futureloan/mvc/api/invest/getInvestsByMemberId"
canshu = {"memberId": "13227011051"}       #用户ID
r = requests.post(url, data=canshu)
print(r.text)
print("--------获取标的所有投资记录-------")
url = "http://192.168.150.222:8081/futureloan/mvc/api/invest/getInvestsByLoanId"
canshu = {"loanId": "001"}                  #标ID
r = requests.post(url, data=canshu)
print(r.text)
print("--------生成借款人回款计划-------")
url = "http://192.168.150.222:8081/futureloan/mvc/api/loan/generateRepayments"
canshu = {"id": "001"}                #项目id
r = requests.post(url, data=canshu)
print(r.text)




