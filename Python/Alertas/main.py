import requests
import smtplib
import email.message

def enviar_email(cotacao):
    corpo_email = f"""
    <p>Dolar está abaixo de R$ 5.20 Cotação atual R$ {cotacao}</p>
    """
    
    msg = email.message.Message()
    msg['Subject'] = 'Dolar abaixo de 5.20'
    msg['From'] = 'wolneysp@gmail.com'
    msg['To'] = 'wolneysp@gmail.com'
    password = ''
    msg.add_header('Content-Type','text/html')
    msg.set_payload(corpo_email)
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')



url = 'http://economia.awesomeapi.com.br/json/last/USD-BRL'
response = requests.get(url)
response_dict = response.json()
cotacao = float(response_dict['USDBRL']['bid'])


if cotacao < 5.20:
    enviar_email(cotacao)


