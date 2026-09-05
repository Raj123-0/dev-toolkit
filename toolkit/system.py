import os
import platform
import sys
from typing import Dict, Any

def get_system_summary() -> Dict[str, Any]:
    """Return runtime host and python environment diagnostics."""
    return {
        "platform": platform.platform(),
        "python_version": sys.version.split()[0],
        "cpu_count": os.cpu_count() or 1,
        "architecture": platform.machine()
    }
