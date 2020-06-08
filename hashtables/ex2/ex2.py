#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    current_city = "NONE"
    route = []

    for i in tickets:
        #     current_city = tickets[i]
        #     cache[current_city.source] = current_city.destination
        if i.source not in cache:
            if i.source is current_city:
                route.append(i.destination)
            else:
                cache[i.source] = i.destination

    for i in range(0, length):
        if len(route) == length:
            return route
        else:
            route.append(cache[route[i]])

    # route[0] = cache["NONE"]
    # route[1] = cache[route[0]]

    # if length > 2:
    #     for i in range(2, length):
    #         route[i] == cache[route[i-1]]

    # for ticketroute in tickets:
    #     if ticketroute == current_city:
    #         route[0] = ticketroute.destination
    #     cache[ticketroute.source] = ticketroute.destination

    # return route
