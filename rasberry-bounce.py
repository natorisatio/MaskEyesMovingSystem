from machine import Pin, SPI
import ili9341
from time import sleep

# ピンの初期化
rst_pin = Pin(27, Pin.OUT)
rst_pin.value(1)  # 17ピンをハイに設定

# SPIバスとピンの初期化
spi = SPI(1, baudrate=60000000, sck=Pin(14), mosi=Pin(13))
display = ili9341.Display(spi, dc=Pin(2), cs=Pin(15), rst=Pin(17))

# 画面を白色でクリア
display.fill_rectangle(0, 0, 240, 320, ili9341.color565(255, 255, 255))

# 画像ファイルの読み込み関数
def load_image(path, width, height):
    with open(path, "rb") as file:
        return file.read(width * height * 2)

# スプライトデータの読み込み
sprite_data = load_image("/images/RaspberryPiWB128x128.raw", 128, 128)

# スライドアニメーションの設定
y = 0  # 初期Y座標
direction = 1  # 移動方向 (1: 下へ, -1: 上へ)

while True:  # 無限ループ
    x = (240 - 128) // 2  # 中央にX座標を設定
    display.draw_sprite(sprite_data, x, y, 128, 128)  # スプライトの表示
    sleep(0.05)  # 少し待つ

    y += direction * 6  # Y座標を更新

    # 反転条件のチェック
    if y <= 0 or y >= (320 - 128):
        direction *= -1  # 移動方向を反転
