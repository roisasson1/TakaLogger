class Message:
    time = 0
    site = ""
    error_type = ""

    def __init__(self, i_site, i_error_type):
        self.site = i_site
        self.error_type = i_error_type
