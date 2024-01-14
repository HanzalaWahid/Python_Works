import random

Upper_Case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_Case = "abcdefghijklmnopqrstuvwxyz"
Number = "123456789"
Special_character = "[,{,',#,@,/,"

All_character  = Upper_Case + lower_Case + Special_character + Number
length = 16
password = "".join((random.sample(All_character,length)))
print(password)
