# Sistema de Gestão de Obras

Este repositório traz um MVP inicial para o sistema de gestão de obras discutido anteriormente. A solução está organizada em módulos que podem evoluir para uma plataforma completa de controle de orçamento, etapas, custos e pagamentos.

## Estrutura do Projeto

```text
.
├── backend
│   ├── app
│   │   ├── main.py          # API FastAPI com endpoints REST
│   │   ├── schemas.py       # Modelos Pydantic para validação
│   │   └── storage.py       # Repositório em memória para prototipagem
│   ├── requirements.txt     # Dependências mínimas para executar a API
│   └── tests
│       └── test_main.py     # Fluxo básico cobrindo cadastro, custos e pagamentos
├── docs                     # Espaço para documentação funcional/técnica
└── frontend                 # Ponto de partida para o futuro front-end
```

## Executando o Back-end

1. Crie e ative um ambiente virtual Python 3.11.
2. Instale as dependências:

   ```bash
   pip install -r backend/requirements-dev.txt
   ```

3. Suba a API localmente:

   ```bash
   uvicorn app.main:app --reload --app-dir backend/app
   ```

   A API ficará disponível em `http://127.0.0.1:8000` e a documentação automática em `http://127.0.0.1:8000/docs`.

## Executando os Testes

```bash
pytest backend/tests -q
```

## Próximos Passos Sugeridos

- Persistir os dados em um banco relacional (PostgreSQL) e substituir o armazenamento em memória.
- Implementar autenticação e controle de acesso.
- Criar um front-end (React ou Vue) consumindo os endpoints expostos.
- Adicionar integrações com ferramentas financeiras para automatizar o contas a pagar.
- Expandir a suíte de testes com cenários de erro e fluxos alternativos.
