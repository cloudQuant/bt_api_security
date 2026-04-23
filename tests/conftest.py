from __future__ import annotations

import sys
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PACKAGE_ROOT / "src"
REPO_ROOT = PACKAGE_ROOT.parents[1]

for path in (SRC_ROOT, REPO_ROOT):
    text = str(path)
    if text not in sys.path:
        sys.path.insert(0, text)

import bt_api_security
import bt_api_security.auth
import bt_api_security.auth.mfa_provider
import bt_api_security.auth.oauth2_provider
import bt_api_security.core
import bt_api_security.core.access_control
import bt_api_security.core.audit_logger
import bt_api_security.core.compliance_monitor
import bt_api_security.core.encryption_manager
import bt_api_security.core.identity_manager
import bt_api_security.core.threat_detection
import bt_api_security.data
import bt_api_security.data.protection
import bt_api_security.framework
import bt_api_security.monitoring
import bt_api_security.monitoring.security_monitoring
import bt_api_security.network
import bt_api_security.network.tls_manager
import bt_api_security.recovery
import bt_api_security.recovery.disaster_recovery

sys.modules["bt_api_py.security_compliance"] = bt_api_security
sys.modules["bt_api_py.security_compliance.auth"] = bt_api_security.auth
sys.modules["bt_api_py.security_compliance.auth.mfa_provider"] = bt_api_security.auth.mfa_provider
sys.modules["bt_api_py.security_compliance.auth.oauth2_provider"] = bt_api_security.auth.oauth2_provider
sys.modules["bt_api_py.security_compliance.core"] = bt_api_security.core
sys.modules["bt_api_py.security_compliance.core.access_control"] = bt_api_security.core.access_control
sys.modules["bt_api_py.security_compliance.core.audit_logger"] = bt_api_security.core.audit_logger
sys.modules["bt_api_py.security_compliance.core.compliance_monitor"] = bt_api_security.core.compliance_monitor
sys.modules["bt_api_py.security_compliance.core.encryption_manager"] = bt_api_security.core.encryption_manager
sys.modules["bt_api_py.security_compliance.core.identity_manager"] = bt_api_security.core.identity_manager
sys.modules["bt_api_py.security_compliance.core.threat_detection"] = bt_api_security.core.threat_detection
sys.modules["bt_api_py.security_compliance.data"] = bt_api_security.data
sys.modules["bt_api_py.security_compliance.data.protection"] = bt_api_security.data.protection
sys.modules["bt_api_py.security_compliance.framework"] = bt_api_security.framework
sys.modules["bt_api_py.security_compliance.monitoring"] = bt_api_security.monitoring
sys.modules["bt_api_py.security_compliance.monitoring.security_monitoring"] = bt_api_security.monitoring.security_monitoring
sys.modules["bt_api_py.security_compliance.network"] = bt_api_security.network
sys.modules["bt_api_py.security_compliance.network.tls_manager"] = bt_api_security.network.tls_manager
sys.modules["bt_api_py.security_compliance.recovery"] = bt_api_security.recovery
sys.modules["bt_api_py.security_compliance.recovery.disaster_recovery"] = bt_api_security.recovery.disaster_recovery

try:
    import bt_api_py

    bt_api_py.security_compliance = bt_api_security
except ImportError:
    pass
