---
id: requisitos
title: Levantamento de Requisitos
---

# Levantamento de Requisitos

## Introdução

Este documento apresenta o levantamento de requisitos do Sistema de Gestão de Estágios, com o objetivo de definir as funcionalidades e restrições do sistema.

---

## Atores do Sistema

- **Aluno**: busca vagas e se candidata  
- **Empresa**: publica vagas e seleciona candidatos  
- **Instituição**: valida e acompanha os estágios  

---

## Requisitos Funcionais

- **RF01** – O sistema deve permitir o cadastro de alunos com informações acadêmicas  
- **RF02** – O sistema deve permitir o cadastro de empresas com seus dados institucionais  
- **RF03** – O sistema deve permitir que empresas cadastrem vagas de estágio  
- **RF04** – O sistema deve permitir que alunos visualizem e filtrem vagas disponíveis  
- **RF05** – O sistema deve permitir que alunos se candidatem às vagas  
- **RF06** – O sistema deve permitir que empresas visualizem os candidatos inscritos  
- **RF07** – O sistema deve permitir que empresas selecionem candidatos  
- **RF08** – O sistema deve permitir que o aluno acompanhe o status da candidatura  
- **RF09** – O sistema deve permitir autenticação de usuários  
- **RF10** – O sistema deve permitir edição de dados cadastrais  

---

## Requisitos Não Funcionais

- **RNF01 (Desempenho)** – O sistema deve responder em tempo adequado  
- **RNF02 (Segurança)** – O sistema deve garantir autenticação segura  
- **RNF03 (Privacidade)** – O sistema deve proteger os dados conforme a LGPD  
- **RNF04 (Disponibilidade)** – O sistema deve estar disponível sempre que necessário  
- **RNF05 (Usabilidade)** – O sistema deve ser simples e intuitivo  

---

## Regras de Negócio

- **RN01** – Um aluno pode se candidatar a múltiplas vagas  
- **RN02** – Uma vaga pode possuir vários candidatos  
- **RN03** – Apenas empresas cadastradas podem publicar vagas  
- **RN04** – O aluno deve estar regularmente matriculado  
- **RN05** – A candidatura deve estar vinculada a uma vaga existente  