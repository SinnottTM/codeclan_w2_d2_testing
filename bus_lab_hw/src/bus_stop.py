class BusStop:

    # declare data-types
    name = str
    queue = []

    # Initialise the BusStop Class
    def __init__(self, name):
        self.name = name
        self.queue = []

    # adding ppl to the bus stop queue
    def add_to_queue(self, person):
        self.queue.append(person)

    # getting the length of the queue at the bus stop
    def queue_length(self):
        return len(self.queue)

    # empty the queue at the bus stop
    def clear(self):
        if len(self.queue) > 0:
            self.queue = []
