from spellcheck import correct
lrs = 'speling is cool'
lss = correct(lrs)

dict = {}
list = []
newlist = []

words = lrs.split()

for word in words:
    list.append(word)

for item in list:
    corr = correct(item)

    newlist.append(corr)

print lrs
print ' '.join(newlist)




