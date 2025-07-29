import datetime

WAREKI_MAP = {
    'R': 2018, '令和': 2018,
    'H': 1988, '平成': 1988,
    'S': 1925, '昭和': 1925,
    'T': 1911, '大正': 1911,
    'M': 1867, '明治': 1867,
}


def main():
    print("生年月日を入力してください")
    birthdate = input("入力(yyyy/mm/dd)：")

    try:
        parts = birthdate.split("/")

        year_part = parts[0]
        birth_month = int(parts[1])
        birth_day = int(parts[2])

        if year_part.isdigit():
            birth_year = int(year_part)

        else:
            era = ""
            era_year_str = ""
            for i, char in enumerate(year_part):
                if char.isdigit():
                    era = year_part[:i].upper() 
                    era_year_str = year_part[i:] 
                    break

            if era not in WAREKI_MAP:
                return f"エラー: 不明な元号です。「{era}」"
            
            
            birth_year = WAREKI_MAP[era] + int(era_year_str)

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