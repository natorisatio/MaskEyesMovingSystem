import machine
import time

# パラメータ設定
MIC_PIN_NUMBER = 35  # マイクロフォン入力ピン番号
RED_LED_PIN_NUMBER = 4  # 赤色LEDピン番号
GREEN_LED_PIN_NUMBER = 16  # 緑色LEDピン番号
BLUE_LED_PIN_NUMBER = 17  # 青色LEDピン番号
ZERO_CROSSING_DURATION_MS = 100  # ゼロクロッシングの計測時間（ミリ秒）
CLICK_THRESHOLD_FREQUENCY = 100  # クリックとしてカウントする周波数の閾値
DEBOUNCE_TIME_MS = 300  # デバウンス時間（ミリ秒）

# ピンの設定
mic_pin = machine.Pin(MIC_PIN_NUMBER, machine.Pin.IN)
red_led = machine.Pin(RED_LED_PIN_NUMBER, machine.Pin.OUT)
green_led = machine.Pin(GREEN_LED_PIN_NUMBER, machine.Pin.OUT)
blue_led = machine.Pin(BLUE_LED_PIN_NUMBER, machine.Pin.OUT)

# ゼロクロッシングをカウントする関数
def count_zero_crossings(duration_ms):
    count = 0
    last_value = mic_pin.value()
    end_time = time.ticks_add(time.ticks_ms(), duration_ms)
    
    while time.ticks_ms() < end_time:
        current_value = mic_pin.value()
        if current_value != last_value:
            count += 1
            last_value = current_value
    
    return count

# LED色設定関数
def set_led_color(mode, count=0):
    if mode == 'command':
        green_led.value(0)  # 緑色LED点灯
        red_led.value(1)
        blue_led.value(1)
    elif mode == 'red':
        green_led.value(1)
        red_led.value(0)  # 赤色LED点灯
        blue_led.value(1)
    elif mode == 'blue':
        green_led.value(1)
        red_led.value(1)
        blue_led.value(0)  # 青色LED点灯
    elif mode == 'yellow':
        red_led.value(0)  # 赤色LED点灯
        green_led.value(0)  # 緑色LED点灯
        blue_led.value(1)  # 黄色表示
    else:
        green_led.value(1)  # LED消灯
        red_led.value(1)
        blue_led.value(1)

# メインループ
while True:
    command_mode = False
    set_led_color('off')  # 初期状態でLED消灯

    # コマンドモードのアクティベーションの確認
    if count_zero_crossings(ZERO_CROSSING_DURATION_MS) >= CLICK_THRESHOLD_FREQUENCY:
        command_mode = True
        set_led_color('command')  # コマンドモードのLED（緑）点灯
        time.sleep(DEBOUNCE_TIME_MS / 1000)  # デバウンス

    if command_mode:
        start_time = time.time()
        click_count = 0

        # クリック数を数える
        while time.time() - start_time < 2:  # 2秒間クリックを待つ
            if count_zero_crossings(ZERO_CROSSING_DURATION_MS) >= CLICK_THRESHOLD_FREQUENCY:
                click_count += 1
                time.sleep(DEBOUNCE_TIME_MS / 1000)  # デバウンス

        # クリック数に応じてLEDの色を設定
        if click_count == 1:
            set_led_color('red')
        elif click_count == 2:
            set_led_color('blue')
        elif click_count == 3:
            set_led_color('yellow')
 
        else:
            continue  # クリックがなければコマンドモード終了

        time.sleep(2)  # LED色の表示時間

# このプログラムは、マイクロコントローラボード上で動作することを想定しています。
