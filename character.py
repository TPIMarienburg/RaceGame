class Driver:
    def __init__(self, tires=0, brakes=0, transmission=0, body=0, engine=0, suspension=0):
        self.stats = {
            "Tires": {"max":tires, "current":tires},
            "Brakes": {"max":brakes, "current":brakes},
            "Transmission": {"max":transmission, "current":transmission},
            "Body": {"max":body, "current":body},
            "Engine": {"max":engine, "current":engine},
            "Suspension": {"max":suspension, "current":suspension}
        }
        self.possition = 0
        self.space = 0

    def check_for_valid(self):
        # check to see if the driver/car stats meet the minimum legal starting requirements
        if self.total_check() and self.check_for_zeros_in_max():
            return True
        else:
            return False

    def total_check(self):
        # make sure that the sum of all the max stats is 20
        total_stats = sum([self.stats[x]["max"] for x in self.stats.keys()])
        if total_stats == 20:
            return True
        else:
            return False

    def check_for_zeros_in_max(self):
        # make sure that none of the stats are 0
        for key in self.stats.keys():
            if self.stats[key]["max"]/1 == 0.0:
                return False
            else:
                pass
            return True

    def check_for_zeros_in_current(self):
        # make sure that none of the stats are 0
        for key in self.stats.keys():
            if self.stats[key]["current"]/1 == 0.0:
                return False
            else:
                pass
            return True

    def set_position(self):
        pass

    def set_space(self):
        pass

    return current_stats(self):
        pass
