import hashlib
import time
try:
    pas = open(input('hash file --> '), 'r')
    wrd = open(input('wordlist file --> '), 'r')
except:
    print('wrong file name')
    for _ in range(5,0,-1):
        print(f'exit in {_} seconds')
        time.sleep(1)
    quit()
passwd = [g.strip('\n') for g in pas]
pas.close()
k = 0
decrypted = []
allowbreak = False
print('if number will increase all is normal')
for _ in range(3,0,-1):
    print(f'{_}...')
    time.sleep(1.5)
for i in wrd:
    if allowbreak:
        break
    i = i.strip('\n').strip()
    i1 = hashlib.md5(i.encode('utf-8')).hexdigest()
    i2 = hashlib.sha1(i.encode('utf-8')).hexdigest()
    i3 = hashlib.sha256(i.encode('utf-8')).hexdigest()
    i4 = hashlib.sha512(i.encode('utf-8')).hexdigest()
    k += 1
    print(f'===>{k}')
    for dd in passwd:
        if dd == i1:
            decrypted.append(f'MD5 : {dd} : {i}')
            passwd.remove(dd)
        elif dd == i2:
            decrypted.append(f'SHA-1 : {dd} : {i}')
            passwd.remove(dd)
        elif dd == i3:
            decrypted.append(f'SHA-256 : {dd} : {i}')
            passwd.remove(dd)
        elif dd == i4:
            decrypted.append(f'SHA-512 : {dd} : {i}')
            passwd.remove(dd)
        if len(passwd) == 0:
            allowbreak = True
wrd.close()
for end in passwd:
    print()
    print(f'{end} : No results')
    print()
for end in decrypted:
    print()
    print(end)
    print()
print('--->  finished  <---')
time.sleep(999)
