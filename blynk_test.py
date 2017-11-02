import BlynkLib
from machine import Pin
import onewire, ds18x20
import wifi_connect as wlan
import _thread as th
BLYNK_AUTH = '71554af7a98b4535a7383f5be5d91ca3'
BLYNK_SERVER = '27.254.63.34'
wlan.connect()
v4 = Pin(18, Pin.OUT)
v4.value(True)
v5 = Pin(23, Pin.OUT)
v5.value(True)
v6 = Pin(19, Pin.OUT)
v6.value(True)
v7 = Pin(22, Pin.OUT)
v7.value(True)
ow = onewire.OneWire(Pin(5))
ds = ds18x20.DS18X20(ow)
roms = ds.scan()
  v7.value(not int(value))
  v6.value(not int(value))
  v5.value(not int(value))
  v4.value(not int(value))
  if len(roms) > 0:
    ds.convert_temp()
    t = ds.read_temp(roms[0])
    print('Temperature: {0:.2f}'.format(t))
    blynk.virtual_write(8, t)
th.start_new_thread('blink', blynk.run, ()) 