"""Auxiliar interno para carregar o .env quando python-dotenv está disponível."""
from __future__ import annotations

from pathlib import Path

_ENV_LOADED = False


def load_env(force: bool = False) -> None:
    """Carrega variáveis de ambiente do .env se python-dotenv estiver instalado.

    É uma operação nula e segura se python-dotenv estiver ausente, preservando
    a operação sem dependências do Nível 0 (manual). Busca a partir do
    diretório de trabalho atual subindo na árvore e verifica a raiz do
    repositório. Variáveis de ambiente já existentes são preservadas.
    """
    global _ENV_LOADED
    if _ENV_LOADED and not force:
        return

    try:
        from dotenv import find_dotenv, load_dotenv

        # 1. Busca a partir do cwd subindo na árvore (para usuários de plugin
        #    trabalhando em diretórios de projeto)
        dotenv_path = find_dotenv(usecwd=True)
        if dotenv_path:
            load_dotenv(dotenv_path)

        # 2. Verifica a raiz do repositório relativa a este arquivo
        repo_env = Path(__file__).resolve().parents[1] / ".env"
        if repo_env.is_file():
            load_dotenv(repo_env)
    except ImportError:
        pass

    _ENV_LOADED = True
