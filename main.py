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
  season = input("\nEnter a season: ")
  body_part = input("Enter a part of your body: ")
  friend = input("Enter the name of a friend: ")
  food = input("Enter a food: ")
  animal = input("Enter an animal: ")
  liquid = input("Enter a liquid: ")
  print(f"The beach in the {season} is so fun! \nMy {body_part} sunk into the sand, just beneath the waves. \n{friend} sat at the shore, tossing {food} at the pesky seagulls. \nA young girl crossed the waves on a {animal} float. \nSuddenly, {liquid} pelted my back! \nI turned to see {friend} behind me, squirt gun in hand. \nI smiled, sprinting back across the beach. {friend} is so going down!")

print("\nThank you for playing!" + "\nTry again to get a different story!")