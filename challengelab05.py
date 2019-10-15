#!/usr/bin/env python3

hero_dict={"Flash":{"Speed": "Fastest", "Intelligence": "Lowest", "Strength": "Lowest"}, "Batman":{"Speed": "Slowest", "Intelligence": "Highest", "Strength": "Money"}, "Superman":{"Speed": "Fast", "Intelligence": "Average", "Strength": "Strongest"}}


char_name=input("Which character do you want to know about?(Flash, Batman, Superman) ")
char_stat=input("What statistic do you want to know about?(Strength, Speed, or Intelligence) ")


print(char_name,"'s",char_stat," is: ", hero_dict[char_name][char_stat])

#or
# print)f"{char_name}'s {char_stat} is: {hero_dict[char_name][char_stat]}")
