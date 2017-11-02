import BlynkLibimport time
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
roms = ds.scan()blynk = BlynkLib.Blynk(BLYNK_AUTH, server=BLYNK_SERVER)@blynk.VIRTUAL_WRITE(7)def v7_read_handler(value):  print ('V7: ', value)
  v7.value(not int(value))  @blynk.VIRTUAL_WRITE(6)def v6_write_handler(value):  print ('V6: ', value)
  v6.value(not int(value))  @blynk.VIRTUAL_WRITE(5)def v5_write_handler(value):  print ('V5: ', value)
  v5.value(not int(value))  @blynk.VIRTUAL_WRITE(4)def v4_write_handler(value):  print ('V4: ', value)
  v4.value(not int(value))  def blynk_connected():    print('Connected') def blynk_task():  print('Blynk task')
  if len(roms) > 0:
    ds.convert_temp()
    t = ds.read_temp(roms[0])
    print('Temperature: {0:.2f}'.format(t))
    blynk.virtual_write(8, t)    blynk.on_connect(blynk_connected)blynk.set_user_task(blynk_task, 5000)
th.start_new_thread('blink', blynk.run, ()) 