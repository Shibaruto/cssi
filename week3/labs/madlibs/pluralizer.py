word = "In NYC {0}, with {1} of times."
print word
p = raw_input("Enter a word: ")
g = int(raw_input("Enter a number:"))
if g == 0 or g >= 1:
    nword = p+"s"
    print word.format(nword,g)
else:
    print word.format(p,g)
