import smtplib

class sender():
#mail.nic.ru 587 465

    smtp_server = 'smtp.gmail.com'#input("Введите адрес SMTP-Сервера: ")
    smtp_port = 465 #int(input("Введите порт SMTP-Сервера: "))

    e_adress = 'emik219@gmail.com'#input("Введите свой адрес ЭП: ")
    e_pass = 'Emil4ik229'#input("Введите пароль ЭП: ")

    to = input("Кому отправить сообщение: ")

    e_text = input("Введите текст отправки: ")

    def connection():
        smtpObj = smtplib.SMTP(smtp_server,smtp_port)

        smtpObj.starttls()

        smtpObj.login(e_adress,e_pass)

    def spam():
        f = open('123.txt', 'r')

        line = f.readline()
        while line:
            smtpObj.sendmail(e_adress,line,"")
            print(line,end='')
            line = f.readline()
        f.close
        smtpObj.sendmail(e_adress,line,"")


    def sent(smtp_server,smtp_port,e_adress,e_pass,to,e_text):
        try:
            server = smtplib.SMTP_SSL(smtp_server,smtp_port)
            server.ehlo()
            server.login(e_adress, e_pass)
            server.sendmail(e_adress, to, e_text)
            server.close()

            return print('Email sent!')
        except:
            print('Something went wrong...')

    sent(smtp_server,smtp_port,e_adress,e_pass,to,e_text)
    