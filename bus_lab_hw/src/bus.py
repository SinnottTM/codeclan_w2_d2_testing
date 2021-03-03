class Bus:

    # declare data-types
    route_number = int
    destination = str
    passengers = []
    total_passengers = int

    # initialise the Bus Class
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []
        self.total_passengers = len(self.passengers)

    # this bus is clearly noisy
    def drive(self):
        return "Brum brum"

    # passenger count on the bus
    def passenger_count(self):
        return self.total_passengers
    
    # passengers getting on the bus
    def pick_up(self, person):
        self.total_passengers += 1
        self.passengers.append(person)

    # passengers getting off the bus
    def drop_off(self, person):
        self.total_passengers -= 1
        self.passengers.remove(person)

    # emptying out the bus
    def empty(self):
        if self.total_passengers != 0:
            self.total_passengers = 0
            self.passengers = []
    
    # collecting from the bus_stop and clearing the bus stop to 0     
    def pick_up_from_stop(self, bus_stop):
        self.total_passengers += len(bus_stop.queue)
        self.passengers.append(bus_stop.queue)    
        bus_stop.queue.clear
    
    # Alternative if you make this with logic to cover total_passenger already
    # def pick_up_from_stop(self, bus_stop):
    #     self.passengers += bus_stop.queue
    #     bus_stop.queue.clear
