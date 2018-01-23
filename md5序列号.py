#注册码写法
#取mac地址,异或0xf出机器码
#取mac地址,异或0x4出sn中间码
#sn中间码经过md5运算，出SN
import uuid
import hashlib
#md5计算函数
def curlmd5(src):
    m = hashlib.md5()
    m.update(src.encode('UTF-8'))
    return m.hexdigest()
#取主机mac地址，目前不确定取得哪个网卡地址
mac=uuid.UUID(int = uuid.getnode()).hex[-12:].upper()
#mac地址转列表
mac2=list(mac)
mac3=[]#定义两个空列表
sn_1=[]
for i in mac2:#列表赋值
    mac3.append(i)
    sn_1.append(i)
for i in range(12):
    mac3[i]=hex(int(mac2[i], 16)^0xf)#逐位异或，控制0xf值可以有不同结果
    sn_1[i]=hex(int(mac2[i], 16)^0x4)#异或值不同，对SN和机器码分开计算
id4="".join(mac3).upper()#连接list为字符串
id5=id4.split("0X")
id6="".join(id5).upper()#连接list为字符串
sn_2="".join(sn_1).upper()#连接list为字符串
sn=curlmd5(sn_2)
print("机器码:", id6)
print("序列号:", sn)

