# Arquitetura Inicial

## Visão Geral

O objetivo deste MVP é validar os principais fluxos de cadastro de obras, controle de etapas, orçamento, lançamento de custos e solicitações de pagamento. Ele serve como base para evoluções futuras descritas na visão de produto.

## Componentes

- **API FastAPI**: expõe endpoints REST para manipular obras e entidades relacionadas.
- **Armazenamento em Memória**: simplifica o desenvolvimento inicial; deve ser substituído por um banco de dados relacional.
- **Testes Automatizados**: garantem o fluxo principal (cadastro → custo → pagamento) funcionando de ponta a ponta.

## Próximas Evoluções

1. Persistência utilizando PostgreSQL com SQLAlchemy.
2. Autenticação baseada em JWT com perfis de acesso.
3. Módulo financeiro com integração a gateways de pagamento ou ERPs.
4. Front-end web para operação pelos times de engenharia e financeiro.
