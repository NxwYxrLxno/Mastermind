import random

def get_guess():
    while True:
        try:
            user_input = input("Enter a number: ")
            user_list = []
            for item in user_input:
                user_list.append(int(item))

            illegal_num1 = False
            illegal_num2 = False
            illegal_length = False

            for number in user_list:
            #First Condition: To be in the range 1-7
                if number > 7 and number < 1:
                    illegal_num1 = True

            #Second Condition: To be a unique value
                if user_list.count(number) > 1:
                    illegal_num2 = True

            #Third Condition: Length of the guess should be 4
                if len(user_list) != 4:
                    illegal_length = True


            if illegal_num1:
                print "The number is not in range 1-7"
            if illegal_num2:
                print "The number should be unique"
            if illegal_length:
                print "The guess should have a length of 4"
            if not illegal_num1 and not illegal_num2 and not illegal_length:
                return user_list

        except ValueError:
            print "Error 404. Enter only numbers"



def check_values(user_list,computer_list):
    response=[]
    for numb in user_list:
        if numb in computer_list:
            if computer_list.index(numb)==user_list.index(numb):
                response.append("Red")
            else:
                response.append("White")
        else:
            response.append("Black")
    random.shuffle(response)
    print response
    return(check_win(response))



def check_win(response_list):
    win=0
    for item in response_list:
        if item=="RED":
            win=win+1
    if win==4:
        print("You Won")
    else:
        print("Trying")



def create_comp_list():
    mylist=[]
    while len(mylist)<4:
        random_num=random.randint(1,7)
        if random_num not in mylist:
            mylist.append(random_num)
    return mylist



def play_game():
    game_list=create_comp_list()
    total_guesses=0

    while total_guesses<5:
        print"Guesses Remaning "+str(5-total_guesses)
        user_input= get_guess()

        if check_values(game_list,user_input)==4:
            break
        total_guesses=total_guesses+1
    if total_guesses==5:
        print "sorry thats all the guesses you get"
        print "this is the correct answer"
        print game_list
    print "Thanks for Playing"




# Print directions telling the user how to play the game. Then call the
# play_game function to begin the game, using all of your prewritten functions.



play_game()
