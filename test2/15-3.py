import re
def check_phone(strPhone):  #中华人民共和国电话号码
    regex_phone=re.compile(r'^(\(\d{3}\)|\d{3}-)?\d{8}$')
    result=True if regex_phone.match(strPhone) else False
    return result
def check_ZIP(strZIP):  #中华人民共和国邮政编码
    regex_ZIP=re.compile(r'^\d{6}$')
    result=True if regex_ZIP.match(strZIP) else False
    return result
def check_URL(strURL):  #网站网址
    regex_URL=re.compile(r'https?://\w+(?:\.[^\.]+)+(?:/.+)*$')
    result=True if regex_URL.match(strURL) else False
    return result
strPhone=input("请输入中国电话号码：")
input("{0}是有效的电话号码格式吗？{1}".format(strPhone,check_phone(strPhone)))
strZIP=input("请输入中国邮政编码：")
input("{0}是有效的邮政编码格式吗？{1}".format(strZIP,check_ZIP(strZIP)))
strURL=input("请输入网站网址：")
input("{0}是有效的网站网址格式吗？{1}".format(strURL,check_URL(strURL)))