from spellcheck import correct
lrs = 'speling is fin'
lss = correct(lrs.partition(' '))
print lss
print lrs
