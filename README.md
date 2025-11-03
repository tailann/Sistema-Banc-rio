🏦 Sistema Bancário CLI em Python
Projeto Desenvolvido no Curso Luizalabs: Back-end com Python

Sistema Bancário Sem Interface Gráfica
<P> O Sistema Bancário CLI em Python é um projeto desenvolvido como Estudo de Caso Prático durante o curso Luizalabs - Back-end com Python. O foco principal é a aplicação rigorosa dos conceitos de Programação Orientada a Objetos (POO) em um sistema de linha de comando (CLI), simulando as operações básicas de uma conta bancária. </P>

Funcionalidades e Conceitos de POO
<p> O código foi estruturado para demonstrar o uso eficiente de classes e padrões de projeto para gestão de clientes, contas e transações. Os principais conceitos de POO aplicados são: </p>

Abstração e Herança: Uso de classes base (Conta, Cliente, Transacao - esta última como Abstract Base Class) e herança para estender funcionalidades (ContaCorrente, PessoaFisica, Saque, Deposito).

Encapsulamento: Utilização de properties (@property) para proteger o estado interno dos objetos, como o saldo (_saldo).

Polimorfismo: Implementação do método sacar na classe ContaCorrente com lógica específica (limite por saque e limite de saques diários).

Iteradores: Implementação de um iterador customizado (contasIterador) para facilitar a listagem formatada das contas.

Decoradores (@log_transacao): Uso de decoradores para adicionar logging automático às funções de transação.

Tecnológia Utilizada
<p>


Linguagem Principal: Python


Paradigma: Programação Orientada a Objetos (POO)


Interface: Comando de Linha (CLI) </p>

Funcionalidades Disponíveis
<p> O sistema permite a interação com as seguintes operações via menu CLI: </p>

[nu] - Novo Usuário: Criação de novos clientes (Pessoa Física).

[nc] - Nova Conta: Abertura de Contas Correntes.

[lc] - Listar Contas: Exibição detalhada de todas as contas.

[d] - Depositar: Realiza depósitos, seguindo a lógica da transação.

[s] - Sacar: Realiza saques, aplicando as regras de limites da ContaCorrente.

[e] - Extrato: Exibe o histórico de transações completo.

Como Rodar Localmente
<ol> <tittle>Siga os passos para executar o sistema na sua máquina</tittle> <li>Clonar o Repositório: git clone [LINK_DO_SEU_REPOSITORIO]</li> <li>Acessar o diretório: cd [NOME_DO_DIRETORIO]</li> <li>Executar o Aplicativo via terminal: python nome_do_arquivo.py</li> </ol>

<p> Desenvolvido como Estudo de Caso para aprofundamento
