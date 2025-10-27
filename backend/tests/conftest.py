import sys
from pathlib import Path

# Garante que o pacote `app` seja encontrado durante os testes
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "app") not in sys.path:
    sys.path.insert(0, str(ROOT))
