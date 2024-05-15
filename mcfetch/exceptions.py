class RequestFailedError(Exception):
    """Whoops"""

    def __init__(self, e: Exception) -> None:
        self.original = e
        super().__init__(f"Request raised an exception: {e.__class__.__name__}: {e}")
