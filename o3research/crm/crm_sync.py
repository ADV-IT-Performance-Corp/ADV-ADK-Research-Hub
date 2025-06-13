from __future__ import annotations

import json
import time
from typing import Mapping, Any
from urllib import request

__version__ = "4.0.0"


def sync_to_crm(
    record: Mapping[str, Any],
    token: str,
    base_url: str = "https://api.example-crm.com",
) -> str:
    """Send *record* to the CRM using the provided API *token*.

    Parameters
    ----------
    record:
        Lead fields to push.
    token:
        Bearer token for authentication.
    base_url:
        CRM API base URL.

    Returns
    -------
    str
        Identifier of the synced lead.
    """
    start = time.perf_counter()
    data = json.dumps(record).encode("utf-8")
    req = request.Request(
        f"{base_url}/leads",
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with request.urlopen(req, timeout=10) as resp:
        resp_data = json.loads(resp.read().decode("utf-8"))
    latency = time.perf_counter() - start
    return f"Lead {resp_data.get('id', 'unknown')} synced in {latency:.2f}s"
