import tkinter as tk
import pyshorteners

def encurtar_url():
    url_original = entrada.get()
    if url_original:
        try:
            s = pyshorteners.Shortener()
            url_curta = s.tinyurl.short(url_original)
            label_resultado.config(text=url_curta)
            botao_copiar.config(state=tk.NORMAL)
        except Exception as e:
            label_resultado.config(text="Erro ao encurtar a URL")
            botao_copiar.config(state=tk.DISABLED)

def copiar_url():
    url = label_resultado.cget("text")
    janela.clipboard_clear()
    janela.clipboard_append(url)
    janela.update()
    label_resultado.config(text=f"Copiado: {url}")

# Criar janela principal
janela = tk.Tk()
janela.title("Encurtador de URL")
janela.geometry("400x200")

# Entrada de URL
tk.Label(janela, text="Digite a URL para encurtar:").pack(pady=5)
entrada = tk.Entry(janela, width=50)
entrada.pack(pady=5)

# Botão de encurtar
botao_encurtar = tk.Button(janela, text="Encurtar URL", command=encurtar_url)
botao_encurtar.pack(pady=5)

# Label para exibir resultado
label_resultado = tk.Label(janela, text="", fg="blue")
label_resultado.pack(pady=5)

# Botão de copiar (desativado inicialmente)
botao_copiar = tk.Button(janela, text="Copiar URL", command=copiar_url, state=tk.DISABLED)
botao_copiar.pack(pady=5)

# Loop principal
janela.mainloop()