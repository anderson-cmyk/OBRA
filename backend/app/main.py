from fastapi import FastAPI, HTTPException

from . import schemas, storage

app = FastAPI(title="Gestão de Obras")


@app.get("/obras", response_model=list[schemas.Obra])
def listar_obras() -> list[schemas.Obra]:
    """Retorna todas as obras cadastradas."""
    return storage.storage.list_obras()


@app.post("/obras", response_model=schemas.Obra, status_code=201)
def criar_obra(payload: schemas.ObraCreate) -> schemas.Obra:
    """Cadastra uma nova obra."""
    return storage.storage.create_obra(payload)


@app.post("/obras/{obra_id}/etapas", response_model=schemas.Etapa, status_code=201)
def criar_etapa(obra_id: int, payload: schemas.EtapaCreate) -> schemas.Etapa:
    """Cadastra uma etapa para a obra informada."""
    try:
        return storage.storage.create_etapa(obra_id, payload)
    except KeyError as exc:  # pragma: no cover - tratado pelo HTTPException
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@app.post("/obras/{obra_id}/orcamentos", response_model=schemas.Orçamento, status_code=201)
def criar_orcamento(obra_id: int, payload: schemas.OrçamentoCreate) -> schemas.Orçamento:
    try:
        return storage.storage.create_orcamento(obra_id, payload)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@app.post("/custos", response_model=schemas.Custo, status_code=201)
def registrar_custo(payload: schemas.CustoCreate) -> schemas.Custo:
    try:
        return storage.storage.create_custo(payload)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@app.post("/pagamentos", response_model=schemas.Pagamento, status_code=201)
def solicitar_pagamento(payload: schemas.PagamentoCreate) -> schemas.Pagamento:
    try:
        return storage.storage.create_pagamento(payload)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@app.patch("/pagamentos/{pagamento_id}", response_model=schemas.Pagamento)
def atualizar_status_pagamento(pagamento_id: int, status: str) -> schemas.Pagamento:
    try:
        return storage.storage.update_pagamento_status(pagamento_id, status)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
