from yapsy.IPlugin import IPlugin


class IExtension(IPlugin):

    def __init__(self):
        super().__init__()

    def get_tasks(self):
        pass
