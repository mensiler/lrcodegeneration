#coding=utf_8
#POST 请求提交form数据
import json
from custom_request import config
#事物
lr_transaction=config.lr_transaction
#检查点
asse=config.asse
#json数据
body_param=config.body_param
#接口名称
name=config.name
#接口地址
url=config.url
#header
header_param=config.header_param
lr_start='lr_start_transaction("%s");'%lr_transaction
print(lr_start)
header_data=header_param.strip().split('\n')
for i in header_data :
    r1="web_add_header("+str(i.strip().split(":"))[1:-1]+");"
    header=r1.replace("'",'"')
    print(header)

post_json='''web_custom_request("%s",
                       "URL=%s",
                       "Method=POST",
                       "Resource=0",
                       "Mode=HTML",
                       "Body=%s",
                       LAST );
'''%(name,url,body_param)
#
save_par='''web_reg_save_param("%s","LB=**","RB=**","ORD=1","Notfound=warning",LAST );'''%asse
print("//检查点")
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
print("//事务判断")
print(duanyan)