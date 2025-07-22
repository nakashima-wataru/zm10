import datetime

def main():
    print("生年月日を入力してください")
    birthdate = input("入力(yyyy/mm/dd)：")

    try:
        parts = birthdate.split("/")
        birth_year = int(parts[0])
        birth_month = int(parts[1])
        birth_day = int(parts[2])

        dt = datetime.date.today()
        age = dt.year - birth_year

        if (birth_month, birth_day) > (dt.month, dt.day):
            age -= 1
        return (f"あなたの年齢は{age}歳です。")
    
    except (ValueError, IndexError):
        return ("エラー: 入力形式が正しくありません。")

if __name__ == "__main__":
    result = main()
    print(result)