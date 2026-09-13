"""Shared fixtures."""

from __future__ import annotations

from pathlib import Path

import pytest

from aptosed.config import WalletConfig
from aptosed.services.wallet import WalletService


@pytest.fixture()
def service(tmp_path: Path) -> WalletService:
    config = WalletConfig(storage_dir=str(tmp_path))
    return WalletService(config)
