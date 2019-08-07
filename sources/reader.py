
class IO:
    def __init__(self, filename):
        self.file = open(filename, "rb")

    def setSeek(self, start):
        if self.file is not None:
            self.file.seek(start)

    def readChunk(self, start, size):
        if self.file is not None:
            self.file.seek(start)
            return self.file.read(size)
        else:
            return None

    def __del__(self):
        if self.file is not None:
            self.file.close()