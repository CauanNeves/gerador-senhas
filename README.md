# Gerador de Senhas com PySimpleGUI

Um gerador de senhas simples e intuitivo desenvolvido com Python e PySimpleGUI. Permite criar senhas seguras com diferentes combinações de caracteres.

## 📋 Funcionalidades

- **Comprimento Personalizável:** Ajuste o comprimento da senha entre 4 e 15 caracteres.
- **Opções de Componentes:**
  - Letras maiúsculas
  - Letras minúsculas
  - Números
  - Símbolos (@, #, %, &, $, .)
- **Geração Múltipla:** Gere até 6 senhas simultaneamente.

## 🛠️ Pré-requisitos

- Python 3.x
- Biblioteca PySimpleGUI

Instale a biblioteca necessária com o comando:
```bash
pip install PySimpleGUI
```

## 🚀 Como Executar

1. Clone este repositório:
```bash
git clone https://github.com/CauanNeves/gerador-senhas.git
```

2. Acesse o diretório do projeto:
```bash
cd gerador-senhas
```

3. Execute o programa:
```bash
python app.py
```

## 🖥️ Interface

- **Slider:** Ajusta o comprimento da senha.
- **Checkboxes:** Escolha os tipos de caracteres.
- **Botão 'Gerar':** Cria até 6 senhas com base nas configurações selecionadas.

## 🧠 Lógica de Geração de Senhas

A função `gerar_senha` utiliza a biblioteca `random` para selecionar aleatoriamente caracteres com base nas opções escolhidas pelo usuário.

## 📸 Exemplo de Uso

1. Selecione o comprimento da senha.
2. Marque as opções desejadas (Maiúsculas, Minúsculas, Números, Símbolos).
3. Clique em **Gerar**.
4. As senhas aparecerão na seção de resultados.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

---
Desenvolvido por Cauan Neves.

