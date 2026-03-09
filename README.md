🔴Pokédex Web

Uma Pokédex interativa desenvolvida com Python + Flask no backend e HTML, CSS e JavaScript no frontend.

A aplicação consome dados da PokéAPI e exibe informações detalhadas dos Pokémon em uma interface inspirada em uma Pokédex clássica.

O projeto foi desenvolvido separando backend e frontend, que rodam juntos para entregar a aplicação completa.
<img width="1352" height="625" alt="image" src="https://github.com/user-attachments/assets/69a0a9fc-29ea-4a34-a420-5a22a702b6e9" />


🚀 Funcionalidades

🔎 Buscar Pokémon por nome ou número (ID)
📊 Exibir stats com barras animadas
🧬 Mostrar tipos do Pokémon com cores dinâmicas
📏 Exibir altura e peso
🖼️ Mostrar arte oficial do Pokémon
➡️ Navegar entre Pokémon usando setas de navegação
⏳ Tela de carregamento durante a busca

🧠 Arquitetura do Projeto

O projeto foi dividido em duas partes principais:

🖥️ Backend

Desenvolvido com Flask em Python.

Responsável por:

Receber requisições do frontend

Consultar a API externa de Pokémon

Retornar os dados em formato JSON

Fluxo:

Frontend → Flask API → PokéAPI → Flask → Frontend

Isso permite que o frontend não precise acessar diretamente a API externa.

🎨 Frontend

Desenvolvido com:

HTML

CSS

JavaScript

Responsável por:

Interface da Pokédex

Animações

Exibição das informações

Interação com o usuário

O frontend faz requisições para a API do backend usando fetch().

🧰 Tecnologias Utilizadas

🐍 Python

🌐 Flask

🎨 HTML

🎨 CSS

⚡ JavaScript

📡 PokéAPI

📂 Estrutura do Projeto

Exemplo simplificado:

pokedex/
│
├── app.py
├── interface.html
└── README.md
⚙️ Como executar o projeto
1️⃣ Clonar o repositório
git clone https://github.com/seu-usuario/pokedex.git

Entrar na pasta:

cd pokedex
2️⃣ Executar o servidor
python app.py

O servidor iniciará em:

http://127.0.0.1:5000
3️⃣ Abrir no navegador

Acesse:

http://127.0.0.1:5000
📸 Interface

A interface foi inspirada em uma Pokédex clássica, contendo:

tela principal com o Pokémon

painel de status

barra de atributos

área de busca

navegação entre Pokémon

🎯 Objetivo do Projeto

Este projeto foi desenvolvido para praticar:

integração entre backend e frontend

consumo de APIs externas

criação de APIs com Flask

manipulação de JSON

construção de interfaces interativas com JavaScript

👨‍💻 Autor

Projeto desenvolvido por Eduardo Gomes.
