---
id: brainstorm
title: Brainstorm
---
 
## Introdução
<p align = "justify">
O brainstorm é uma técnica de elicitação de requisitos que consiste em reunir a equipe e discutir sobre diversos tópicos gerais do projeto apresentados no documento problema de negócio. No brainstorm o diálogo é incentivado e críticas são evitadas para permitir que todos colaborem com suas próprias ideias.
</p>
 
## Metodologia
<p align = "justify">
A equipe se reuniu para debater ideias gerais sobre o projeto via Discord, começou dia 29 e terminou dia 31 de março, onde o Gabriel Rocha foi o moderador, direcionando a equipe com questões pré-elaboradas, e transcrevendo as respostas para o documento.
</p>
 
## Brainstorm
 
## Versão 1.0
 
## Perguntas
 
### 1. Qual o objetivo principal da aplicação?
 
<p align = "justify">
 <b>Jorge</b> - Deve ser uma plataforma onde alunos consigam encontrar vagas de estágio compatíveis com seu curso e acompanhar todo o processo de candidatura. </p>

<b>Davi</b> - A plataforma deve fornecer um sistema centralizado para gerenciar estágios, incluindo cadastro de alunos, empresas e vagas.

<b>Rafael</b> - O objetivo da aplicação é organizar o processo de estágio dentro da instituição, reduzindo a burocracia e facilitando o envio e controle de documentos.

<b>Gabriel</b> - O principal objetivo da aplicação é permitir que a faculdade acompanhe os estágios dos alunos de forma mais eficiente.

<b>Gabriel Aguiar</b> - A plataforma deve gerenciar todo o ciclo do estágio, desde a candidatura até o encerramento, incluindo termos e documentação.
 
---
 
### 2. Como será o processo para cadastrar um novo cliente?
 
<p align = "justify"> 
<b>Jorge</b> - O usuário deverá acessar o sistema e realizar um cadastro informando dados básicos como nome, e-mail, curso (no caso de aluno) ou informações da empresa. </p>

<b>Davi</b> - O aluno poderá se cadastrar informando seus dados acadêmicos, como curso e período, para facilitar a recomendação de vagas.

<b>Rafael</b> - Com o usuário cadastrado, ele poderá fazer login e acessar o sistema para visualizar vagas ou gerenciar informações.

<b>Gabriel</b> - A empresa deverá preencher informações como nome, área de atuação e dados de contato para poder cadastrar vagas.

<b>Gabriel Aguiar</b> - Após o cadastro, o sistema pode validar os dados e liberar o acesso ao sistema.
 
---
 
### 3. Como será a forma de adicionar produtos?
 
<p align = "justify"> 
<b>Jorge</b> - A empresa, após fazer login, poderá cadastrar uma vaga informando título, descrição, requisitos e carga horária. </p> <p align = "justify"> 

<b>Rafael</b> - A vaga deve conter informações como área de atuação, habilidades exigidas e benefícios oferecidos. </p>

<b>Davi</b> - O sistema deve permitir que a vaga seja associada a cursos específicos, facilitando a busca dos alunos.

<b>Gabriel</b> - Após o cadastro, a vaga ficará disponível para os alunos se candidatarem.

<b>Gabriel Aguiar</b> - O sistema também pode permitir a edição ou remoção da vaga pela empresa.

 
---
 
### 4. Outras perguntas pertinentes ao context
- Como a instituição validará se uma vaga cadastrada está de acordo com a Lei do Estágio e com as regras internas?
- O sistema deverá permitir o gerenciamento de documentos obrigatórios, como TCE, Termo Aditivo e Termo de Rescisão?
- O acompanhamento será apenas da candidatura ou do estágio completo, desde a aprovação até o encerramento?
- A instituição precisará de relatórios consolidados sobre vagas, candidaturas e pendências documentais?
 
## 5. Como seria a forma de adicionar as vagas de estágio?

- As empresas poderão cadastrar vagas diretamente no sistema.
- O cadastro da vaga deverá conter título, descrição, requisitos, carga horária, bolsa, modalidade e localidade.
- As vagas poderão passar por validação institucional antes da publicação.
- As empresas poderão editar, pausar ou encerrar vagas já cadastradas.
 
## 6. Quais informações seriam interessantes para o cliente?

- Informações acadêmicas dos alunos, como curso, período, matrícula e histórico de candidaturas.
- Informações das empresas, como nome, área de atuação e vagas publicadas.
- Informações detalhadas das vagas, como requisitos, carga horária, bolsa e prazo de inscrição.
- Informações documentais, como TCE, Termo Aditivo, Termo de Rescisão e pendências.
- Relatórios gerenciais sobre estágios ativos, encerrados e vagas em aberto.

### Requisitos elicitados
 
|ID|Descrição|
|----|-------------|
|BS01| O sistema deve permitir o cadastro de alunos com informações acadêmicas, como nome, matrícula, curso e período.|
|BS02| O sistema deve permitir o cadastro de empresas interessadas em oferecer vagas de estágio.|
|BS03| O sistema deve permitir o cadastro de vagas de estágio com informações como título, descrição, requisitos, carga horária, bolsa e localidade.|
|BS04| O sistema deve permitir que as empresas editem, pausem ou encerrem vagas cadastradas.|
|BS05| O sistema deve permitir que alunos visualizem vagas de estágio disponíveis.|
|BS06| O sistema deve permitir que alunos se candidatem às vagas cadastradas.|
|BS07| O sistema deve permitir o acompanhamento do status da candidatura, como em análise, aprovada ou rejeitada.|
|BS08| O sistema deve permitir a validação institucional das vagas antes da publicação.|
|BS09| O sistema deve permitir o registro do estágio aprovado, vinculando aluno, empresa e instituição.|
|BS10| O sistema deve permitir o upload e armazenamento de documentos obrigatórios do estágio.|
|BS11| O sistema deve permitir o gerenciamento do Termo de Compromisso de Estágio (TCE).|
|BS12| O sistema deve permitir o registro e controle de Termos Aditivos de estágio.|
|BS13| O sistema deve permitir o registro do encerramento do estágio por meio do Termo de Rescisão.|
|BS14| O sistema deve permitir o acompanhamento de pendências documentais relacionadas ao estágio.|
|BS15| O sistema deve permitir a geração de relatórios sobre vagas, candidaturas, estágios ativos e encerrados.|
 
## Conclusão
<p align = "justify">
Através da aplicação da técnica de pesquisa, foi possível elicitar requisitos iniciais relevantes para o desenvolvimento do Sistema de Gestão de Estágios. A análise do contexto mostrou que o processo de estágio envolve não apenas a divulgação de vagas, mas também o acompanhamento institucional, o controle documental e a conformidade com a legislação vigente. Dessa forma, os requisitos levantados servem como base para a evolução do projeto, permitindo que o sistema atenda às necessidades de alunos, empresas e da instituição de ensino de maneira mais organizada e eficiente.
</p>

## Referências Bibliográficas
 
> BRASIL. Lei nº 11.788, de 25 de setembro de 2008. Dispõe sobre o estágio de estudantes.

> BARBOSA, S. D. J; DA SILVA, B. S. Interação humano-computador. Elsevier, 2010.
 
 
## Autor(es)
| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| 31/03/2026 | 1.0 | Criação do documento | Jorge, Gabriel, Rafael, Davi e Biel |
