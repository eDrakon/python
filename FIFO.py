class QueueError(IndexError):  # Eligir la clase base para la nueva excepción.
    #
    #  Escribe el código aquí.
    #
    def __init__(self):
        Exception.__init__(self)
        print('Error, el elemento no existe.')

class Queue:
    def __init__(self):
        #
        # Escribe el código aquí.
        #
        self.__queue = []

    def put(self, elem):
        #
        # Escribe el código aquí.
        #
        self.__queue.insert(0, elem)
    def get(self):
        #
        # Escribe el código aquí.
        #
        if len(self.__queue) > 0:
            val = self.__queue[-1]
            self.__queue.pop(-1)
            return val
        else:
            raise QueueError

    def get_len(self):
        return len(self.__queue)

class SuperQueue(Queue):
    def isempty(self):
        return self.get_len() == 0


que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")