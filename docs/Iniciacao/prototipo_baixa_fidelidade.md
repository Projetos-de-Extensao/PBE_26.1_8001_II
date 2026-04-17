# Protótipo de Baixa Fidelidade

## Introdução

O protótipo de baixa fidelidade é a primeira representação visual do sistema, criada com o objetivo de **validar a estrutura e o fluxo de interações** antes de investimentos maiores em design.

Através desses wireframes simples, conseguimos:
- Validar fluxos de usuário com stakeholders
- Identificar problemas de navegação cedo
- Comunicar ideias de forma clara e acessível
- Iterar rapidamente sem custos altos

## Metodologia

AO projeto teve início a partir dos levantamentos realizados pela equipe, seguidos de discussões para definição das melhores abordagens.

Após essa etapa, foi escolhida a ferramenta Figma para a criação do protótipo de alta fidelidade, com apoio do Material Design Color Tool na definição da identidade visual.

---

## Telas Prototipadas

### 1. Login
**Propósito:** Autenticação do usuário no sistema

**Elementos principais:**
- Campo de email/matrícula
- Campo de senha
- Botão de login
- Link para recuperação de senha

```
@startsalt
{
  {^"Sistema de Estágio - Login"

    E-mail/Matrícula: | ___________
    Senha:            | ___________

    [Login] [Esqueceu a senha?]
  }
}
@endsalt
```

---

### 2. Detalhes da Solicitação
**Propósito:** Visualizar todas as informações de uma solicitação de estágio

**Elementos principais:**
- Dados do aluno (nome, curso, empresa)
- Informações do supervisor
- Status atual da solicitação
- Documentos anexados
- Resultado da análise automática (IA)

```
@startsalt
{
  {^"Detalhes da Solicitação"

    Aluno:      | João Silva
    Curso:      | Sistemas de Informação
    Empresa:    | Tech Solutions
    Supervisor: | Carlos Lima
    Status:     | Em análise

    Documentos:
    [Ver Termo] [Ver Plano] [Ver Matrícula]

    Resultado IA:
    Pendências em assinatura e supervisor

    [Aprovar] [Solicitar ajuste] [Rejeitar]
  }
}
@endsalt
```

---

### 3. Painel do Coordenador
**Propósito:** Gerenciamento e acompanhamento de todas as solicitações

**Elementos principais:**
- Contadores de solicitações pendentes
- Lista de solicitações recentes
- Checkboxes para seleção múltipla
- Botões de ação (Ver detalhes, Aprovar, Rejeitar)
- Menu superior com dados estatísticos

```
@startsalt
{
  {^"Painel do Coordenador"

    Solicitações pendentes: 8
    Pendências críticas: 3

    ()
    Solicitação #2026-01 - João Silva

    ()
    Solicação #2026-02 - Maria Souza

    ()
    Solicitação #2026-03 - Pedro Lima

    [Ver detalhes] [Aprovar] [Rejeitar]

    --

    [Sair]
  }
}
@endsalt
```

---

### 4. Acompanhamento da Solicitação
**Propósito:** Permitir que o aluno acompanhe o progresso de sua solicitação

**Elementos principais:**
- Identificação da solicitação (#2026-01)
- Status atual
- Timeline com passos concluídos e pendentes
- Checkboxes indicando progresso
- Botões de ação (Atualizar, Voltar)

```
@startsalt
{
  {^"Acompanhamento"

    Solicitação: #2026-01
    Aluno: João Silva

    Status: Em análise

    [x] Solicitação enviada
    [x] Documentos recebidos
    [ ] Validação IA
    [ ] Aprovação
    [ ] Finalizado

    [Atualizar] [Voltar]
  }
}
@endsalt
```

---
