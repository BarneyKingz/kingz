print("Hey Welcome To D-Kingz Quiz")

playing = input("Do You Want To Play This Game? ")
if playing.lower() != "yes":
    quit()
print("Alright!, let's play on")
score = 0

answer = input("what does CPU stands for? ").lower()
if answer == "central processing unit":
    print("correct")
    score += 1

else:
    print("incorret")

answer = input("what does maths stands for? ").lower()
if answer == "mathematics":
    print("correct")
    score += 1

else:
    print("incorret")

answer = input("what does ATM stands for? ").lower()
if answer == "automated teller machine":
    print("correct")
    score += 1

else:
    print("incorret")

answer = input("what does ROM stands for? ").lower()
if answer == "read only memory":
    print("correct")
    score += 1

else:
    print("incorret")

answer = input("what does AOO stands for? ").lower()
if answer == "ayo oluwayomi olaoluwa":
    print("correct")
    score += 1

else:
    print("incorret")

answer = input("what does MAO stands for? ").lower()
if answer == "makanjuola ayomide odunayo":
    print("correct")
    score += 1

else:
    print("incorret")
answer = input("what does IRS stands for? ").lower()
if answer == "international relation studies":
    print("correct")
    score += 1

else:
    print("incorret")

answer = input("what does AFIT stands for? ").lower()
if answer == "airforce institute of technology":
    print("correct")
    score += 1

else:
    print("incorret")
answer = input("what does GSU stands for? ").lower()
if answer == "general studies unit":
    print("correct")
    score += 1

else:
    print("incorret")
answer = input("what does WHO stands for? ").lower()
if answer == "world health orginization":
    print("correct")
    score += 1

else:
    print("incorret")
answer = input("what is the name of afit current commandant ? ").lower()
if answer == "even me i no no am":
    print("correct")
    score += 1

else:
    print("incorret")
answer = input("what is the name of afit ex-commandant ? ").lower()
if answer == "oga jemitola":
    print("correct")
    score += 1

else:
    print("incorret")
answer = input("what what is the name of afit commandant before oga jemitola? ").lower()
if answer == "oga ma yakubu":
    print("correct")
    score += 1

else:
    print("incorret")
answer = input("how many degree courses is afit currently offering? ").lower()
if answer == "twenty three":
    print("correct")
    score += 1

else:
    print("incorret")
answer = input("which year did afit start offering degree programs? ").lower()
if answer == "year twenty eighteen":
    print("correct")
    score += 1

else:
    print("incorret")
answer = input("what year did year afit get acreditated ? ").lower()
if answer == "year twenty seventeen":
    print("correct")
    score += 1

else:
    print("incorret")
answer = input("who is the current president of nigeria? ").lower()
if answer == "president bola ahmed tinubu":
    print("correct")
    score += 1

else:
    print("incorret")
answer = input("who is nigeria's ex-president? ").lower()
if answer == "general mohammed buhari":
    print("correct")
    score += 1

else:
    print("incorret")

    answer = input("whats the most popular engineering course in afit? ").lower()
if answer == "aerospace engineering":
    print("correct")
    score += 1

else:
    print("incorret")

answer = input("how many years is engineering courses in afit? ").lower()
if answer == "five years":
    print("correct")
    score += 1

else:
    print("incorret")

    answer = input("how many semesters are there in a university session? ").lower()
if answer == "two semesters":
    print("correct")
    score += 1

else:
    print("incorret")

print("congrts you got " + str(score) + " questions correct")

print("congrts you got " + str((score/21)*100) + "%.")
      
print("thank you for playing the KINGZ quiz i hope u had a good time")
