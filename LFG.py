import numpy
# This is a Simple Lagged Fibonacci Generator using n=7 j=3, k=7 , m=10
list_key = []
j = 3
k = 7
s = [6, 4, 2, 1, 8, 9, 3]
for n in range(10):
    for i in range(len(s)):
        if i == 0:
            out = (s[j-1] + s[k-1]) % 100 # the pseudorandom output
        elif 0 < i < 6:
            s[i] = s[i+1] # shift the array
            print("s[",i,"]", s[i])
        else:
            s[i] = out   # append the result to last position in the sequence
            list_key.append(out)


print(list_key)

#sequence: numpy.ndarray = numpy.random.randint(-128, 128, 1000, dtype=int)
#print(sequence)