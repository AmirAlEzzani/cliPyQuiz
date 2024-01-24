print("Welcome to my CLI quiz!")

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    print("ok, maybe next time!")
    quit()

print("Let's play!")

numCorrect = 0

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    numCorrect = numCorrect+1
else:
    print('incorrect')

answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('correct!')
    numCorrect = numCorrect+1
else:
    print('incorrect')

answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory":
    print('correct!')
    numCorrect = numCorrect+1
else:
    print('incorrect')

answer = input("what does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('correct!')
    numCorrect = numCorrect+1
else:
    print('incorrect')

print("You got " + str(numCorrect) + "/4 questions correct!")
print("Your score is "+ str(numCorrect/4*100)+"%")