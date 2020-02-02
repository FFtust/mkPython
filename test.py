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
# ____________________________________________________________________b_________
import communication.protocol.F3F4
import communication.channel.commu_uart

uart = communication.channel.commu_uart.uart_link(["COM3", "115200"])
uart.config(["COM3", "115200"])
uart.open()

protocol = communication.protocol.F3F4.F3F4_frame()

uart.rigister_protocol_parse_handle(protocol)

# uart.write(b"hello")
uart.start_listening()