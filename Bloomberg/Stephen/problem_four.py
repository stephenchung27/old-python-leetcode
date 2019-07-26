class StationChecker:
    def __init__(self):
        self.station_to_station = collections.defaultdict(dict)
        self.cards = {}

    def swipe_in(from_time, from_station_id, card_id):
        self.cards[card_id] = (from_station_id, from_time)

    def swipe_out(to_time, to_station_id, card_id):
        from_station_id, from_time = self.cards[card_id]

        if "total_time" in self.station_to_station[(from_station_id, to_station_id)]:
            self.station_to_station[(
                from_station_id, to_station_id)]["total_time"] += to_time - from_time
            self.station_to_station[(
                from_station_id, to_station_id)]["count"] += 1
        else:
            self.station_to_station[(
                from_station_id, to_station_id)]["total_time"] = to_time - from_time
            self.station_to_station[(
                from_station_id, to_station_id)]["count"] = 1

        del self.cards[card_id]

    def get_average_travel_time(from_station_id, to_station_id):
        total_time, count = self.station_to_station[(
            from_station_id, to_station_id)]

        return total_time / count
