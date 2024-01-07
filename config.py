# config.py

# ESPNOW関連の設定
ESPNOW_PEER_MAC = '24:0A:C4:00:00:00'  # 通信先デバイスのMACアドレス

# TFTディスプレイのピン設定
TFT_BL = 27   # バックライト制御
TFT_CS = 15   # チップセレクト
TFT_DC = 2    # データ/コマンド制御
TFT_MISO = 12 # SPI通信 MISO
TFT_MOSI = 13 # SPI通信 MOSI
TFT_SCLK = 14 # SPI通信 SCLK
TFT_RST = -1  # リセット（使用しない場合は-1）

# SDカードのピン設定
SD_CS = 5     # SDカード チップセレクト

# その他のセンサーやデバイスの設定
# 例: センサーの感度やモードなど
SENSOR_SENSITIVITY = 0.5
SENSOR_MODE = 1

# ロギングやデバッグに関する設定
DEBUG = True
LOG_LEVEL = 'INFO'

# アプリケーション固有の設定
# 例: メインループのディレイタイムやアプリケーションのバージョン
LOOP_DELAY = 1.0  # メインループのディレイタイム（秒）
APP_VERSION = '1.0.0'
