from tkinter import Tk, Text, Scrollbar, Button

import openai

# Configura tu clave de API de OpenAI
openai.api_key = "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"

# Función para enviar una pregunta al chatbot y obtener una respuesta
def enviar_pregunta():
    pregunta = entrada_pregunta.get("1.0", 'end-1c')
    if pregunta:
        respuesta = obtener_respuesta_pregunta(pregunta)
        chat.config(state='normal')
        chat.insert('end', f"Usuario: {pregunta}\n")
        chat.insert('end', f"ChatGPT: {respuesta}\n\n")
        chat.config(state='disabled')
        entrada_pregunta.delete("1.0", 'end-1c')

def obtener_respuesta_pregunta(pregunta):
    # Llama a la API de GPT-3.5 para obtener una respuesta
    respuesta = openai.Completion.create(
        engine="text-davinci-002",
        prompt=pregunta,
        max_tokens=50,
        temperature=0.7
    )
    return respuesta.choices[0].text

# Configuración de la ventana de la aplicación
def send():
    enviar_pregunta()

base = Tk()
base.title("Chatbot")
base.geometry("400x500")
base.resizable(width=False, height=False)

# Crear ventana de chat
chat = Text(base, bd=0, bg="white", height="8", width="50", font="Arial")
chat.config(state='disabled')

# Enlazar scrollbar a la ventana de chat
scrollbar = Scrollbar(base, command=chat.yview, cursor="heart")
chat['yscrollcommand'] = scrollbar.set

# Crear botón para enviar mensajes
SendButton = Button(base, font=("Verdana", 12, 'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", fg='#ffffff', command=send)

# Cuadro para ingresar preguntas
entrada_pregunta = Text(base, bd=0, bg="white", width="29", height="5", font="Arial")

scrollbar.place(x=376, y=6, height=386)
chat.place(x=6, y=6, height=386, width=370)
entrada_pregunta.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

base.mainloop()
