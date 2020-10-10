import smtplib

#mail.nic.ru 587 465
smtp_server = input("Введите адрес SMTP-Сервера: ")
smtp_port = int(input("Введите порт SMTP-Сервера: "))

e_adress = input("Введите свой адрес ЭП: ")
e_pass = input("Введите пароль ЭП: ")

e_text = input("Введите текст отправки")

smtpObj = smtplib.SMTP(smtp_server,smtp_port)

smtpObj.starttls()

smtpObj.login(e_adress,e_pass)

f = open('123.txt', 'r')

line = f.readline()
while line:
    smtpObj.sendmail(e_adress,line,"")
    print(line,end='')
    line = f.readline()
f.close

print("Jobs Done!!!")


