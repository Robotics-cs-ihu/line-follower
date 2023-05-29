import machine
from machine import Pin

M1A = machine.PWM(machine.Pin(8))
M1B = machine.PWM(machine.Pin(9))
M2A = machine.PWM(machine.Pin(10))
M2B = machine.PWM(machine.Pin(11))
M1A.freq(50)
M1B.freq(50)
M2A.freq(50)
M2B.freq(50)

Rir = Pin(26, Pin.IN)
Cir = Pin(27, Pin.IN)
Lir = Pin(28, Pin.IN)

while True :    
        
        #move forward-both motors rotate
        def move_forward() :
            M1A.duty_u16(30000)     						# Duty Cycle must be between 0 until 65535 #chech battery
            M1B.duty_u16(0)
            M2A.duty_u16(0)
            M2B.duty_u16(30000)
         
        #   turn left-motorL stops
        def turn_left() :
            M1A.duty_u16(0)     
            M1B.duty_u16(0)
            M2A.duty_u16(0)
            M2B.duty_u16(30000)
        
        #turn right-right motor stops
        def turn_right() :
            print
            M1A.duty_u16(30000)     
            M1B.duty_u16(0)
            M2A.duty_u16(0)
            M2B.duty_u16(0)  #backwards  slower  (25000)
            
        def stopping() :
            M1A.duty_u16(0)     
            M1B.duty_u16(0)
            M2A.duty_u16(0)
            M2B.duty_u16(0)
        
    
        if Rir.value()==0 and Cir.value()==1 and Lir.value()==0 :
            move_forward()
            
        elif Rir.value()==0 and Lir.value()==0 :
            move_forward()
            
        elif Rir.value()==0 and Cir.value()==0 and Lir.value()==1:
            turn_right()
            
        elif Rir.value()==1 and Cir.value()==0 and Lir.value()==0:
            turn_left()
        
        elif Rir.value()==1 and Cir.value()==1 and Lir.value()==0 :
            turn_right()
        
        elif Rir.value()==0 and Cir.value()==1 and Lir.value()==1 :
            turn_left()
        
        elif Rir.value()==0 and Cir.value()==0 and Lir.value()==0 :
            stopping()
        
        elif Rir.value()==1 and Cir.value()==1 and Lir.value()==1 :
           stopping()
        
    


