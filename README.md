# mkPython

功能描述  

1. 提供python3环境下makeblock系列产品的python3库文件；
2. 提供API文档；
3. 提供根据API问你当自动生成python库功能。

特点说明：
1. 该工程为一个python3控制makeblock硬件的公共框架，
   该框架适用以F3F4协议运行的microPython主控设备和以F0F7协议运行的mbuild及神经元模块，设置运行FF55协议的arduino体系产品（mbot）；
2. 该框架主要分成4层：
    1） 链路层：负责和硬件设备的连接，数据流处理；
    2） 