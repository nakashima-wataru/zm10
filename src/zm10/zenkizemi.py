import requests
import json

# --- 設定 ---
# 天気予報 API (livedoor 天気互換) のURL
# 大阪のcityコード「270000」を指定
API_URL = "https://weather.tsukumijima.net/api/forecast?city=270000"


# --- メインの処理 ---
def get_weather_forecast():
    """
    天気予報 API（livedoor 天気互換）から天気予報を取得し、表示する関数
    """
    try:
        # APIにリクエストを送信し、レスポンスを取得
        response = requests.get(API_URL)
        # ステータスコードが200（成功）以外の場合はエラーを発生させる
        response.raise_for_status()

        # レスポンスをJSON形式に変換
        weather_data = response.json()

        # --- 今日の天気情報を取得して表示 ---
        today_weather = weather_data["forecasts"][0]

        print(f"📍 {weather_data['location']['city']}の天気予報")
        print(f"発表元: {weather_data['publicTimeFormatted']}")
        print("-" * 30)

        print(f"【今日の天気 - {today_weather['dateLabel']} ({today_weather['date']})】")
        print(f"☀️ 天気: {today_weather['telop']}")

        # 気温情報
        temp = today_weather['temperature']
        min_temp = temp['min']['celsius'] if temp['min'] else 'N/A'
        max_temp = temp['max']['celsius'] if temp['max'] else 'N/A'
        print(f"🌡️ 最低気温: {min_temp} ℃ / 最高気温: {max_temp} ℃")

        # 降水確率
        chance_of_rain = " | ".join([
            f"{k.replace('T', '')}時台: {v}"
            for k, v in today_weather['chanceOfRain'].items()
        ])
        print(f"💧 降水確率: {chance_of_rain}")

        print("-" * 30)
        print("詳細:")
        print(weather_data['description']['text'])
        print("-" * 30)


    except requests.exceptions.HTTPError as e:
        # APIからのエラーレスポンスを処理
        print(f"エラー: 天気情報を取得できませんでした。ステータスコード: {e.response.status_code}")
    except requests.exceptions.RequestException as e:
        # ネットワーク接続の問題などを処理
        print(f"エラー: リクエストを送信できませんでした。 {e}")
    except KeyError:
        print("エラー: 受け取ったデータの形式が正しくありません。")
    except IndexError:
        print("エラー: 天気予報のデータが見つかりませんでした。")


if __name__ == "__main__":
    get_weather_forecast()