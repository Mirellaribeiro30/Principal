from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
   nome_usuario = "Visitante"
   html_content = f"""
   <!DOCTYPE html>
   <html>
   <head>
        <title>Saudação Personalizada</title>
   </head>
   <body>
        <h1>Olá, {nome_usuario}!</h1>
        <p>Bem-vindo à sua página personalizada.</p>
        <p>A data e hora atual é: {get_current_time()}</p>
   </body>
   </html>
   """
   return render_template_string(html_content)

def get_current_time():
   return datetime.now().strftime("%H:%M:%S em %d/%m/%Y")

if __name__ == '__main__':
   app.run(debug=True)