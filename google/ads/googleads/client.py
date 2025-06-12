class GoogleAdsClient:
    @classmethod
    def load_from_dict(cls, config, *args, **kwargs):
        return cls()

    def get_service(self, name):
        class Service:
            def mutate_campaigns(self, *args, **kwargs):
                class Result:
                    resource_name = "customers/123/campaigns/1"

                return type("Response", (), {"results": [Result()]})()

        return Service()
