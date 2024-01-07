from machine import Pin, SPI, SDCard
import os
from ili9341 import Display
from time import sleep
import network
import espnow

# SDカードの設定
def initialize_sd_card():
    sd = SDCard(slot=2)  # ESP32の場合、slot=2
    os.mount(sd, '/sd')
    files = os.listdir('/sd')
    print("Files on SD card:", files)

# ESPNOWの初期設定
def initialize_espn():
    wlan = network.WLAN(network.STA_IF)  # Wi-Fiをステーションモードに設定
    wlan.active(True)

    esp_now = espnow.ESPNow()
#    esp_now.init()

    # ESPNOWの追加設定（必要に応じて）
    # ...

    print("ESPNOW Initialized")

# TFTディスプレイの初期設定
def initialize_display():
    # ディスプレイの初期化コードをここに記述
    # 例: display = Display(spi, ...)
    print("Display Initialized")

def main():
    """メイン関数で各初期設定を呼び出す"""
    try:
        initialize_sd_card()
        initialize_display()
        initialize_espn()
    except Exception as e:
        print("Initialization error:", e)

if __name__ == "__main__":
    main()
