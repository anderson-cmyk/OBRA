"""Armazena os dados em memória para fins de prototipagem."""
from collections import defaultdict
from typing import Dict, List

from . import schemas


class InMemoryStorage:
    def __init__(self) -> None:
        self._obras: Dict[int, schemas.Obra] = {}
        self._etapas: Dict[int, schemas.Etapa] = {}
        self._orcamentos: Dict[int, schemas.Orçamento] = {}
        self._custos: Dict[int, schemas.Custo] = {}
        self._pagamentos: Dict[int, schemas.Pagamento] = {}
        self._obra_etapas: Dict[int, List[int]] = defaultdict(list)
        self._obra_orcamentos: Dict[int, List[int]] = defaultdict(list)
        self._counter = defaultdict(int)

    def _next_id(self, key: str) -> int:
        self._counter[key] += 1
        return self._counter[key]

    # Obras ---------------------------------------------------------------
    def create_obra(self, payload: schemas.ObraCreate) -> schemas.Obra:
        obra_id = self._next_id("obra")
        obra = schemas.Obra(id=obra_id, **payload.dict())
        self._obras[obra_id] = obra
        return obra

    def list_obras(self) -> List[schemas.Obra]:
        obras = []
        for obra in self._obras.values():
            etapas_ids = self._obra_etapas.get(obra.id, [])
            orcamentos_ids = self._obra_orcamentos.get(obra.id, [])
            etapas = [self._etapas[etapa_id] for etapa_id in etapas_ids]
            orcamentos = [self._orcamentos[orcamento_id] for orcamento_id in orcamentos_ids]
            obras.append(
                schemas.Obra(
                    **obra.dict(exclude={"etapas", "orcamentos"}),
                    etapas=etapas,
                    orcamentos=orcamentos,
                )
            )
        return obras

    # Etapas --------------------------------------------------------------
    def create_etapa(self, obra_id: int, payload: schemas.EtapaCreate) -> schemas.Etapa:
        if obra_id not in self._obras:
            raise KeyError("Obra não encontrada")
        etapa_id = self._next_id("etapa")
        etapa = schemas.Etapa(id=etapa_id, **payload.dict())
        self._etapas[etapa_id] = etapa
        self._obra_etapas[obra_id].append(etapa_id)
        return etapa

    # Orçamentos ----------------------------------------------------------
    def create_orcamento(self, obra_id: int, payload: schemas.OrçamentoCreate) -> schemas.Orçamento:
        if obra_id not in self._obras:
            raise KeyError("Obra não encontrada")
        orcamento_id = self._next_id("orcamento")
        orcamento = schemas.Orçamento(id=orcamento_id, **payload.dict())
        self._orcamentos[orcamento_id] = orcamento
        self._obra_orcamentos[obra_id].append(orcamento_id)
        return orcamento

    # Custos --------------------------------------------------------------
    def create_custo(self, payload: schemas.CustoCreate) -> schemas.Custo:
        if payload.etapa_id not in self._etapas:
            raise KeyError("Etapa não encontrada")
        custo_id = self._next_id("custo")
        custo = schemas.Custo(id=custo_id, **payload.dict())
        self._custos[custo_id] = custo
        return custo

    # Pagamentos ----------------------------------------------------------
    def create_pagamento(self, payload: schemas.PagamentoCreate) -> schemas.Pagamento:
        if payload.custo_id not in self._custos:
            raise KeyError("Custo não encontrado")
        pagamento_id = self._next_id("pagamento")
        pagamento = schemas.Pagamento(id=pagamento_id, **payload.dict())
        self._pagamentos[pagamento_id] = pagamento
        return pagamento

    def update_pagamento_status(self, pagamento_id: int, status: str) -> schemas.Pagamento:
        if pagamento_id not in self._pagamentos:
            raise KeyError("Pagamento não encontrado")
        pagamento = self._pagamentos[pagamento_id]
        pagamento = schemas.Pagamento(**{**pagamento.dict(), "status": status})
        self._pagamentos[pagamento_id] = pagamento
        return pagamento


storage = InMemoryStorage()
