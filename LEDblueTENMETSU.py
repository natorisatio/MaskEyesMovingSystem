import machine
import time
pin = machine.Pin(17, machine.Pin.OUT)

while True:
  pin.on()
  time.sleep_ms(2000)
  pin.off()
  time.sleep_ms(2000)
