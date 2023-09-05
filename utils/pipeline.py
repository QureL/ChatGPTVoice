class AbstractPipeline:

    def __init__(self, interceptor=None) -> None:
        self.interceptor = interceptor

    def put(self, msg):
        raise NotImplementedError()

    def get(self):
        raise NotImplementedError()
