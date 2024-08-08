str='India is My Love'
print(' '.join([str.split() [ind] for ind in range(len(str.split())-1,-1,-1)]))