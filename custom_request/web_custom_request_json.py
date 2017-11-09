#coding=utf_8
import json
#事物
lr_transaction="搜索"
#检查点
asse="searchresult"
#json数据
body='''searchMode=1&currPage=1&queryType=1&keyword=%E8%8C%85%E5%8F%B0&pageSize=30'''
#接口名称
name="search"
#接口地址
url="http://las.secoo.com/api/search/keyword"
#header
l='''User-Agent: android
Keep-Alive: true
screen-width: 1080
app_ver: 5.9.1
uuid: 864229039374202_18%3Ad2%3A76%3A42%3A62%3A3b
mac: 18%3Ad2%3A76%3A42%3A62%3A3b
upk: 1125edab63da4fa7af684c8d4d9328c3%7C14003422896%7C466900e2d3a4408bbc327efa435d81f0%7C600CDA204228EE965C2918096970776A
app-id: 644873678
Accept-Encoding: gzip%2Cdeflate
platform: MHA-AL00
device-id: 864229039374202_18%3Ad2%3A76%3A42%3A62%3A3b
screen-height: 1812
device_id: 864229039374202_18%3Ad2%3A76%3A42%3A62%3A3b
imei: 864229039374202
app-ver: 5.9.1
appver: 5.9.1
platform-ver: 7.0
sysverlevel: 24
session_id: 1510134341640-9113
platform-type: 1
sysver: 7.0
platform_type: 1
channel: vivo
product: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 74
Host: las.secoo.com
Connection: Keep-Alive
'''








lr_start='lr_start_transaction("%s");'%lr_transaction
print(lr_start)
d=l.strip().split('\n')
for i in d :
    r1="web_add_header("+str(i.strip().split(":"))[1:-1]+");"
    r=r1.replace("'",'"')
    header=r
    print(r)

d={}
l="upkey=1125edab63da4fa7af684c8d4d9328c3%7C14003422896%7C466900e2d3a4408bbc327efa435d81f0%7C600CDA204228EE965C2918096970776A&sync=true&aid=2&choseProductInfo=%5B%7B%22productId%22%3A%2224325424%22%2C%22quantity%22%3A1%2C%22type%22%3A0%2C%22areaType%22%3A0%2C%22isChecked%22%3A0%2C%22packageId%22%3A0%7D%5D&isChecked=0&client=iphone"
l1=l.strip().split("&")
for i in l1:
    l2=i.strip().split("=")
    d[l2[0]]=l2[1]
body=str(json.dumps(d)).replace('"','\\"')

post_json='''web_custom_request("%s",
                       "URL=%s",
                       "Method=POST",
                       "Resource=0",
                       "Mode=HTML",
                       "EncType=application/json",
                       "Body=%s",
                       LAST );
'''%(name,url,body)
#
save_par='''web_reg_save_param("%s","LB=**","RB=**","ORD=1","Notfound=warning",LAST );'''%asse
print(save_par)
print(post_json)
duanyan='''if(strcmp(lr_eval_string("{%s}"),"**")==0)

	{

		lr_end_transaction("%s", LR_PASS);

	}
else
	{
		lr_output_message("%s失败，返回：%s",lr_eval_string("{%s}"));
		lr_end_transaction("%s", LR_FAIL);

	}'''%(asse,lr_transaction,lr_transaction,"%s",asse,lr_transaction)
print(duanyan)