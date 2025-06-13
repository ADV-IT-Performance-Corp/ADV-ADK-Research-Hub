# limit_output
MAX_BYTES = 1600


class _LimitedIO:
    """Wrap a text stream to limit total bytes written."""

    def __init__(self, stream, limit: int = MAX_BYTES):
        self.stream = stream
        self.remaining = limit

    def write(self, data: str) -> None:
        if self.remaining <= 0:
            return
        # Slice to avoid encoding very long strings
        encoded = data[:200].encode(self.stream.encoding or "utf-8", errors="replace")
        chunk = encoded[: self.remaining]
        self.stream.buffer.write(chunk)
        self.remaining -= len(chunk)

    def flush(self) -> None:
        self.stream.flush()
