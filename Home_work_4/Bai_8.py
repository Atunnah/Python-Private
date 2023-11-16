import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def play_round(player):
    while True:
        n = int(input("Nhap n: "))
        k = int(input("Nhap k (k < n): "))
        if n > k:
            break
        else: print("Khong thoa man dieu kien n > k. Vui long nhap lai")
    turns = 0
    faults1 = 0
    faults2 = 0
    while n > 0:
        while True:
            current_turn = int(input(f"Nhap 1 so tu 1 den {min(n, k)}: "))
            if 1 <= current_turn <= min(n, k):
                break
            else: 
                print(f"Khong thoa man dieu kien nhap tu 1 den {min(n, k)}. Vui long nhap lai.")
                if turns % 2 == 0:
                    faults1 += 1
                else:
                    faults2 += 1
        n -= current_turn
        turns += 1
    print(f"{player} thua trong turn {turns}")
    return turns, faults1, faults2

def main():
    rounds = 1
    player1_wins = 0
    player2_wins = 0

    while True:
        clear_screen()
        print("Round: ", rounds)
        player_turns, player1_faults, player2_faults = play_round("Player")
        if player_turns % 2 != 0:
            player1_wins += 1
            print("Player 1 thang round nay.")
        else:
            player2_wins += 1
            print("Player 2 thang round nay")
        continue_game = input("Tiep tuc game (YES/NO)? ").upper()
        if continue_game == "NO":
            break
        rounds += 1
    print("Thong ke: ")
    player_wins = 0
    i = 0
    if player1_wins > player2_wins:
        print("Player 1 thang")
        player_wins = player1_wins
        i = 1
    elif player1_wins < player2_wins:
        print("Player 2 thang")
        player_wins = player2_wins
        i = 2
    else:
        if player1_faults > player2_faults:
            print("Player 2 thang")
        elif player1_faults < player2_faults:
            print("Player 1 thang")
        else:
            print("Hai nguoi choi hoa")
    if i != 0:
        print(f"Cac round ma Player {i} da thang: ", end=" ")
        print(", ".join(map(str, range(1, player_wins + 1))))
    else:
        print("Khong co round thang nao")

if __name__ == "__main__":
    main()
