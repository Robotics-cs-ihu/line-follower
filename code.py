#Libraries imports
import machine
from machine import Pin

#Motors Pins
M1A = machine.PWM(machine.Pin(8))
M1B = machine.PWM(machine.Pin(9))
M2A = machine.PWM(machine.Pin(10))
M2B = machine.PWM(machine.Pin(11))

#Define frequency for each motor
M1A.freq(50)
M1B.freq(50)
M2A.freq(50)
M2B.freq(50)

#IR infared sensors Pins
Rir = Pin(26, Pin.IN)
Cir = Pin(27, Pin.IN)
Lir = Pin(28, Pin.IN)

#While loop for motors movements
while True :    
        
        #Function move forward - Both motors rotate forwards
        def move_forward() :
            M1A.duty_u16(30000)     						# Duty Cycle must be between 0 until 65535  
            M1B.duty_u16(0)
            M2A.duty_u16(0)
            M2B.duty_u16(30000)
         
        #Function turn left - Right motor rotates forward and left motor stops rotation
        def turn_left() :
            M1A.duty_u16(0)     
            M1B.duty_u16(0)
            M2A.duty_u16(0)
            M2B.duty_u16(30000)
        
        #Function turn right - Left motor rotates forward and right motor stops rotation
        def turn_right() :
            print
            M1A.duty_u16(30000)     
            M1B.duty_u16(0)
            M2A.duty_u16(0)
            M2B.duty_u16(0)  
        
        #Function stop rotation - Both motors stop rotation
        def stopping() :
            M1A.duty_u16(0)     
            M1B.duty_u16(0)
            M2A.duty_u16(0)
            M2B.duty_u16(0)
        
        #If statements for line following, when value is 0 the sensor detects light and when is 1 sensor doesn't detects light(black line)
        #When both lights on sensors is ON then there is reflection, and when on of them is OFF there is not reflection. 
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
        
    


