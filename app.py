import PySimpleGUI as sg
import random
import string

#Tema
sg.theme('DarkBlue17')

#Layout
#Parte das senhas geradas
frame_result= [
    [sg.Text('', key= 'result1'), sg.Text('', key= 'result4')],
    [sg.Text('', key= 'result2'), sg.Text('', key= 'result5')],
    [sg.Text('', key= 'result3'), sg.Text('', key= 'result6')],
]

#Layout principal
main_layout= [
    [sg.Text('Comprimento da Senha:')],
    [sg.Slider(range= (4, 15), orientation= 'h', key= 'comprimento')],
    [sg.Text('Componentes:')],
    [sg.Checkbox('Maiúscula', key= 'maiuscula'), sg.Checkbox('Minúscula', key= 'minuscula')],
    [sg.Checkbox('Números', key= 'numeros'), sg.Checkbox('Símbolos', key= 'simbolos')],
    [sg.Button('Gerar', key= 'btn-gerar')],
    [sg.Frame('Senhas', frame_result, expand_x= True)]
]

#Janela
window= sg.Window('Gerador de senha', layout= main_layout, element_justification= 'c', size= (450, 300))
#Leitura de eventos e valores
while True:
    event, values= window.read()
    #ler e reagir
    if event == sg.WIN_CLOSED:
        break
    elif event == 'btn-gerar':
        #Senha com letras maiúsculas, sem números e sem caracteres especiais
        if values['maiuscula'] == True and values['minuscula'] == True:
            senha = ''
            for i in range(int(values['comprimento'])):
                senha += random.choice(string.ascii_letters) #Letras maiúsculas e minúsculas
            print(senha)
        #Senha minúscula sem números e sem caracteres especiais
        elif values['minuscula'] == True and values['maiuscula'] == False:
            senha = ''
            for i in range(int(values['comprimento'])):
                senha += str.lower(random.choice(string.ascii_letters)) #Letras minúsculas
            print(senha)
        #Senha com números, letras maiúsculas e minúsculas e sem caracteres especiais
        elif values['numeros'] == True:
            senha= ''
            for i in range(int(values['comprimento'])):
                senha += random.choice(string.hexdigits) #Letras e números
            print(senha)
        print(event, values)