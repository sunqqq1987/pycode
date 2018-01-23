#注册码写法
#取mac地址,异或0xf出机器码
#取mac地址,异或0x4出sn中间码
#sn中间码经过md5运算，出SN
#测试用
import uuid
import hashlib
#md5计算函数
class Md5calc(object):
    def calc_md5(self, src):
        m = hashlib.md5()
        m.update(src.encode('UTF-8'))
        return m.hexdigest().upper()
#取主机mac地址，目前不确定取得哪个网卡地址
    def get_mac(self):
        mac=uuid.UUID(int = uuid.getnode()).hex[-12:].upper()
        return mac
    def conver_list(self, list1):  
      str1="".join(list1).upper()#连接list为字符串
      list2=str1.split("0X")
      str3="".join(list2).upper()#连接list为字符串
      return(str3)
#mac地址转列表
    def id_calc(self):
        mac=uuid.UUID(int = uuid.getnode()).hex[-12:].upper()
        mac2=list(mac)
        for i in range(12):
            mac2[i]=hex(int(mac2[i], 16)^0xf)#逐位异或，控制0xf值可以有不同结果
        id6=self.conver_list(mac2)
        return(id6)      
    def sn_calc(self):
        mac=uuid.UUID(int = uuid.getnode()).hex[-12:].upper()
        mac2=list(mac)
        for i in range(len(mac2)):
            mac2[i]=hex(int(mac2[i], 16)^0x4)#异或值不同，对SN和机器码分开计算
        sn_4=self.conver_list(mac2)
        sn_5=self.calc_md5(sn_4)
        return(sn_5)
    def sn_calc2(self, sn1):
        sn1_1=list(sn1)
        for i in range(len(sn1)):
            sn1_1[i]=hex(int(sn1_1[i], 16)^0xf^0x4)#由机器码反推出mac  
        sn1_6=self.conver_list(sn1_1)
        sn1_7=self.calc_md5(sn1_6)
        return(sn1_7)
        
        
