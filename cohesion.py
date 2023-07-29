import os


# before refactoring
class ApiClient:
    def __init__(self) -> None:
        self.api_key = os.getenv("API_KEY")  # dependency
        self.timeout = int(os.getenv("API_TIMEOUT"))  # dependecy


class Service:
    def __init__(self):
        self.api_client = ApiClient()  # dependency


def main():
    service = Service()  # dependency


if __name__ == "__main__":
    main()


# after refactoring


class ApiClient:
    def __init__(self, api_key: str, timeout: int) -> None:
        self.api_key = api_key
        self.timeout = timeout


class Service:
    def __init__(self, api_client):
        self.api_client = api_client


def main(service: Service):
    ...


if __name__ == "__main__":
    main(
        service=Service(
            api_client=ApiClient(
                api_client=os.getenv("API_KEY"), timeout=int(os.getenv("API_TIMEOUT"))
            )
        )
    )
