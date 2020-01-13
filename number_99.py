answer = int(input("I am a magician and I know what the answer will be: "))
while (True):   
    if answer < 10 or answer > 49:
        print("The number chosen is not between 10 and 49")
        answer = int(input("I am choosing a number from 10-49, which is: "))
        continue
    else:
        break
factor = 99 - answer
print("Now I subtracted my answer from 99, which is " + str(factor))
friend_guess = int(input("Now you have to chose a number from 50-99, which is: "))
while (True):   
    if friend_guess < 50 or friend_guess > 99:
        print("The number chosen is not between 50 and 99")
        friend_guess = int(input("Now you have to chose a number from 50-99, which is: "))
        continue
    else:
        break
three_digit_num = factor + friend_guess
print("Now I added " + str(factor) + " and " + str(friend_guess) + " to get " + str(three_digit_num))
one_digit_num = three_digit_num//100
two_digit_num = three_digit_num - 100
almost_there = two_digit_num + one_digit_num
print("Now I added the hundreds digit of " + str(three_digit_num) + " to the tens and ones digit of " + str(three_digit_num) + " to get " + str(almost_there))
final_answer = friend_guess - almost_there
print("Now I subtracted your number, " + str(friend_guess) + " from " + str(almost_there) + " to get " + str(final_answer))
print("The final answer, " + str(final_answer) + " is equal to my answer from the beginning, " + str(answer))
