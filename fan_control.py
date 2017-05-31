import RPi.GPIO as GPIO
import os
import time

fan_gpio = 18
temp_min = 22
temp_max = 25
dev_path = '/sys/bus/w1/devices/'
dev_name = '28-000005be78bb'
dev_file = dev_path + dev_name + '/w1_slave'

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

GPIO.setmode(GPIO.BCM) 
GPIO.setup(fan_gpio, GPIO.OUT) 

def get_temp():
  temp=0
  for t in range(10):
     tempfile = open(dev_file)
     text = tempfile.read() 
     tempfile.close() 
     tline = text.split("\n")[1] # the second line contains temperature
     tdata = tline.split(" ")[9] # position 9 contains temparature value
     temp  += float(tdata[2:])/10
     time.sleep(0.1) 
  else: 
     return (temp / 1000)

############## CLASS FAN #############################

class FAN:
   def __init__(self, min=22, max=25 ):

      self.min=min
      self.max=max
      self.sFan=False
      self.last=self.sFan

   def update(self,current_value):
      if current_value < self.min :
         self.sFan = False
      elif current_value > self.max :
         self.sFan = True
      else :
         self.sFan = self.last

      self.last = self.sFan
      return self.sFan

   def setMin(self, Min):
      self.min = Min

   def setMax(self, Max):
      self.max=Max


############## END CLASS FAN #########################


fan=FAN(temp_min,temp_max)
fan.setMin( temp_min )
fan.setMax( temp_max )

while True:
  datafile = open("temperaturedata.log", "a")
  curr_temp = get_temp()
  datafile.write(str(time.strftime("%d/%m/%Y %H:%M:%S")) + " " + str(curr_temp) + " " + str(fan.update(curr_temp)) + "\n")
  datafile.close()
  GPIO.output(fan_gpio,fan.update(curr_temp))
  time.sleep(59) 
