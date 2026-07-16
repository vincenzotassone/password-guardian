import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "src"))

from rules import RegolaLunghezza


def test_regola_lunghezza():

    regola = RegolaLunghezza()

    assert regola.verifica("Password123") == True
    assert regola.verifica("abc") == False
