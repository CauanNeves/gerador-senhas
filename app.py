import PySimpleGUI as sg

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
        print(event, values)