# -*- coding: UTF-8 -*-
from PCA9685 import PCA9685 #导入驱动，
import time
import ultrasonic
pwm=PCA9685()
pwm.init()#初始化pca9685
pwm.setsq(60)#设置频率
pwm.allinit()#把16个通道初始化

jiaodu=90
while 1:
    while jiaodu<130:
        pwm.setduoji(0,jiaodu)#设置0通道角度
#        pwm.setduoji(1,jiaodu)#设置1通道角度
#        jiaodu=jiaodu+1
#        time.sleep(0.01)
        print jiaodu
        ultrasonic.reading(0)
    while jiaodu>30:
        pwm.setduoji(0,jiaodu)
#        pwm.setduoji(1,jiaodu) 
#        jiaodu=jiaodu-1 
#        time.sleep(0.01)
        print jiaodu
        ultrasonic.reading(0)
