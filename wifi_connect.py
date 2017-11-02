import network
import time
wlan=None
def connect():
  global wlan
  wlan=network.WLAN(network.STA_IF) 
  wlan.active(True)
  wlan.connect('<SSID>', '<PASSWORD>')
  _connected = False
  _count = 0
  while not wlan.isconnected():
    time.sleep(1)
    print('Waiting for connect')
    _count = _count +1
    if _count == 10:
      break;
  if wlan.isconnected():
    print('IPAddress: {}'.format(wlan.ifconfig()[0]))
  else:
    print('Can not connect WIFI')
  
def get_ip():
  if wlan.isconnected():
    return wlan.ifconfig()[0]
  else:
    return None

