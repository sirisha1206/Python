import random
num1 = random.randrange(0,9,1)
print(num1)

while True:
    num2 = input('Enter the guess number in between 0-9:')
    num2 = int(num2);
    if(num2 < num1):
        print('Your answer is low than  required')
    elif (num2 > num1):
        print('Your answer is high than  required')
    else:
        print('Your answer is PERFECT!! Congratulations!!')
        break
