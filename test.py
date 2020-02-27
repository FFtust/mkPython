'''
class a():
	def __init__(self):
		self.var = 1


class b(a):
	def __init__(self):
		super().__init__()
		self.var = 2

class c(a):
	def __init__(self):
		super().__init__()
		self.var = 3

A = a()

B = b()

C = c()


print(A.var)
print(B.var)
print(C.var)


'''
# _____________________________________________________________________________
'''
import hashlib
m = hashlib.md5()

m.update("lie".encode("utf-8"))
m.update("n".encode("utf-8"))
print(m.hexdigest())

m = hashlib.md5()

m.update("lien".encode("utf-8"))
print(m.hexdigest())
'''
# _____________________________________________________________________________
# import communication.protocol.F3F4
# import communication.channel.commu_uart

# uart = communication.channel.commu_uart.uart_link(["COM3", "115200"])
# uart.config(["COM3", "115200"])
# uart.open()

# protocol = communication.protocol.F3F4.F3F4_frame()

# uart.rigister_protocol_parse_handle(protocol)

# # uart.write(b"hello")
# uart.start_listening()

# _____________________________________________________________________________
# link = link_c()

# protocol = protocol_c();

# link.register(protocol)

# process = process_c()

# protocol.register(process)

# process.update_value()
# process.update_parameter()


# get_value(tag, xx)
# request(tag, xx)

# halo.button_is_pressed()
# halo.led.show_all(100, 0, 0)

# _____________________________________________________________________________
#!/usr/bin/env python
# !-*- coding:utf-8 -*-

# class Menu:

#     def __init__(self):
#         pass

#     def updateProject(self):
#         pass

#     def restartProject(self):
#         pass

#     def restartTomcat(self):
#         pass

#     def stopTomcat(self):
#         pass

#     def startTomcat(self):
#         pass

#     def methods(self):
#         return(list(filter(lambda m: not m.startswith("__") and not m.endswith("__") and callable(getattr(self, m)), dir(self))))

# if __name__ == '__main__':
#     print(Menu().methods())


 
import socket               # 导入 socket 模块
 
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口号
 
s.connect((host, port))
print(s.recv(1024))
s.close()