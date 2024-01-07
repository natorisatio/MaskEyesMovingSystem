import machine
import time

# パラメータ設定
MIC_PIN_NUMBER = 35  # マイクロフォン入力ピン番号
RED_LED_PIN_NUMBER = 4  # 赤色LEDピン番号
GREEN_LED_PIN_NUMBER = 16  # 緑色LEDピン番号
BLUE_LED_PIN_NUMBER = 17  # 青色LEDピン番号
ZERO_CROSSING_DURATION_MS = 100  # ゼロクロッシングの計測時間（ミリ秒）
CLICK_THRESHOLD_FREQUENCY = 100  # クリックとしてカウントする周波数の閾値
COUNT_DURATION_SECONDS = 3  # クリック数える秒数
DEBOUNCE_TIME_MS = 300  # デバウンス時間（ミリ秒）
SLEEP_AFTER_COUNT_SECONDS = 1  # カウント後のスリープ時間（秒）

# ピンの設定
mic_pin = machine.Pin(MIC_PIN_NUMBER, machine.Pin.IN)
red_led = machine.Pin(RED_LED_PIN_NUMBER, machine.Pin.OUT)
green_led = machine.Pin(GREEN_LED_PIN_NUMBER, machine.Pin.OUT)
blue_led = machine.Pin(BLUE_LED_PIN_NUMBER, machine.Pin.OUT)

# ゼロクロッシングをカウントする関数
def count_zero_crossings(pin, duration_ms):
    count = 0
    last_value = pin.value()
    end_time = time.ticks_add(time.ticks_ms(), duration_ms)
    
    while time.ticks_ms() < end_time:
        current_value = pin.value()
        if current_value != last_value:
            count += 1
            last_value = current_value
    
    return count

# LED色設定関数
def set_led_color(count):
    # クリック数に基づいてLEDの色を変更
    if count == 1:
        red_led.value(0)  # 赤色LED点灯
        green_led.value(1)
        blue_led.value(1)
    elif count == 2:
        red_led.value(1)
        green_led.value(0)  # 緑色LED点灯
        blue_led.value(1)
    elif count == 3:
        red_led.value(1)
        green_led.value(1)
        blue_led.value(0)  # 青色LED点灯
    else:
        red_led.value(1)  # LED消灯
        green_led.value(1)
        blue_led.value(1)


# メインループ
while True:
    click_count = 0
    start_time = time.time()

    # クリック音を数える
    while time.time() - start_time < COUNT_DURATION_SECONDS:
        zero_crossings = count_zero_crossings(mic_pin, ZERO_CROSSING_DURATION_MS)
        frequency = zero_crossings // 2
        if frequency >= CLICK_THRESHOLD_FREQUENCY:
            click_count += 1
            time.sleep(DEBOUNCE_TIME_MS / 1000)  # デバウンス

    set_led_color(click_count)  # LED色の設定
    print(click_count)
    time.sleep(SLEEP_AFTER_COUNT_SECONDS)  # スリープ
