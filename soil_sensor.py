import time
from machine import UART

PH_DATA = b"\x01\x03\x00\x03\x00\x04\xB4\x09"           #the soil ph
MOISTURE_DATA = b"\x01\x03\x00\x00\x00\x01\x84\x0A"     #the soil humidity
TEMP_DATA = b"\x01\x03\x00\x01\x00\x02\x95\xCB"         #the soil temp
CONDUCTIVITY_DATA = b"\x01\x03\x00\x02\x00\x03\xA4\x0B" #the soil conductivity
NITROGEN_DATA = b"\x01\x03\x00\x04\x00\x05\xC4\x08"     #the soil N's content
PHOSPHORUS_DATA = b"\x01\x03\x00\x05\x00\x06\xD5\xC9"   #the soil P's content
POTASSIUM_DATA = b"\x01\x03\x00\x06\x00\x07\xE4\x09"    #the soil K's content
SAINITY_DATA = b"\x01\x03\x00\x07\x00\x08\xF5\xCD"      #the soil salt's content

#crc16 modbus计算http://www.ip33.com/crc.html



class the_soil_sensor():
    def __init__(self,uart,freq):
        self.uart = uart
        self.freq = freq
        self.UART = UART(self.uart,self.freq)
        self.uartinit = self.UART.init(self.freq,bits = 8,parity = None,stop = 1)
    def write_cmd(self,cmd):
        self.UART.write(cmd)
    
    def read_uart(self):
        return(self.UART.read())

    
    def the_soil_ph(self,test = None):
        self.write_cmd(PH_DATA)
        time.sleep(0.2)
        soil_ph = self.read_uart()
        try:
            ph_data = float(int(str(hex(soil_ph[3]).lstrip("0").lstrip("x") + hex(soil_ph[4]).lstrip("0").lstrip("x")) ,16)/10)
            return(ph_data)
        except TypeError as e:
            return("error")
    
    def the_soil_water(self,test = None):
        self.write_cmd(MOISTURE_DATA)
        time.sleep(0.2)
        soil_moisture_content = self.read_uart()
        try:
            water_data = float(int(str(hex(soil_moisture_content[3]).lstrip("0").lstrip("x") + hex(soil_moisture_content[4]).lstrip("0").lstrip("x")) ,16)/10)
            return(water_data)
        except TypeError as e:
            return("error")
    
    def the_soil_temp(self,test = None):
        self.write_cmd(TEMP_DATA)
        time.sleep(0.2)
        soil_temp = self.read_uart()
        try:
            temp_data = float(int(str(hex(soil_temp[3]).lstrip("0").lstrip("x") + hex(soil_temp[4]).lstrip("0").lstrip("x")) ,16)/10)
            return(temp_data)
        except TypeError as e:
            return("error")
    def the_soil_conductivity(self,test = None):
        self.write_cmd(CONDUCTIVITY_DATA)
        time.sleep(0.2)
        soil_conductivity = self.read_uart()
        try:
            conductivitya_data = float(int(str(hex(soil_conductivity[3]).lstrip("0").lstrip("x") + hex(soil_conductivity[4]).lstrip("0").lstrip("x")) ,16)/10)
            return(conductivitya_data)
        except TypeError as e:
            return("error")
    
    def the_soil_nitrogen(self,test = None):
        self.write_cmd(NITROGEN_DATA)
        time.sleep(0.2)
        soil_nitrogen_content = self.read_uart()
        try:
            nitrogen_data = float(int(str(hex(soil_nitrogen_content[3]).lstrip("0").lstrip("x") + hex(soil_nitrogen_content[4]).lstrip("0").lstrip("x")) ,16)/100)
            return(nitrogen_data)
        except TypeError as e:
            return("error")
    def the_soil_phosphorus(self,test = None):
        self.write_cmd(PHOSPHORUS_DATA)
        time.sleep(0.2)
        soil_phosphorus_content = self.read_uart()
        try:
            phosphorus_data = float(int(str(hex(soil_phosphorus_content[3]).lstrip("0").lstrip("x") + hex(soil_phosphorus_content[4]).lstrip("0").lstrip("x")) ,16)/100)
            return(phosphorus_data)
        except TypeError as e:
            return("error")
    def the_soil_potassium(self,test = None):
        self.write_cmd(POTASSIUM_DATA)
        time.sleep(0.2)
        soil_potassium_content = self.read_uart()
        try:
            potassium_data = float(int(str(hex(soil_potassium_content[3]).lstrip("0").lstrip("x") + hex(soil_potassium_content[4]).lstrip("0").lstrip("x")) ,16)/100)
            return(potassium_data)
        except TypeError as e:
            return("error")
    def the_soil_sainity(self,test = None):
        self.write_cmd(SAINITY_DATA)
        time.sleep(0.2)
        soil_sainity = self.read_uart()
        try:
            sainity_data = float(int(str(hex(soil_sainity[3]).lstrip("0").lstrip("x") + hex(soil_sainity[4]).lstrip("0").lstrip("x")) ,16)/100)
            return(sainity_data)
        except TypeError as e:
            return("error")
        
if __name__ == "__main__":
    from soil_sensor import the_soil_sensor
    soilsensor = the_soil_sensor(2,4800)
    soilsensor.the_soil_conductivity()
    soilsensor.the_soil_nitrogen()
    soilsensor.the_soil_ph()
    soilsensor.the_soil_phosphorus()
    soilsensor.the_soil_potassium()
    soilsensor.the_soil_sainity()
    soilsensor.the_soil_temp()
    soilsensor.the_soil_water()

