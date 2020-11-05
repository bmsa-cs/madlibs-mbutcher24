"""
MadLibs
Author: Mallory Butcher
Period/Core: 3


"""
print("Let's play Silly Sentences!\n")

story = int(input("What is your favorite whole number? "))

if story%2==0:
  company = input("\nEnter the name of a company: ")
  pt_verb = input("Enter a past-tense verb: ")
  drink = input("Enter the name of a drink: ")
  person_one = input("Enter a name: ")
  ing_verb = input("Enter a verb ending with \"ing\": ")
  person_two = input("Enter another name: ")
  job = input("Enter the name of a job: ")
  print("\nYou want to know why I want to quit my job at {}? \nWell, I got {} in an elevator the other day. \nI was just bringing the boss some {} and suddenly, the lights went out. \n{} was standing next to me. \nThat idiot started {} the ever-present-not-moving door. \nThe entire thing kept shaking. \nThe boss's {} flew out of my hands and {} had to change their shirt. \nThe {} eventually got us out, but oh my, I never want to do that again! \nYou can see why I’m quitting... \tRight?".format(company, pt_verb, drink, person_one, ing_verb, drink, person_two, job))

else:
  print("pfft {} {}".format(34455, 444))
  print(f'pifffieoijfe {story}')

print("Thank you for playing!" + "\nTry again to get a different story!")