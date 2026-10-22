"""Robô de teste: abre um pop-up nativo na tela da máquina.

Serve para confirmar visualmente que um job da Control Room chegou até a
máquina e foi executado pelo agente. No macOS usa o ``osascript``
(``display dialog``); em outros sistemas apenas registra um aviso.
"""

import subprocess
import sys

from core.tratador import ErroRPA, passo
from core.logger import logger


@passo("Abrir pop-up")
def abrir_popup(
    navegador=None,
    agente=None,
    item=None,
    mensagem: str = "Olá! Sou um robô rodando nesta máquina via Control Room.",
    segundos: int = 30,
) -> bool:
    """Abre um diálogo nativo que fecha sozinho após ``segundos``."""
    logger.info("Robô de teste de pop-up iniciado.")

    if agente is not None and agente.cancelado():
        logger.warning("Job cancelado antes de abrir o pop-up — encerrando.")
        return False

    if sys.platform != "darwin":
        logger.warning("Pop-up nativo disponível apenas no macOS; nada a exibir.")
        return True

    titulo = "RPA Brasil — Teste"
    script = (
        f'display dialog "{mensagem}" '
        f'buttons {{"OK"}} default button 1 with title "{titulo}" '
        f"giving up after {segundos}"
    )
    logger.info(f"Abrindo pop-up na tela (fecha sozinho em {segundos}s)...")
    resultado = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    saida = (resultado.stdout or resultado.stderr or "").strip()
    logger.info(f"Pop-up retornou: {saida or '(sem saída)'}")
    if resultado.returncode != 0:
        raise ErroRPA(f"Não foi possível exibir o pop-up: {saida}")

    logger.success("Pop-up exibido com sucesso na máquina.")
    return True


def rodar(navegador=None, agente=None, item=None):
    """Função executada pelo agente."""
    return abrir_popup(navegador=navegador, agente=agente, item=item)


if __name__ == "__main__":
    rodar()
