# 🪙 Aplicativo de Cotação de Criptomoedas 🚀

Este projeto é um aplicativo simples de cotação de criptomoedas desenvolvido com Kivy, um framework Python para a criação de aplicativos multiplataforma
com tela sensível ao toque. Ele busca os preços das criptomoedas em tempo real na AwesomeAPI e os exibe em uma interface gráfica amigável. O aplicativo 
permite que os usuários alternem a visibilidade do preço de cada criptomoeda com uma animação suave.

## 🚀 Recursos

  - **Busca de Preços em Tempo Real:** Busca os preços mais recentes de criptomoedas na AwesomeAPI.
  - **Interface Amigável:** Uma interface gráfica limpa e intuitiva baseada em Kivy.
  - **Alternar Preço:** Os usuários podem mostrar ou ocultar o preço de cada criptomoeda com um clique.
  - **Transições Animadas:** Animações suaves aprimoram a experiência do usuário ao mostrar ou ocultar preços.
  - **Várias Criptomoedas:** Suporta Bitcoin, Ethereum, Solana, XRP e Dogecoin.

## 🛠️ Pilha de Tecnologia

- **Frontend:**
  - Kivy: Um framework Python para construir aplicativos multiplataforma.
  - Linguagem Kivy (arquivos .kv): Linguagem declarativa para projetar a interface do usuário.
  - **Backend:**
  - Python: A linguagem de programação primária.
  - Requests: Para fazer solicitações HTTP à API.
- **API:**
  - AwesomeAPI: Uma API de preço de criptomoedas.
- **Elementos de UI:**
  - `kivy.uix.gridlayout.GridLayout`
  - `kivy.uix.boxlayout.BoxLayout`
  - `kivy.animation.Animation`
  - `kivy.lang.Builder`

## 📦 Primeiros passos / Instruções de configuração

### Pré-requisitos

- Python 3.6 ou superior
- pip (instalador de pacotes Python)

### Instalação

1. **Clone o repositório:**

  ```bash
  git clone <url_do_repositório>
  cd <diretório_do_repositório>
  ```

2. **Instale os pacotes Python necessários:**

  ```bash
  pip install kivy requests
  ```

### Executando localmente

1. **Navegue até o diretório do projeto:**

  ```bash
  cd <diretório_do_repositório>
  ```

2. **Execute o aplicativo:**

  ```bash
  python main.py
  ```

## 💻 Uso

  Assim que o aplicativo estiver em execução, você verá uma janela com botões para cada criptomoeda suportada.
  Clicar em um botão exibirá o preço da criptomoeda correspondente abaixo dele. Clicar no botão novamente ocultará o preço.

## 📂 Estrutura do Projeto

```
├── main.py         # Main application logic
├── aplicativo.kv   # Kivy UI definition file
└── README.md       # Project documentation
```

## 📸 Screenshots

<img width="792" height="407" alt="criptos" src="https://github.com/user-attachments/assets/366278a0-0f0b-45d9-a7ca-bac0f3549a91" />



## 🤝 Contribuindo

Contribuições são bem-vindas! Siga estes passos:

1. Faça um fork do repositório.
2. Crie uma nova branch para sua funcionalidade ou correção de bug.
3. Faça suas alterações e confirme-as com mensagens descritivas.
4. Envie suas alterações para o seu fork.
5. Envie um pull request.

## 📝 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## 📬 Contato

Caso tenha alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato comigo pelo e-mail [andersonmariano801@gmail.com](mailto:andersonmariano801@gmail.com).

