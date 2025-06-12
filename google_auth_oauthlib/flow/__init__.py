class InstalledAppFlow:
    @classmethod
    def from_client_secrets_file(cls, filename, scopes):
        return cls()

    def run_local_server(self, *args, **kwargs):
        return "token"
