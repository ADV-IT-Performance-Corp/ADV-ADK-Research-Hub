# Phase 4 Blueprint: Runtime Fixes and A2A Integration

## Executive Summary
Phase 4 focuses on stabilizing the runtime and completing the Agent-to-Agent (A2A) rollout. The goal is smoother orchestration across agents and consistent CI/CD validation. Key deliverables include bug fixes, updated configuration hooks and clear doc updates.

## Root-Cause Matrix
| Issue | Root Cause | Fix |
|-------|------------|-----|
| Memory spikes on long runs | Missing cache cleanup | Add `cleanup_memory()` after each task |
| A2A message delays | Unoptimized routing table | Enable async queue with backoff |
| CI failures on new agents | Version mismatch | Standardize version pins in `settings.yaml` |

## Task Table
| Task | Owner | Priority |
|------|-------|---------|
| Patch cache logic | dev-team | High |
| Deploy async queue | ops-team | High |
| Update docs & settings | docs-team | Medium |

## `dev_setup.sh` Snippet

```bash
info "Installing Python 3.11 via pyenv..."
if ! command -v pyenv >/dev/null 2>&1; then
  apt-get update -qq
  DEBIAN_FRONTEND=noninteractive apt-get install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev \
    libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev >/dev/null
  curl -fsSL https://pyenv.run | bash
  export PATH="$HOME/.pyenv/bin:$PATH"
  eval "$(pyenv init -)"
fi

pyenv install -s 3.11.9
pyenv local 3.11.9
```

## CI YAML Snippet

```yaml
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python }}

      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.node }}

      - name: Install gcloud CLI
        run: |
          URL=https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-475.0.0-linux-x86_64.tar.gz
          curl -sSL "$URL" | tar -xz
          ./google-cloud-sdk/install.sh --quiet

      - name: Install Node dependencies
        run: npm ci --omit=optional

      - name: Install Python dependencies
```

## Doc-change Table
| File | Purpose |
|------|---------|
| `docs/Phase_4_Blueprint.md` | Outline of runtime fixes and A2A integration |
| `README.md` | Link to the new blueprint |

## Week 1–3 Timeline
- **Week 1**: Finalize bug fixes and test A2A queue
- **Week 2**: Roll out updated CI workflows
- **Week 3**: Document results and prep for next phase
