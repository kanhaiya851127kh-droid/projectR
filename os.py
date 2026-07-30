import random 
import os 

number = random.randint(1, 10)
guess = input("Guess the number between 1 and 10: ")
guess = int(guess)

if guess  == number:
    print("you won !")
else:
  print("you lost ! ")
  print("currect number was :",number)

  #include<stdio.h>
int main() {
  int currentAge, electionYear;
  scanf("%d %d", &currentAge, &electionYear);
  //Age in election year = Current age + (Election year - 2026)
  currentAge + (electionYear - 2026) >= 18 ? printf("Eligible") : printf("Not Eligible");
  return 0;
}