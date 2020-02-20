# mkPython #

## 功能描述 ## 

1. 提供python3环境下makeblock系列产品的python3库文件；
2. 提供API文档；
3. 提供根据API问你当自动生成python库功能。

## 使用例程 ##
### halo ###

```
from mkPython import halo
import random

i = 0
j = 0
k = 0

H_J = 1
while True:
	data = [0] * 36
	for t in range(12):
		red  = 32 * (1 + math.sin((t / 2.0 + j / 4.0) * H_J) )
		green = 32 * (1 + math.sin((t / 1.0 + j / 9.0 + 2.1)) * H_J )
		blue = 32 * (1 + math.sin((t / 3.0 + k / 14.0 + 4.2)) * H_J )
		data[t * 3] = int(red)
		data[t * 3 + 1] = int(green)
		data[t * 3 + 2] = int(blue)
	data = bytearray(data)
	halo.led.show_full_color(data)
	j += random.randint(1, 6) / 6.0
	j += random.randint(1, 6) / 6.0
	k += random.randint(1, 6) / 6.0
```


### mbuild ###
```
from mkPython.halo import mbuild
import time

while True:
	print(mbuild.dual_rgb_sensor("RGB1"))
	time.sleep(0.2)
```