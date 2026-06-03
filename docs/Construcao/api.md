# Documentação da API

Esta seção descreve a API REST do Sistema de Gestão de Estágios.

## Endpoints principais

- `GET /api/` — Lista de recursos registrados pela API.
- `POST /api/token/` — Obtenção de token JWT (usuário e senha).
- `POST /api/token/refresh/` — Renovação de token JWT.
- `GET /api/schema/` — Documento OpenAPI em JSON.
- `GET /api/docs/` — Interface navegável Swagger UI.

### Recursos principais

- `api/usuarios/`
- `api/alunos/`
- `api/professores/`
- `api/coordenadores/`
- `api/empresas/`
- `api/vagas/`
- `api/candidaturas/`
- `api/estagios/`
- `api/documentos/`
- `api/relatorios/`

## Autenticação

A API usa JWT para autenticação. Para usar o Swagger UI, siga estes passos:

1. Acesse `/api/token/` e forneça credenciais válidas.
2. Copie o campo `access` retornado.
3. No Swagger UI `/api/docs/`, clique em `Authorize` e cole o valor no formato:

   ```
   Bearer <token>
   ```

4. Teste requisições autenticadas nos endpoints.

## Exemplos de uso

### Obter vagas

- `GET /api/vagas/`
- Filtros suportados: `area`, `carga_horaria`, `empresa`, `ativa`

### Candidatar-se a uma vaga

- `POST /api/candidaturas/`
- Campos principais: `aluno`, `vaga`, `status`

### Aceitar ou rejeitar candidatura

- `PATCH /api/candidaturas/{id}/aceitar/`
- `PATCH /api/candidaturas/{id}/rejeitar/`

A aceitação ou rejeição de candidaturas só pode ser feita por usuários com perfil `empresa`.

## Observações

- O Swagger UI está disponível em `/api/docs/`.
- A especificação OpenAPI JSON está em `/api/schema/`.
- Endpoints padrão do Django Admin permanecem em `/admin/`.
