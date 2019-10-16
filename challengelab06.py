#! /usr/bin/env python3

def zodiac():
    print("*******Zodiac Signs******\n")
    print("NOTE: Please enter your month of birth complete.Day of you birth can be between 1-31:\n")
    #month= input("Write out your birth month: ")
    #day= int(input("Write the day you were born: "))
    continue1="y"

    while (continue1.lower == "y"):
        #print("*******Zodiac Signs******\n")
        #print("NOTE: Please enter your month of birth complete.Day of you birth can be between 1-31:\n")
        month= input("Write out your birth month: ")
        day= int(input("Write the day you were born: "))
         #   if continue1=="n":
         #       break
        if month.lower()=='march' and day>=21:
                print(' Your Zodiac Sign is Aries')
          #      break
        elif (month.lower()=='april' and day<=19):
                print(' Your Zodiac Sign is Aries')
           #     break
        elif month.lower=='april' and day>=20:
                print(' Your Zodiac Sign is Taurus')
            #    break
        elif month.lower()=='may' and day<=20:
                print(' Your Zodiac Sign is Taurus')
             #   break
        elif month.lower()=='may' and day>=21:
                print(' Your Zodiac Sign is Gemini')
              #  break
        elif month.lower()=='june' and day<=20:
                print(' Your Zodiac Sign is Gemini')
               # break
        elif month.lower()=='june' and day>=21:
                print(' Your Zodiac Sign is Cancer')
              #  break
        elif month.lower()=='july' and day<=22:
                print(' Your Zodiac Sign is Cancer')
               # break
        elif month.lower()=='july' and day>=23:
                print(' Your Zodiac Sign is Leo')
               # break
        elif month.lower()=='august' and day<=22:
                print(' Your Zodiac Sign is Leo')
               # break
        elif month.lower()=='august' and day>=23:
                print(' Your Zodiac Sign is Vigro')
               # break
        elif month.lower()=='september' and day<=22:
                print(' Your Zodiac Sign is Virgo')
               # break
        elif month.lower()=='october' and day<=22:
                print(' Your Zodiac Sign is Libra')
                #break
        elif month.lower()=='october' and day>=23:
                print(' Your Zodiac Sign is Scorpion')
               # break
        elif month.lower()=='november' and day<=21:
                print(' Your Zodiac Sign is Scorpion')
               # break
        elif month.lower()=='november' and day>=22:
                print(' Your Zodiac Sign is Sagittarius')
                #break
        elif month.lower()=='december' and day<=21:
                print(' Your Zodiac Sign is Sagittarius')
                #break
        else:
                print(f"{month} or {day} is not a correct entry.")
        continue1=input("Do you want to continue?(y/n) ")

zodiac()
