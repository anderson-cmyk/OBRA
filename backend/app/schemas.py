from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field


class EtapaBase(BaseModel):
    nome: str = Field(..., description="Nome da etapa")
    descricao: Optional[str] = Field(None, description="Descrição detalhada da etapa")
    data_inicio: Optional[date] = Field(None, description="Data planejada de início")
    data_fim: Optional[date] = Field(None, description="Data planejada de término")


class EtapaCreate(EtapaBase):
    parent_id: Optional[int] = Field(None, description="Identificador da etapa mãe, quando aplicável")


class Etapa(EtapaBase):
    id: int
    parent_id: Optional[int]

    class Config:
        orm_mode = True


class OrçamentoBase(BaseModel):
    descricao: str
    valor_total: float = Field(..., ge=0)


class OrçamentoCreate(OrçamentoBase):
    pass


class Orçamento(OrçamentoBase):
    id: int

    class Config:
        orm_mode = True


class CustoBase(BaseModel):
    descricao: str
    valor: float = Field(..., ge=0)
    etapa_id: int = Field(..., description="Etapa vinculada ao custo")
    comprovante_url: Optional[str] = Field(None, description="Link para o comprovante")


class CustoCreate(CustoBase):
    pass


class Custo(CustoBase):
    id: int

    class Config:
        orm_mode = True


class PagamentoBase(BaseModel):
    custo_id: int = Field(..., description="Custo a ser pago")
    solicitante: str
    status: str = Field("pendente", description="Status do pagamento")


class PagamentoCreate(PagamentoBase):
    pass


class Pagamento(PagamentoBase):
    id: int

    class Config:
        orm_mode = True


class ObraBase(BaseModel):
    nome: str
    cliente: str
    responsavel_tecnico: Optional[str] = None
    endereco: Optional[str] = None


class ObraCreate(ObraBase):
    pass


class Obra(ObraBase):
    id: int
    etapas: List[Etapa] = []
    orcamentos: List[Orçamento] = []

    class Config:
        orm_mode = True
