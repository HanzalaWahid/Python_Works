s = "We are Developers \n We made programs solve bug \n Life of a programmer is Absolutely Worse \n We find Bugs and Debug then."
# Writing to a file
# with open("open.txt", "w") as f:
#     f.write(s)
#
# fp = open("open.txt", "w")
# fp.write(s)
# fp.close()


# Reading to a file
# with open("open.txt", "r") as f:
#     a = f.read()
#     print(a)
fp = open("open.txt", "r")
a = fp.read()
print(a)
fp.close()

# Append to a file
with open("open.txt", "a") as f:
    a = f.write("HEY! ITS Hanzala here \n")
    # print(a)
fp = open("open.txt", "a")
a = fp.write("HELLO")
# print(a)
fp.close()
