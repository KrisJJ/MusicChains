class Buffer:
    def __init__(self):
        self.inner = ''

    def clear(self):
        self.inner = ''

    def add(self,c):
        self.inner += c

    def get(self):
        return self.inner

    def isempty(self):
        return self.inner==''
