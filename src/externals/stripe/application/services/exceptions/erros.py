class Error(Exception):
    def __init__(self):
        self.msg = ""
        self.status_code = 500

    def __str__(self):
        return self.msg


class FaliedSaveUser(Error):
    def __init__(self):
        self.msg = "Failed to save user"
        self.status_code = 400
