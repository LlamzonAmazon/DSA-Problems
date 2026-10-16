class UndergroundSystem:

    def __init__(self):

        self.departures = {} # { id : [start,time] }
        self.travelTimes = {} # { (start,end) : [totalTime,count] }
        
    def checkIn(self, id: int, startStation: str, t: int) -> None:

        self.departures[id] = [startStation, t] # Overwrite traveller's last trip

    def checkOut(self, id: int, endStation: str, t: int) -> None:

        startStation, time = self.departures[id]
        trip = (startStation, endStation)

        if trip not in self.travelTimes:
            self.travelTimes[trip] = [t-time, 1]
        else:
            self.travelTimes[trip][0] += t - time
            self.travelTimes[trip][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, count = self.travelTimes[(startStation, endStation)]

        return totalTime / count
        