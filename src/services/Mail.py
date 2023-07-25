import win32com.client as win32
import pythoncom

def send_email(subject, body, recipient_email):
    pythoncom.CoInitialize()

    outlook_app = win32.Dispatch('Outlook.Application')
    mail = outlook_app.CreateItem(0)  # 0: Email
    mail.Subject = subject
    mail.Body = body
    mail.To = recipient_email
    mail.Send()
    pythoncom.CoUninitialize()

# Datos para el correo electrónico
# recipient_email = 'Harrydlopez@itsa.edu.co'
# subject = 'Cambio de contraseña'
# body = 'la contraseña es miguel123'

# # Enviar el correo electrónico
# send_email(subject, body, recipient_email)
