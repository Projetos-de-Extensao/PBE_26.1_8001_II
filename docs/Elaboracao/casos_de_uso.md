---
id: diagrama_de_casos_de_uso
title: Diagrama de Casos de Uso
---

## Casos de Uso

Este documento apresenta os principais casos de uso do Sistema de Gestão de Estágios, descrevendo as interações entre os atores e as funcionalidades disponíveis no sistema.

## Diagrama de Casos de Uso

![Diagrama de Casos de Uso](../assets/diagrama_classes/casos_de_uso.png)

### Principais Casos de Uso

#### Aluno
- Realizar cadastro
- Realizar login
- Atualizar dados cadastrais
- Recuperar senha
- Cadastrar estágio
- Enviar documento
- Visualizar status do estágio
- Visualizar documentos enviados

#### Professor Orientador
- Realizar login
- Validar estágio
- Solicitar correção
- Visualizar alunos orientados
- Visualizar documentos do estágio

#### Coordenador
- Realizar login
- Visualizar todos os estágios
- Filtrar estágios por curso
- Gerar relatório

---

## Realizar cadastro no sistema

**Atores:**
- Usuário
- Sistema

**Pré-condições:**
- Nenhuma

**Fluxo Básico:**
1. Usuário acessa a tela de cadastro.
2. Usuário informa os dados solicitados.
3. Sistema valida os dados informados.
4. Sistema registra o novo usuário.
5. Sistema confirma a realização do cadastro.

**Fluxos Alternativos:**
- 3a. Dados inválidos ou incompletos.
  - 3a1. Sistema exibe mensagem de erro.
- 4a. Usuário já cadastrado no sistema.
  - 4a1. Sistema informa que já existe cadastro com os dados fornecidos.

---

## Realizar login no sistema

**Atores:**
- Usuário
- Sistema

**Pré-condições:**
- Usuário deve estar cadastrado no sistema

**Fluxo Básico:**
1. Usuário acessa a tela de login.
2. Usuário informa e-mail e senha.
3. Sistema autentica o usuário.
4. Sistema redireciona o usuário para a área principal do sistema.

**Fluxos Alternativos:**
- 3a. Dados de acesso inválidos.
  - 3a1. Sistema exibe mensagem de erro.
- 3b. Conta desativada.
  - 3b1. Sistema informa que o acesso não pode ser realizado.

---

## Atualizar dados cadastrais

**Atores:**
- Usuário
- Sistema

**Pré-condições:**
- Usuário deve estar autenticado no sistema

**Fluxo Básico:**
1. Usuário acessa a área de edição cadastral.
2. Usuário altera os dados desejados.
3. Sistema valida as informações atualizadas.
4. Sistema salva as alterações.
5. Sistema confirma a atualização dos dados.

**Fluxos Alternativos:**
- 3a. Dados inválidos.
  - 3a1. Sistema exibe mensagem de erro.
- 4a. Falha no salvamento.
  - 4a1. Sistema informa que não foi possível concluir a atualização.

---

## Recuperar senha

**Atores:**
- Usuário
- Sistema

**Pré-condições:**
- Usuário deve possuir cadastro no sistema

**Fluxo Básico:**
1. Usuário acessa a opção de recuperação de senha.
2. Usuário informa o e-mail cadastrado.
3. Sistema valida o e-mail informado.
4. Sistema envia instruções para redefinição de senha.
5. Usuário realiza a redefinição.
6. Sistema confirma a atualização da senha.

**Fluxos Alternativos:**
- 3a. E-mail não encontrado.
  - 3a1. Sistema informa que não existe cadastro vinculado ao e-mail.
- 4a. Falha no envio.
  - 4a1. Sistema solicita nova tentativa posteriormente.

---

## Cadastrar estágio

**Atores:**
- Aluno
- Sistema

**Pré-condições:**
- Aluno deve estar autenticado no sistema

**Fluxo Básico:**
1. Aluno acessa a funcionalidade de cadastro de estágio.
2. Aluno informa os dados do estágio.
3. Sistema valida os dados informados.
4. Sistema registra o estágio.
5. Sistema confirma o cadastro do estágio.

**Fluxos Alternativos:**
- 3a. Dados obrigatórios não preenchidos.
  - 3a1. Sistema exibe mensagem de erro.
- 4a. Falha no cadastro.
  - 4a1. Sistema informa que o estágio não pôde ser registrado.

---

## Enviar documento

**Atores:**
- Aluno
- Sistema

**Pré-condições:**
- Aluno deve estar autenticado no sistema
- Estágio deve estar cadastrado

**Fluxo Básico:**
1. Aluno acessa a área de documentos do estágio.
2. Aluno seleciona o tipo de documento.
3. Aluno envia o arquivo.
4. Sistema valida o envio.
5. Sistema registra o documento no estágio.
6. Sistema confirma o envio do documento.

**Fluxos Alternativos:**
- 4a. Arquivo em formato inválido.
  - 4a1. Sistema exibe mensagem de erro.
- 4b. Documento não enviado corretamente.
  - 4b1. Sistema solicita novo envio.

---

## Visualizar status do estágio

**Atores:**
- Aluno
- Sistema

**Pré-condições:**
- Aluno deve estar autenticado no sistema
- Estágio deve estar cadastrado

**Fluxo Básico:**
1. Aluno acessa a área de acompanhamento.
2. Sistema busca as informações do estágio.
3. Sistema exibe o status atual do estágio.

**Fluxos Alternativos:**
- 2a. Estágio não localizado.
  - 2a1. Sistema informa que não há registro disponível.

---

## Visualizar documentos do estágio

**Atores:**
- Aluno
- Professor Orientador
- Sistema

**Pré-condições:**
- Usuário deve estar autenticado no sistema
- Estágio deve estar cadastrado

**Fluxo Básico:**
1. Usuário acessa a área de documentos do estágio.
2. Sistema busca os documentos vinculados.
3. Sistema exibe os documentos disponíveis.

**Fluxos Alternativos:**
- 2a. Nenhum documento encontrado.
  - 2a1. Sistema informa que não existem documentos cadastrados.

---

## Validar estágio

**Atores:**
- Professor Orientador
- Sistema

**Pré-condições:**
- Professor Orientador deve estar autenticado no sistema
- Estágio deve estar cadastrado

**Fluxo Básico:**
1. Professor Orientador acessa a lista de estágios.
2. Professor Orientador seleciona um estágio.
3. Sistema exibe os dados e documentos do estágio.
4. Professor Orientador realiza a validação.
5. Sistema atualiza o status do estágio.
6. Sistema confirma a validação.

**Fluxos Alternativos:**
- 3a. Documentação incompleta.
  - 3a1. Sistema informa que a validação não pode ser concluída.
- 4a. Professor decide não validar o estágio.
  - 4a1. Sistema mantém o status atual.

---

## Solicitar correção

**Atores:**
- Professor Orientador
- Sistema

**Pré-condições:**
- Professor Orientador deve estar autenticado no sistema
- Estágio deve estar cadastrado

**Fluxo Básico:**
1. Professor Orientador acessa os dados do estágio.
2. Professor Orientador identifica pendências.
3. Professor Orientador registra a solicitação de correção.
4. Sistema atualiza o status do estágio.
5. Sistema informa ao aluno que há correções pendentes.

**Fluxos Alternativos:**
- 3a. Falha no registro da solicitação.
  - 3a1. Sistema informa erro ao professor.

---

## Visualizar alunos orientados

**Atores:**
- Professor Orientador
- Sistema

**Pré-condições:**
- Professor Orientador deve estar autenticado no sistema

**Fluxo Básico:**
1. Professor Orientador acessa a área de alunos orientados.
2. Sistema busca os alunos vinculados.
3. Sistema exibe a lista de alunos orientados.

**Fluxos Alternativos:**
- 2a. Nenhum aluno vinculado.
  - 2a1. Sistema informa que não há alunos orientados cadastrados.

---

## Visualizar todos os estágios

**Atores:**
- Coordenador
- Sistema

**Pré-condições:**
- Coordenador deve estar autenticado no sistema

**Fluxo Básico:**
1. Coordenador acessa a área de estágios.
2. Sistema busca os registros disponíveis.
3. Sistema exibe todos os estágios cadastrados.

**Fluxos Alternativos:**
- 2a. Nenhum estágio cadastrado.
  - 2a1. Sistema informa que não há estágios registrados.

---

## Filtrar estágios por curso

**Atores:**
- Coordenador
- Sistema

**Pré-condições:**
- Coordenador deve estar autenticado no sistema
- Devem existir estágios cadastrados

**Fluxo Básico:**
1. Coordenador acessa a funcionalidade de filtro.
2. Coordenador seleciona o curso desejado.
3. Sistema aplica o filtro.
4. Sistema exibe os estágios correspondentes ao curso informado.

**Fluxos Alternativos:**
- 4a. Nenhum estágio encontrado para o curso selecionado.
  - 4a1. Sistema informa que não existem resultados.

---

## Gerar relatório

**Atores:**
- Coordenador
- Sistema

**Pré-condições:**
- Coordenador deve estar autenticado no sistema
- Devem existir dados cadastrados no sistema

**Fluxo Básico:**
1. Coordenador acessa a funcionalidade de relatórios.
2. Coordenador solicita a geração do relatório.
3. Sistema reúne os dados necessários.
4. Sistema gera o relatório.
5. Sistema exibe ou disponibiliza o relatório gerado.

**Fluxos Alternativos:**
- 3a. Dados insuficientes para geração.
  - 3a1. Sistema informa que não foi possível gerar o relatório.
- 4a. Falha na geração.
  - 4a1. Sistema informa erro ao coordenador.

## Autor(es)

| Data     | Versão | Descrição                         | Autor(es)                                      |
| -------- | ------ | --------------------------------- | ---------------------------------------------- |
| 16/04/25 | 1.0    | Criação do documento              | [Davi, Rafael, Jorge Alves, Gabriel, Gabriel] |
| 16/04/25 | 1.1    | Adição dos casos de uso principais | [Davi, Rafael, Jorge Alves, Gabriel, Gabriel] |