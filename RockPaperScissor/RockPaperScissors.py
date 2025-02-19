from random import choice


class RocPapSci:
    @classmethod
    def play_game(cls):
        while True:
            com_score = 0
            user_score = 0
            for i in range(1, 4):
                if i == 3:
                    print("\n\t\t\t   Last Round")
                else:
                    print(f"\n\t\t\t\tRound {i}")
                __computer = ["rock", "paper", "scissor"]
                com_choice = choice(__computer)
                user_choice = input("Enter your choice ('rock', 'paper', 'scissor'):  ").lower()
                if com_choice == user_choice:
                    print(f"\nThis Round Was a Tie: (computer: {com_choice}, user: {user_choice})\n")
                # computer's winning possibilities
                elif ((com_choice == 'rock' and user_choice == 'scissor') or
                      (com_choice == 'paper' and user_choice == 'rock') or
                      (com_choice == 'scissor' and user_choice == 'paper')):
                    print(f"\nComputer win this Round: (computer: {com_choice}, user: {user_choice})\n")
                    com_score += 1
                # user's winning possibilities
                elif ((user_choice == 'rock' and com_choice == 'scissor') or
                      (user_choice == 'paper' and com_choice == 'rock') or
                      (user_choice == 'scissor' and com_choice == 'paper')):
                    print(f"\nUser win this Round: (computer: {com_choice}, user: {user_choice})")
                    user_score += 1
                else:
                    print("\nThe selection was invalid\n")
            print("#####GAME RESULTS#####")
            if com_score == user_score:
                print(f"The Game Was Tie!!\nScore(computer:{com_score}, user:{user_score})")
            elif com_score > user_score:
                print(f"Computer Won The Game!!\nScore(computer:{com_score}, user:{user_score})")
            else:
                print(f"User Won The Game!!\nScore(computer:{com_score}, user:{user_score})")
            new_game = input("\nWant to Play another game(y / n): ").lower()
            if new_game == 'n':
                print("\nCome Again, Thanks For playing")
                break
            elif new_game == 'y':
                print("\n**********##### New Game #####**********")
                pass
            else:
                print("\nInvalid selection!!\nStart Again")
                break


try:
    RocPapSci.play_game()
except Exception as err:
    print("Error Occurred!!", err)
