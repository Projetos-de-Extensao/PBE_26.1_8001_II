# Design Thinking

## 1. Capa

- **Título do Projeto:** Sistema de Gestão de Estágios Acadêmicos
- **Nome da Equipe:** Rafael Barbosa, Gabriel Lima, Jorge Alves, Davi Ito, Gabriel Aguiar
- **Data:** 2026.1
- **Instituição:** Ibmec

---

## 2. Introdução

### Contexto do Projeto

O processo de estágio no ambiente acadêmico envolve múltiplos atores — alunos, empresas e a própria instituição — e exige a gestão de documentos, prazos e comunicações que, atualmente, ocorrem de forma descentralizada. Isso gera confusão, retrabalho e dificuldade de acompanhamento para todos os envolvidos.

### Objetivo

Desenvolver um sistema back-end que centralize e organize o processo de gestão de estágios, desde a publicação de vagas até o encerramento do estágio, facilitando a comunicação entre alunos, empresas e o Ibmec.

### Público-Alvo

- Alunos de graduação do Ibmec em busca de estágio
- Empresas parceiras que oferecem vagas de estágio
- Coordenação acadêmica e setor de estágios do Ibmec

### Escopo

O sistema abrange o cadastro de usuários, publicação e busca de vagas, candidatura, acompanhamento do processo seletivo e gestão documental do estágio. Não inclui, nesta fase, o desenvolvimento do front-end completo nem integração com sistemas externos.

---

## 3. Fases do Design Thinking

### 3.1. Empatia

**Pesquisa realizada:**
A equipe conduziu uma análise do processo atual de estágios no Ibmec, levantando os principais pontos de atrito relatados por alunos e pela coordenação acadêmica. Foram analisados também documentos institucionais como o Manual do Estagiário e o Termo de Compromisso de Estágio (TCE).

**Principais insights:**
- Alunos têm dificuldade em encontrar vagas alinhadas ao seu curso e período
- O processo de envio e validação de documentos é manual e sujeito a erros
- A instituição não tem visibilidade consolidada dos estágios em andamento
- Empresas precisam de um canal direto para divulgar vagas e receber candidaturas

**Personas identificadas:**

**Persona 1 — O Aluno**
> João, 20 anos, 4º semestre de Engenharia de Computação. Quer encontrar um estágio na área de desenvolvimento, mas não sabe por onde começar e tem dificuldade em entender quais documentos a instituição exige.

**Persona 2 — O RH da Empresa**
> Ana, 30 anos, analista de RH de uma empresa de tecnologia. Quer divulgar vagas para alunos de TI e receber currículos de forma organizada, sem depender de e-mails avulsos.

**Persona 3 — A Coordenação**
> Prof. Carlos, coordenador de estágios do Ibmec. Precisa validar estágios, acompanhar documentação e garantir que os alunos estão cumprindo a carga horária corretamente.

---

### 3.2. Definição

**Problema Central:**
> "Como podemos centralizar e organizar o processo de gestão de estágios do Ibmec, facilitando a busca de vagas, a candidatura e o acompanhamento documental para alunos, empresas e a instituição?"

**Pontos de Vista (POV):**
- O aluno precisa de uma forma simples de encontrar vagas compatíveis com seu curso e acompanhar o status da candidatura.
- A empresa precisa de um canal direto para publicar vagas e selecionar candidatos sem burocracia.
- A instituição precisa de visibilidade sobre todos os estágios ativos e controle sobre a documentação exigida por lei.

---

### 3.3. Ideação

**Ideias geradas no brainstorm:**
- Sistema de cadastro diferenciado por tipo de usuário (aluno, empresa, instituição)
- Filtro de vagas por curso, área, modalidade e bolsa
- Painel de acompanhamento de candidaturas com status em tempo real
- Upload e validação de documentos obrigatórios (TCE, Termo Aditivo, Rescisão)
- Notificações automáticas sobre mudanças de status
- Relatórios gerenciais para a coordenação

**Ideias selecionadas para prototipagem:**
- Cadastro e autenticação por perfil
- Publicação e busca de vagas com filtros
- Candidatura e acompanhamento de status
- Gestão básica de documentos do estágio

---

### 3.4. Prototipagem

**Descrição do Protótipo:**
Foi desenvolvido um protótipo de baixa fidelidade utilizando esboços das telas principais do sistema, cobrindo os fluxos de login, cadastro, busca de vagas, candidatura e dashboard. Em seguida, foi elaborado um protótipo de alta fidelidade no Figma com as telas detalhadas e o fluxo de navegação completo.

**Ferramentas utilizadas:**
- Figma (prototipagem visual)
- MkDocs (documentação)
- Mermaid (diagramas de fluxo)

**Telas prototipadas:**
- Login e cadastro (aluno e empresa)
- Dashboard do aluno e da empresa
- Busca e detalhes de vaga
- Candidatura e acompanhamento
- Gestão de documentos do estágio

---

### 3.5. Teste

**Feedback coletado:**
- A separação de perfis (aluno/empresa) foi considerada clara e intuitiva
- O fluxo de candidatura foi validado como simples e direto
- Sugestão: adicionar filtro por localidade na busca de vagas
- Sugestão: exibir prazo de encerramento da vaga diretamente no card

**Ajustes realizados:**
- Adicionado campo de localidade no formulário de cadastro de vaga
- Prazo de inscrição adicionado ao card de vaga na listagem
- Status da candidatura representado por badges coloridos para melhor visualização

**Resultado final:**
Sistema validado com os fluxos principais funcionando de forma coerente, cobrindo as necessidades das três personas identificadas.

---

## 4. Conclusão

### Resultados Obtidos
O processo de Design Thinking permitiu que a equipe compreendesse profundamente o problema antes de propor soluções. As personas criadas guiaram as decisões de design e os requisitos levantados foram diretamente incorporados ao sistema.

### Próximos Passos
- Implementação do back-end em Python
- Desenvolvimento das APIs REST para cada funcionalidade
- Integração com banco de dados
- Testes de aceitação com usuários reais

### Aprendizados
- A empatia com os usuários revelou necessidades que não eram óbvias inicialmente, como o controle de documentos do TCE
- Iterar entre ideação e prototipagem acelerou a validação das funcionalidades
- A divisão clara de responsabilidades entre os perfis simplificou a arquitetura do sistema

---

## 5. Anexos

- [Brainstorming completo](../Brainstorm/)
- [Mapa Mental](../mapa_mental/)
- [Protótipo de Baixa Fidelidade](../prototipo_baixa_fidelidade/)
- [Requisitos levantados](../../Elaboracao/requisitos/)

---

## Histórico de Versão

| Data | Versão | Descrição | Autor(es) |
|---|---|---|---|
| 06/05/2026 | 1.0 | Criação do documento de Design Thinking | Davi Ito |
