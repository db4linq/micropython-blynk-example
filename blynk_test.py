import BlynkLibimport time
from machine import Pin
import onewire, ds18x20
import wifi_connect as wlan
import _thread as th
BLYNK_AUTH = '<BLYNK_AUTH>'
BLYNK_SERVER = '<BLYNK_SERVER>'
wlan.connect()
v4 = Pin(19, Pin.OUT) 
v5 = Pin(21, Pin.OUT) 
v6 = Pin(22, Pin.OUT) 
v7 = Pin(23, Pin.OUT) 
ow = onewire.OneWire(Pin(18))
ds = ds18x20.DS18X20(ow)
roms = ds.scan()blynk = BlynkLib.Blynk(BLYNK_AUTH, server=BLYNK_SERVER)
@blynk.BLYNK_WRITE(7)def v7_read_handler(value):  print ('V7: ', value)
  v7.value(int(value))  @blynk.BLYNK_WRITE(6)def v6_write_handler(value):  print ('V6: ', value)
  v6.value(int(value))  @blynk.BLYNK_WRITE(5)def v5_write_handler(value):  print ('V5: ', value)
  v5.value(int(value))  @blynk.BLYNK_WRITE(4)def v4_write_handler(value):  print ('V4: ', value)
  v4.value(int(value))  def blynk_connected():  print('Connected') 
  blynk.virtual_write(4, v4.value())
  blynk.virtual_write(5, v5.value())
  blynk.virtual_write(6, v6.value())
  blynk.virtual_write(7, v7.value())def blynk_task():  print('Blynk task')
  if len(roms) > 0:
    ds.convert_temp()
    t = ds.read_temp(roms[0])
    print('Temperature: {0:.2f}'.format(t))
    blynk.virtual_write(8, t)    blynk.on_connect(blynk_connected)blynk.set_user_task(blynk_task, 5000)
th.start_new_thread(blynk.run, ()) 