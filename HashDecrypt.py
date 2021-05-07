import hashlib
import time
try:
    enc = input('wordlist file name: ')
    wrd = open(enc, 'r')
    wrd1 = open(enc, 'r')
    enc = open(input('hash-file name: '), 'r')
except:
    print('no file with this names found')
    for _ in range(10,0,-1):
        print(f'exitting in {_} seconds')
        time.sleep(1)
    quit()
password = [kk.strip('\n') for kk in enc]
print(password)
enc.close()
allowbreak = False
k = 0
aaa = []
l = wrd1.read().count('\n')+1
wrd1.close()
for i in wrd:
    if allowbreak:
        break
    i = i.strip('\n')
    i1 = hashlib.md5(i.encode('utf-8').strip()).hexdigest()
    i2 = hashlib.sha1(i.encode('utf-8').strip()).hexdigest()
    i3 = hashlib.sha256(i.encode('utf-8').strip()).hexdigest()
    k += 1
    print(f'trying {k} of {l}')
    for v in password:
        if v == i1:
            aaa.append(f'md5 : {v} : {i}')
            password.remove(v)
        if v == i2:
            aaa.append(f'sha1 : {v} : {i}')
            password.remove(v)
        if v == i3:
            aaa.append(f'sha256 : {v} : {i}')
            password.remove(v)
        if len(password) <= 0:
            allowbreak = True
wrd.close()
for i in aaa:
    print(i)
    print()
    print()
time.sleep(999)
# thediamondx13
