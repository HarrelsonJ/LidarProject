class SCAN:
    def __init__(self, time, *args) -> None:
        self.time = time # System clock when scan was taken
        self.scans = [] # [[angle0, range0], [angle1, range1], [angle2, range2], [angle3, range3]]
        for result in args: # result = [angle, range]
            self.scans.append(result)

    def data(self) -> list[list]:
        return self.scans