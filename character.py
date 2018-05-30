class Driver:
    def __init__(
        self,
        tires=0,
        brakes=0,
        transmission=0,
        body=0,
        engine=0,
        suspension=0
    ):
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
        self.gear = 1
        self.tires = "Hard"

    def check_for_valid(self):
        # check to see if the driver/car stats meet the minimum legal starting
        # requirements
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

    def set_position(self, new_position):
        self.position = new_position

    def return_position(self):
        return self.position

    def set_space(self, new_space):
        self.space = new_space

    def return_space(self):
        return self.space

    def return_current_stats(self):
        return [self.stats[x]["current"] for x in self.stats.keys()]

    def shift(self, target_gear):
        """
        Checks to see what the current transmission stat is.  If the stat is
        higher than 0 then gear skipping will be allowed.

        Gears can only be skipped when down shifting.

        Gear skipping will cause damage to car parts.

        ------------------------------------------------------------------------
        | Gears Skipped | Transmission Damage | Brake Damage | Engine Damage   |
        ------------------------------------------------------------------------
        | 1 Gear        |           1         |      0       |       0         |
        ------------------------------------------------------------------------
        | 2 Gears       |           1         |      1       |       0         |
        ------------------------------------------------------------------------
        | 3 Gears       |           1         |      1       |       1         |
        ------------------------------------------------------------------------

        :direction: a string value; either up or down
        """
        # check the difference between the current gear and the target gears
        gear_diff = self.gear - target_gear
        if  5 > gear_diff > 1:
            self.gear_skipping(target_gear)
        elif (gear_diff == -1) or (gear_diff == 1):
            self.gear = target_gear
        elif gear_diff > 4:
            raise ValueError("Cannot downshift more than 4 gears at a time")
        elif gear_diff < -1:
            raise ValueError("Cannot skip gears while up shifting")

        def gear_skipping(self, target_gear):
            """
            Checks to make sure that skipping gears is possible

            :target_gear:
            """
            if self.stats["Transmission"]["current"] == 0:
                raise ValueError("Cannot skip gears with Transmission stat of 0")
            elif gear_diff == 2:
                self.damage_transmission()
                self.gear = target_gear
            elif gear_diff == 3:
                self.damage_transmission()
                self.damage_brakes()
                self.gear = target_gear
            elif gear_diff == 4:
                self.damage_transmission()
                self.damage_brakes()
                self.damage_engine()
                self.gear = target_gear
            else:
                pass

    def pit(self):
        self.stats["Tires"]["current"] = self.stats["Tires"]["max"]

    def damage_transmission(self):
        self.stats["Transmission"]["current"] -= 1

    def damage_suspension(self):
        self.stats["Suspension"]["current"] -= 1

    def damage_tires(self):
        self.stats["Tires"]["current"] -= 1

    def damage_engine(self):
        self.stats["Engine"]["current"] -= 1

    def damage_body(self):
        self.stats["Body"]["current"] -= 1

    def damage_brakes(self):
        self.stats["Brakes"]["current"] -= 1
