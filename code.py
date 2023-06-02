#Import needed libraries
import machine
from machine import Pin
import utime
#Run code when button GP21 is pressed
#Code must be saved on the board as 'main'
gp21_pin = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_UP)
#Pins for motors' rotation
M1A = machine.PWM(machine.Pin(8))
M1B = machine.PWM(machine.Pin(9))
M2A = machine.PWM(machine.Pin(10))
M2B = machine.PWM(machine.Pin(11))
#Setting frequency for motors
M1A.freq(50)
M1B.freq(50)
M2A.freq(50)
M2B.freq(50)
#Pins for the sensors
Rir = Pin(26, Pin.IN)          
Cir = Pin(27, Pin.IN)
Lir = Pin(28, Pin.IN)
 #Function for forward movement
def move_forward() :
    M1A.duty_u16(35000)     		# Duty Cycle must be between 0 until 6553
    M1B.duty_u16(0)
    M2A.duty_u16(0)
    M2B.duty_u16(35000)         
 #Function for left turn. Left motor stops rotation
def turn_left() :
     M1A.duty_u16(35000)     
     M1B.duty_u16(0)
     M2A.duty_u16(0)
     M2B.duty_u16(0)        
  #Function for right turn. Right motor stops rotation
def turn_right() :
     M1A.duty_u16(0)     
     M1B.duty_u16(0)
     M2A.duty_u16(0)
     M2B.duty_u16(35000)  
 #Function for stopping the vehicle. Both motors stop rotation           
def stopping() :
     M1A.duty_u16(0)     
     M1B.duty_u16(0)
     M2A.duty_u16(0)
     M2B.duty_u16(0)
 #Function for line-following       
def line_follower():
    while True:
    
        if Rir.value()==0 and Cir.value()==1 and Lir.value()==0 :
            move_forward()
            
        elif Rir.value()==0 and Lir.value()==0 :    
            move_forward()
            
        elif Rir.value()==0 and Cir.value()==0 and Lir.value()==1:
            turn_left()
        
        elif Rir.value()==1 and Cir.value()==0 and Lir.value()==0:
            turn_right()
        
        elif Rir.value()==1 and Cir.value()==1 and Lir.value()==0 :
            turn_left()
        
        elif Rir.value()==0 and Cir.value()==1 and Lir.value()==1 :
            turn_right()
        
        elif Rir.value()==0 and Cir.value()==0 and Lir.value()==0 :
            stopping()
        
        elif Rir.value()==1 and Cir.value()==1 and Lir.value()==1 :
            stopping()
        
    
while True:
    if gp21_pin.value() == 0 :
        line_follower()





    


