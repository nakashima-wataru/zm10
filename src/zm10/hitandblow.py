import random

def play_game():
    """ヒットアンドブローのメインゲーム関数"""

    # 1. コンピュータの答えを作成 (4桁のユニークな数字)
    digits = list("0123456789")
    random.shuffle(digits)
    answer = digits[:4]
    
    attempts = 0 # 挑戦回数を記録

    print("=== ヒットアンドブロー 開始 ===")
    print("4桁のユニークな数字を当ててください。")
    print("---------------------------------")
    
    while True:
        attempts += 1
        print(f"\n--- {attempts}回目の挑戦 ---")

        # 2. プレイヤーからの入力を受け取り、チェックする
        guess_str = input("4桁の数字を入力してください: ")

        # 入力形式のチェック
        if len(guess_str) != 4 or not guess_str.isdigit():
            print("エラー: 必ず4桁の数字を入力してください。")
            continue
        
        if len(set(guess_str)) != 4:
            print("エラー: 数字は重複しないように入力してください。")
            continue
        
        guess = list(guess_str)
        
        # 3. HitとBlowを判定する
        hits = 0
        blows = 0

        for i in range(4):
            if guess[i] == answer[i]:
                # 場所も数字も合っている場合 (Hit)
                hits += 1
            elif guess[i] in answer:
                # 場所は違うが数字が含まれている場合 (Blow)
                blows += 1
        
        # 4. 結果を表示し、正解か判定する
        print(f"結果: {hits} Hit, {blows} Blow")

        if hits == 4:
            print("\n🎉 おめでとうございます！正解です！")
            print(f"正解は「{''.join(answer)}」でした。")
            print(f"{attempts}回でクリアしました。")
            break

# --- プログラムの実行 ---
if __name__ == "__main__":
    play_game()