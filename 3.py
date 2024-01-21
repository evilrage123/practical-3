#password creater
import random 
length = 8
i = 1
char_set = 'abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ123456789!@#$%^&*'
password = ''
while(i<=length):
    password = password + random.choice(char_set)
    i=i+1
fh = open('pactical3.txt','w')
fh.write(password)
fh.close()