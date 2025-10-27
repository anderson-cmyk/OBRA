from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_fluxo_basico():
    obra_payload = {
        "nome": "Residencial Alfa",
        "cliente": "Construtora XYZ",
        "responsavel_tecnico": "Eng. Maria",
        "endereco": "Rua das Flores, 100",
    }
    obra = client.post("/obras", json=obra_payload).json()

    etapa_payload = {
        "nome": "Fundação",
        "descricao": "Etapa de fundações",
    }
    etapa = client.post(f"/obras/{obra['id']}/etapas", json=etapa_payload).json()

    orcamento_payload = {
        "descricao": "Orçamento Inicial",
        "valor_total": 100000.0,
    }
    client.post(f"/obras/{obra['id']}/orcamentos", json=orcamento_payload)

    custo_payload = {
        "descricao": "Concreto",
        "valor": 5000.0,
        "etapa_id": etapa["id"],
    }
    custo = client.post("/custos", json=custo_payload).json()

    pagamento_payload = {
        "custo_id": custo["id"],
        "solicitante": "Financeiro",
        "status": "pendente",
    }
    pagamento = client.post("/pagamentos", json=pagamento_payload).json()

    atualizado = client.patch(f"/pagamentos/{pagamento['id']}", params={"status": "aprovado"}).json()

    assert atualizado["status"] == "aprovado"

    obras = client.get("/obras").json()
    assert len(obras) == 1
    assert len(obras[0]["etapas"]) == 1
    assert len(obras[0]["orcamentos"]) == 1
