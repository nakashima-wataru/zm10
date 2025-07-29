import random

def play_game():
    


    digits = list("0123456789")
    random.shuffle(digits)
    answer = digits[:4]
    
    attempts = 0 

    print("=== ヒットアンドブロー 開始 ===")

    print("---------------------------------")
    
    while True:
        attempts += 1
        print(f"--- {attempts}回目の挑戦 ---")

        guess_str = input("4桁の数字を入力してください: ")


        guess = list(guess_str)
        
        hits = 0
        blows = 0

        for i in range(4):
            if guess[i] == answer[i]:
                
                hits += 1
            elif guess[i] in answer:
            
                blows += 1
        
        print(f"結果: {hits} Hit, {blows} Blow")

        if hits == 4:
            print("おめでとうございます！正解です！")
            print(f"正解は「{''.join(answer)}」でした。")
            break

if __name__ == "__main__":
    play_game()