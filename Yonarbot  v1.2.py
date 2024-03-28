import telebot
import pandas as pd
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Contenido del archivo JSON como un diccionario
key_data = {
 "type": "service_account",
  "project_id": "python-sheets-tesel-418605",
  "private_key_id": "9997cf76d67390a6e5945c3b102a397bdf7e8cfb",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC3sJ2smVT6GuKa\nQiKJtlnK3brirmSpEuXZSZ1uFWo0XrH/gT8k/wh1kD88yyZ7X2ZmK8kFTFLkfYi4\nH01Nte2RVV7T2SLNoFNizM/VL+l3veDmHSTLnEDJJ4IeSZNXPZqP+1Pw/S5WbckQ\nZEilUsSU4a8M2Yx+bOz0aBjqMYi8wNllhcktN/ydBeS040A4oLRSpMuApLwqofvH\n7FhRIeJEGsU8hp8PmlYl2zSowbcVH8MnMk2mIE+pg3PX3B5gH2Z1buYEPwLl2qQs\nJLb2gdcgeSg+CY2z38Ye+EaK1Im9o5beUgT9RjYOWp6q2v2QK4BAJJ5p7ctPq5g/\nadkWb+21AgMBAAECggEAT6sCN8Go4XCXp1/XqvKzrxDL5VTNw6a2ma8b4IrZLS2E\n9dQQlvMlsBeH1c4mOov91YJYBTw9F2x6x6CL3pBxIP9tyWP7fEN05vz9hvDoyU5J\nJISvWL/EOXoxLQGsLcJCLwBKP9MPLd0fv0Q/XbSwHgJj8abJEGwduUMMy0YAkBw2\nCca2zWj73S00XwvJ6t2k63JcLwtGwKXJmVMMiCafz3ic5sEOVI4xUZXbzroD8U3c\nTBw5WtGx1KVZL1gsBwebrJB3IBWY8sFu0bR4LDb8zV1LIi1t4N6WLGJrlGO+U/I5\nDBjtch6bS/vqGyHboSbdnZaSpFY9g/0j/YiMYeBLYQKBgQD7MNDFcw9LRCUhr35/\nmDtAmrbGrtIfD4NJ4iAyaAk8g9h5Km2YxCQzLO0Gb2RbrVBvX/v3fyRw9KeU71hI\nnY5cxE/dhF+xA1uesKNHKaOQbTrmO6Nbo069bD24Pj0CVTmuJG06zR0y64+ksquk\nJOnvYxQKkxJ+OdT0hsVwP+RHawKBgQC7NPPWqF01AJrbjW0HnBO/Sn1VSfAaS+4c\nnUWAqr45CsG3plOhAu/Hd/cRAHafiV6o7PZzDbz/uJzqwSmYhfAxpJ51pyuKlhmO\n7dJ6Yr5ZGzHuuOa8Rn48sVq6MH9wbReUupiwcC2AsudPXANWOLmv8yWdUuwAHSnu\nfKd9kTCHXwKBgG+TrHi4dkexmmjPInqc7VzyHFQ+3XkMk/3iovig+9FUo3iW3x3n\nqkjNIPAl1MdgQgVm9m5mnJJMKpBejLGcwtr0HKHCJhtj6XOg9LYsicoiqvIP9a1D\n6jr79KJ9iu4ZW0i+R4LCD8FJn4HCF7oO55b9RK65y5IkMDL6FoOY7dbHAoGAZaYV\n9GtM2NewPiBnoCcmLcsDjMjt30l1TAI1V+zeBtkJYG+mnxmaGqPP+mJXBr8vL+gi\n1UwTYILcaTdjH5cyWbI5/EY+BS0FSa9mht+Q3Y8/qJCrcHWSW+AtFEX7HI+Pq0k6\nWSs/+c6qfFPI2AtK//e1Z9w7msA7IWx8AVlRkV8CgYEA2UTZw105lhjX5YYgoJvi\nEOoGXRIZZTkJbXffSz2/RuzpCDHrJ7hBVdlnnUhyqe/bPnxGp+IczlueVmZIxuJ5\nqaKH9myTMdYnQQhNuIQHPuN5BTz/iBsUc43+hZqFPHWiPdqRJz4B8EQlc4OcFNZf\nhqvAAoVoek+HGTWxbSRHxU8=\n-----END PRIVATE KEY-----\n",
  "client_email": "python-sheets-tesel@python-sheets-tesel-418605.iam.gserviceaccount.com",
  "client_id": "109625425559694059775",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/python-sheets-tesel%40python-sheets-tesel-418605.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

# Escribe aquí el ID de tu documento:
SPREADSHEET_ID = '1-g7spsC86oAVpsiNEspaJiwTyOW8vvIJdL0MrIM-phU'

creds = None
creds = service_account.Credentials.from_service_account_info(key_data, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

bot = telebot.TeleBot("5951477157:AAEIwwrWlOgfB5qE_AXClfejCr8HX8_AbUY", parse_mode=None) 

# # Función para obtener el rango de la hoja de cálculo y formatearlo como tabla
# def get_range_as_table():
#     result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='Hoja 1!A1:B8').execute()
#     values = result.get('values', [])
#     if not values:
#         return "No se encontraron datos en el rango especificado."
#     else:
#         df = pd.DataFrame(values[1:], columns=values[0])
#         table_str = df.to_string(index=False)
#         return "```\n" + table_str + "\n```"
    
def get_range_as_table():
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='Hoja 1!A1:B8').execute()
    values = result.get('values', [])
    if not values:
        return "No se encontraron datos en el rango especificado."
    else:
        df = pd.DataFrame(values[1:], columns=values[0])
        table_str = df.to_string(index=False, justify='left')  # Alinea la segunda columna a la izquierda
        return "```\n" + table_str + "\n```"


# Manejar el comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, get_range_as_table())

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
