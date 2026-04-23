# bt_api_security

[![Python 3.9-3.14](https://img.shields.io/badge/python-3.9--3.14-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Security compliance and audit framework for the bt_api ecosystem. Provides zero-trust architecture, end-to-end encryption, audit logging, MFA/OAuth2 authentication, and regulatory compliance support.

## Features

### Authentication
- **OAuth2Provider** — OAuth 2.0 authorization code / client credentials flow
- **MFAProvider** — TOTP/HOTP multi-factor authentication

### Access Control
- **AccessControlManager** — Role-based access control (RBAC)
- **Role / Permission** — Typed role and permission enums

### Audit & Compliance
- **AuditLogger** — Immutable audit trail with structured event logging
- **ComplianceMonitor** — Real-time compliance rule enforcement
- **ThreatDetector** — Pattern-based threat detection engine

### Encryption & Data Protection
- **EncryptionManager** — AES-256-GCM encryption with PBKDF2 key derivation
- **DataProtectionManager** — Data classification and protection policies

### Network Security
- **TLSManager** — TLS 1.3 certificate management and cipher suite configuration

### Disaster Recovery
- **DisasterRecoveryManager** — Backup, failover, and recovery orchestration

### Security Monitoring
- **SecurityMonitoring** — Real-time security event aggregation and alerting
- **IdentityManager** — Identity lifecycle management

## Supported Compliance Standards

| Standard | Description |
|----------|-------------|
| PCI DSS Level 1 | Payment card industry data security |
| SOX 404 | Sarbanes-Oxley Act |
| MiFID II | EU markets instrument directive |
| GDPR | EU data protection |
| ISO 27001 | Information security management |
| NIST CSF | US NIST cybersecurity framework |
| SOC 2 Type II | Service organization control |
| FIPS 140-2 Level 3 | Federal cryptographic standard |

## Installation

```bash
pip install bt_api_security
```

## Requirements

- Python >= 3.9
- pyjwt >= 2.8.0
- cryptography >= 41.0.0
- bcrypt >= 4.1.0
- pydantic >= 2.0.0

## Quick Start

### Authentication

```python
from bt_api_security import OAuth2Provider, MFAProvider

# OAuth2 authentication
oauth = OAuth2Provider(client_id="app", client_secret="secret")
token = oauth.get_token(scope="read write")

# MFA verification
mfa = MFAProvider()
verified = mfa.verify_totp(user_secret="JBSWY3DPEHPK3PXP", code="123456")
```

### Access Control

```python
from bt_api_security import AccessControlManager, Role, Permission

acm = AccessControlManager()
acm.assign_role(user_id="user_001", role=Role.TRADER)
acm.grant_permission(role=Role.TRADER, permission=Permission.PLACE_ORDER)
```

### Audit Logging

```python
from bt_api_security import AuditLogger, EventType

logger = AuditLogger()
logger.log_event(
    event_type=EventType.ORDER_PLACED,
    user_id="user_001",
    resource="BINANCE___SPOT:BTCUSDT",
    metadata={"order_id": "xyz", "volume": 0.5},
)
```

### Encryption

```python
from bt_api_security import EncryptionManager

enc = EncryptionManager()
ciphertext = enc.encrypt(plaintext="api_key_secret", associated_data="user_001")
plaintext = enc.decrypt(ciphertext=ciphertext, associated_data="user_001")
```

## API Reference

| Class | Description |
|--------|-------------|
| `OAuth2Provider` | OAuth 2.0 authentication provider |
| `MFAProvider` | TOTP/HOTP MFA verification |
| `AccessControlManager` | RBAC access control |
| `AuditLogger` | Immutable audit trail |
| `ComplianceMonitor` | Compliance rule enforcement |
| `ThreatDetector` | Threat pattern detection |
| `EncryptionManager` | AES-256-GCM encryption |
| `DataProtectionManager` | Data classification and protection |
| `TLSManager` | TLS 1.3 certificate management |
| `DisasterRecoveryManager` | Backup and failover |
| `SecurityMonitoring` | Security event monitoring |
| `IdentityManager` | Identity lifecycle management |

## Documentation

Full documentation available at [bt_api_py documentation](https://cloudquant.github.io/bt_api_py/).

## License

MIT License
