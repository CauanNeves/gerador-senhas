import PySimpleGUI as sg
import random
import string

# Tema
sg.theme('DarkBlue17')

# Layout
# Parte das senhas geradas
frame_result = [
    [sg.Text('', key='result1', justification= 'c', expand_x= True), sg.Text('', key='result4', justification= 'c', expand_x= True)],
    [sg.Text('', key='result2', justification= 'c', expand_x= True), sg.Text('', key='result5', justification= 'c', expand_x= True)],
    [sg.Text('', key='result3', justification= 'c', expand_x= True), sg.Text('', key='result6', justification= 'c', expand_x= True)],
]

# Layout principal
main_layout = [
    [sg.Text('Comprimento da Senha:')],
    [sg.Slider(range=(4, 15), default_value=8, orientation='h', key='comprimento')],
    [sg.Text('Componentes:')],
    [sg.Checkbox('Maiúscula', key='maiuscula'), sg.Checkbox('Minúscula', key='minuscula')],
    [sg.Checkbox('Números', key='numeros'), sg.Checkbox('Símbolos', key='simbolos')],
    [sg.Button('Gerar', key='btn-gerar')],
    [sg.Frame('Senhas', frame_result, expand_x=True)],
]

# Janela
window = sg.Window('Gerador de Senha', layout=main_layout, element_justification='c', size=(400, 310))

# Função para gerar senha
def gerar_senha(comprimento, maiuscula, minuscula, numeros, simbolos):
    caracteres = ''
    if maiuscula:
        caracteres += string.ascii_uppercase
    if minuscula:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += '@#%&$.'

    if not caracteres:
        return 'Selecione pelo menos uma opção'
    
    return ''.join(random.choice(caracteres) for _ in range(int(comprimento)))


# Loop de eventos
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'btn-gerar':
        senhas = [gerar_senha(values['comprimento'], values['maiuscula'], values['minuscula'], values['numeros'], values['simbolos']) for _ in range(6)]
        
        # Atualiza os campos de texto com as senhas geradas
        for i, senha in enumerate(senhas):
            window[f'result{i+1}'].update(senha)

# Fecha a janela
window.close()