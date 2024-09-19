import tkinter as tk 

# Criando a Janela principal 
janela = tk.Tk() 
janela.title("Tabela IMC")  # Título da janela
janela.geometry("400x400")  # Largura x Altura da janela

# Criar botões, textos e outros elementos da tela 
titulo = tk.Label(janela, text="Calculadora de IMC")
texto_altura = tk.Label(janela, text="Coloque sua altura em metros")  # Corrigido o texto
texto_peso = tk.Label(janela, text="Coloque seu peso em quilogramas")  # Corrigido o texto

campo_altura = tk.Entry(janela)
campo_peso = tk.Entry(janela)

def calcular_imc():
    try:
        altura = float(campo_altura.get())
        peso = float(campo_peso.get())
        imc = peso / (altura ** 2)  # Fórmula do IMC
        resultado.config(text=f"Seu IMC é: {imc:.2f}")  # Corrigido o uso do config
    except ValueError:
        resultado.config(text="Por favor, insira valores válidos.")  # Corrigido o uso do config

botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
resultado = tk.Label(janela, text="")

# Elementos na tela 
titulo.pack(padx=10, pady=10)
texto_altura.pack(padx=10, pady=5)
campo_altura.pack(padx=10, pady=5)
texto_peso.pack(padx=10, pady=5)
campo_peso.pack(padx=10, pady=5)
botao_calcular.pack(pady=10)
resultado.pack(pady=10)

# Rodar a janela 
janela.mainloop()

