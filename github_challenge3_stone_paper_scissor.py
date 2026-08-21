import random
l=['stone','paper','scissor']
print("Stone-Paper-Scissor Game")
print("-----------------------")
print(l)
c=random.choice(l)
u = input("Enter your choice:")
if u.lower()==c:
    print(f"its a draw.\nYour choice: {u}\tcomputer choice: {c}")
elif c=='scissor' and u=='stone' or c=='stone' and u=='paper'or c=='paper' and u=='scissor':
    print(f"Your choice:{u}\t computer choice:{c}\nCongratulations ..You win...!")
else:
    print(f"Your choice:{u}\t computer choice:{c}\nComputer wins..!")
