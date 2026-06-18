🛒 Sistema ERP & Chatbot - Pós-Venda de Loja de Calçados (Etapa 4)

Este projeto consiste em um sistema de chatbot automatizado para simular o atendimento de pós-venda de uma loja de calçados, integrado a um modelo de persistência de dados em JSON e geração de relatórios em TXT.

Desenvolvido como parte do projeto integrador PP4.

---

👥 Integrantes da Equipe
* Kelvin Santos Lima
* Lucas Carneiro Brito
* Rafael Sodré Nunes Marques Dourado

---

🏢 Setores Automatizados (Descrição do Sistema)

Para este projeto integrador, focamos na automação e integração de dois setores essenciais para o funcionamento de uma loja de varejo de calçados:

1. Setor de Clientes (Cadastro Geral): Responsável por gerenciar a base de dados de compradores da loja (armazenando ID, Nome, Idade, Telefone e Cidade). É a base que valida se um cliente está ativo e apto a interagir com os serviços da empresa.
2. Setor de Pós-Venda (Produtos/Garantia): Responsável pelo controle de trocas, devoluções e triagem de calçados que apresentaram defeito ou problemas de tamanho. Este setor é integrado diretamente ao de Clientes através do ID do comprador, permitindo rastrear o histórico de reclamações e atualizar o status de cada solicitação (Ex: Em Análise, Aguardando Postagem, Reembolsado).

---

🛠️ Tecnologias Utilizadas
* Python 3 (Lógica principal do sistema e menus)
* JSON (Persistência e armazenamento dinâmico de dados das matrizes)
* Git & GitHub (Versionamento e hospedagem do código)

---

🚀 Funcionalidades Implementadas (Etapa 4)

* A. Persistência de Dados: O sistema realiza a carga inicial dinâmica de dados ao iniciar através de arquivos JSON (`setor_clientes.json` e `setor_produtos.json`). Qualquer novo cadastro, exclusão ou alteração de status é salvo automaticamente em tempo real nos arquivos.
* B. Módulo de Emissão de Relatórios: Opção integrada no menu para gerar arquivos físicos `.txt` formatados, com paginação, colunas alinhadas por f-strings, rodapé com totalizadores e carimbo de data/hora (via biblioteca `datetime`):
  1. Relatório Geral Cruzado: Cruza os dados do pós-venda, buscando e exibindo o nome do cliente correspondente.
  2. Relatório Filtrado: Exporta apenas os produtos com o status selecionado pelo usuário.

---

📂 Estrutura de Pastas

├── data/
│   ├── setor_clientes.json
│   ├── setor_produtos.json
│   ├── relatorio_geral.txt
│   └── relatorio_filtrado.txt
├── projeto 4.py  (Arquivo principal do código)
└── README.md

🏃‍♂️ Como Executar o Projeto
1. Certifique-se de ter o Python instalado.
2. Execute o arquivo principal pelo terminal:
   
   python projeto 4.py