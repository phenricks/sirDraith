class ResponseApi:
    def __init__(self):
        self.message = None

    def create_response(self, message: str):
        self.message = message
        return {"message": self.message}
