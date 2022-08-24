flag="mdg{...................................}"
f = []
for i in range(len(flag)):
    f.append(ord(flag[i]))
for i in range(4, len(flag), 1):
    f[i] ^= (f[i-1]+f[i-2])//3
for i in f:
    print(chr(i), end='')