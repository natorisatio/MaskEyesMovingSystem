"""ILI9341 demo (images)."""
from time import sleep
from ili9341 import Display
from machine import Pin, SPI

def test():
    """Test code."""
    # Baud rate of 20000000 seems about the max
    spi = SPI(1, baudrate=20000000, sck=Pin(14), mosi=Pin(13))
    # ディスプレイの初期化
    display = Display(spi, dc=Pin(2), cs=Pin(15), rst=Pin(17))
    # スリープモードを解除
    display.sleep(False)
    print("okita")
    
    # ピンの初期化（17ピンを出力として設定）
    rst_pin = Pin(27, Pin.OUT)

    # 17ピンをハイに設定
    rst_pin.value(1)
    

    display.draw_image('images/RaspberryPiWB128x128.raw', 0, 0, 128, 128)
    sleep(2)
    print("gazou-1")

    display.draw_image('images/MicroPython128x128.raw', 0, 129, 128, 128)
    sleep(2)
    print("gazou-2")

    display.draw_image('images/Tabby128x128.raw', 112, 0, 128, 128)
    sleep(2)
    print("gazou-3")

    display.draw_image('images/Tortie128x128.raw', 112, 129, 128, 128)

    sleep(9)
    print("gazou-4")

    # ディスプレイのリソースをクリーンアップ
    display.cleanup()
    print("souji")
    
    # 17ピンをローに設定
    rst_pin.value(0)

test()
