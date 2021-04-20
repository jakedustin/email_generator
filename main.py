import sys
import yagmail

name = sys.argv[1]
num = sys.argv[2]
date = sys.argv[3]
amount = sys.argv[4]

with open('source.txt') as f:
    mail = f.read()

    send = mail.format(n=name, i=num, d=date, a=amount)
    print(send)
