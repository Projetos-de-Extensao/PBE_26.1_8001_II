---
id: diagrama_de_casos de uso
title: Diagrama de Casos de Uso
---

## Casos de Uso

### Descrição:

- Contas
	- Criação
	- Entrada
	- Alteração
	- Recuperar Senha
	- Exclusão Lógica
	- Visualização

- Perfis
	- Edição
	- Pesquisar
	- Visualização
	- Seguir/Deixar de Seguir

- Postagens (Público) 	 	
	- Criação
	- Exclusão
	- Interação
	- Visualização

- Mensagens (Privado)
	- Criação
	- Exclusão
	- Visualização

- Galerias
	- Albuns
- Blogs
- Grupos

### Criação de uma conta no sistema

* Atores:

	- Usuário
	- Sistema

- Pré-Condições:
	- Nenhuma

* Fluxo Básico:
    1. Usuário fornece e-mail, senha e confirmações
    2. Dados do Usuário são validados pelo Sistema
    3. Dados do Usuário são encriptados pelo Sistema
    4. Dados do Usuário são persistidos pelo Sistema
    5. Sistema gera um link com prazo de expiração
    6. Sistema envia e-mail de verificação, com o link, para o Usuário
    7. Usuário confirma o e-mail antes do link expirar
    8. Sistema confirma que o Cadastro do Usuário foi realizado com sucesso
    9. Sistema redireciona o Usuário para a página de Entrada

- Fluxos Alternativos:
	- 2a. E-mail do Usuário é inválido
		2a1. Sistema exibe mensagem de erro
	- 2b. Senha do Usuário não respeita regras de segurança
		- 2b1. Sistema exibe mensagem de erro
	- 3a. Usuário tenta confirmar o e-mail depois de o link expirar
		- 3a1. Sistema sugere que o Usuário realize um novo Cadastro

### Entrada do usuário no sistema

- Atores:
	- Usuário
	- Sistema

- Pré-Condições:
	Usuário deve estar cadastrado

- Fluxo Básico:
    - 1. Usuário fornece e-mail e senha
	- 2. Sistema autentica o Usuário
	- 3. Sistema redireciona o Usuário para a página inicial

- Fluxos Alternativos:
	- 2a. Dados do Usuário Inválidos
		- 2a1. Sistema exibe mensagem de erro
	- 3a. Primeio acesso do Usuário
		- 3a1. Sistema redireciona o Usuário para a página de edição de perfil

### Alteração de dados da conta

* Atores:

	- Usuário
	- Sistema

- Pré-Condições:
	Usuário deve estar autenticado no sistema

* Fluxo Básico:
	1. Usuário acessa a área de configurações da conta
	2. Usuário altera os dados desejados
	3. Sistema valida os novos dados
	4. Sistema atualiza as informações do Usuário
	5. Sistema confirma a atualização

- Fluxos Alternativos:
	- 3a. Dados inválidos
		- 3a1. Sistema exibe mensagem de erro
	- 4a. Falha na atualização
		- 4a1. Sistema informa erro ao Usuário


### Recuperar senha

* Atores:

	- Usuário
	- Sistema

- Pré-Condições:
	Usuário deve possuir cadastro no sistema

* Fluxo Básico:
	1. Usuário solicita recuperação de senha
	2. Usuário informa o e-mail cadastrado
	3. Sistema valida o e-mail
	4. Sistema envia link de recuperação
	5. Usuário acessa o link
	6. Usuário define nova senha
	7. Sistema atualiza a senha
	8. Sistema confirma alteração

- Fluxos Alternativos:
	- 3a. E-mail não encontrado
		- 3a1. Sistema informa erro
	- 5a. Link expirado
		- 5a1. Sistema solicita nova requisição


### Exclusão lógica de conta

* Atores:

	- Usuário
	- Sistema

- Pré-Condições:
	Usuário autenticado

* Fluxo Básico:
	1. Usuário solicita exclusão da conta
	2. Sistema solicita confirmação
	3. Usuário confirma ação
	4. Sistema desativa a conta
	5. Sistema encerra sessão do Usuário

- Fluxos Alternativos:
	- 3a. Usuário cancela operação
		- 3a1. Sistema mantém conta ativa


### Visualização de perfil

* Atores:

	- Usuário
	- Sistema

- Pré-Condições:
	Nenhuma

* Fluxo Básico:
	1. Usuário acessa um perfil
	2. Sistema busca os dados do perfil
	3. Sistema exibe as informações


### Edição de perfil

* Atores:

	- Usuário
	- Sistema

- Pré-Condições:
	Usuário autenticado

* Fluxo Básico:
	1. Usuário acessa seu perfil
	2. Usuário edita informações
	3. Sistema valida os dados
	4. Sistema salva alterações
	5. Sistema confirma atualização

- Fluxos Alternativos:
	- 3a. Dados inválidos
		- 3a1. Sistema exibe erro


### Seguir usuário

* Atores:

	- Usuário
	- Sistema

- Pré-Condições:
	Usuário autenticado

* Fluxo Básico:
	1. Usuário acessa perfil de outro usuário
	2. Usuário seleciona a opção "seguir"
	3. Sistema registra a ação
	4. Sistema atualiza lista de seguidores


### Deixar de seguir usuário

* Atores:

	- Usuário
	- Sistema

- Pré-Condições:
	Usuário autenticado

* Fluxo Básico:
	1. Usuário acessa perfil seguido
	2. Usuário seleciona "deixar de seguir"
	3. Sistema remove vínculo
	4. Sistema atualiza lista


### Criação de postagem

* Atores:

	- Usuário
	- Sistema

- Pré-Condições:
	Usuário autenticado

* Fluxo Básico:
	1. Usuário cria nova postagem
	2. Usuário adiciona conteúdo
	3. Sistema valida conteúdo
	4. Sistema publica postagem


### Interação com postagem

* Atores:

	- Usuário
	- Sistema

- Pré-Condições:
	Postagem existente

* Fluxo Básico:
	1. Usuário acessa a postagem
	2. Usuário realiza interação (curtir ou comentar)
	3. Sistema registra interação
	4. Sistema atualiza os dados da postagem


### Envio de mensagem privada

* Atores:

	- Usuário
	- Sistema

- Pré-Condições:
	Usuário autenticado

* Fluxo Básico:
	1. Usuário seleciona destinatário
	2. Usuário escreve mensagem
	3. Sistema envia mensagem
	4. Sistema registra envio


### Visualização de mensagens

* Atores:

	- Usuário
	- Sistema

- Pré-Condições:
	Usuário autenticado

* Fluxo Básico:
	1. Usuário acessa a conversa
	2. Sistema carrega as mensagens
	3. Sistema exibe o conteúdo