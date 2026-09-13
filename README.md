# aptos-ed25519

> aptos · ed25519 · account

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-3776AB)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Build](https://img.shields.io/badge/build-passing-brightgreen)]()

Aptos account helper — Ed25519-shaped address, stub faucet.

## Features

- HD derivation along m/44'/637'/0' for APT
- Passphrase-wrapped vault stored as local JSON
- Deterministic address codec (SHA-256 simulation, no live keys)
- Fee estimator with low / medium / high presets
- Balance sync against a stub RPC client
- Click CLI with vault, account and portfolio commands

## Prerequisites

- Python 3.11+
- Git

## Getting Started

```bash
git clone <repo-url>
cd aptos-ed25519
python -m pip install -e .
python -m aptosed --help
```

## CLI Usage

```bash
aptosed create-vault --name "Main"
# Create an encrypted local vault

aptosed list-vaults
# List vault files in the storage directory

aptosed add-account --label Savings
# Derive the next HD account

aptosed sync
# Refresh stub balances

aptosed balance
# Print account table

aptosed portfolio
# Show coin + stub USD total
```

## Project Structure

```
aptosed/
  crypto/          seed, derive, address
  chain/           stub RPC and fee table
  storage/         vault JSON
  services/        wallet + sync
  cli.py           click entry
tests/             pytest
```

## Configuration

Defaults live in `aptosed/config.py` (`WalletConfig`).

| Setting | Default | Description |
|---------|---------|-------------|
| `network` | `mainnet` | mainnet / testnet |
| `rpc_endpoint` | `http://127.0.0.1:8080` | APT node URL (unused in stub mode) |
| `storage_dir` | `.wallets` | Local vault directory |
| `derivation_path` | `m/44'/637'/0'` | BIP path |

## Tests

```bash
python -m pytest -q
```

## Background

Move-chain scripts search aptos-ed25519.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.


---

## Topics

![aptos](https://img.shields.io/badge/aptos-111827?style=flat-square) ![ed25519](https://img.shields.io/badge/ed25519-111827?style=flat-square) ![aptos-ed25519](https://img.shields.io/badge/aptos%20ed25519-111827?style=flat-square) ![cryptocurrency](https://img.shields.io/badge/cryptocurrency-111827?style=flat-square) ![wallet](https://img.shields.io/badge/wallet-111827?style=flat-square) ![blockchain](https://img.shields.io/badge/blockchain-111827?style=flat-square) ![web3](https://img.shields.io/badge/web3-111827?style=flat-square) ![bitcoin](https://img.shields.io/badge/bitcoin-111827?style=flat-square)

`aptos` `ed25519` `aptos-ed25519` `cryptocurrency` `wallet` `blockchain` `web3` `bitcoin` `ethereum` `hd-wallet` `open-source` `python`

Search: aptos-ed25519 · aptos · ed25519 · account · Aptos account helper — Ed25519-shaped address, stub faucet.

---

<sub>Aptos account helper — Ed25519-shaped address, stub faucet.</sub>
