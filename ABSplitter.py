class ABSplitter(object):
    """
    Decide if a given user should be allocated to Version A or Version. Weights for
    A and B decide how the split will happen. Ensures balancing of allocations
    """
    VERSION_A_WEIGHT = 0.0
    VERSION_B_WEIGHT = 0.0
    counter = 0
    total_A = 0
    total_B = 0

    def reset(self, VERSION_A_WT, VERSION_B_WT):
        """
        Reset counters
        """
        self.VERSION_A_WEIGHT = VERSION_A_WT
        self.VERSION_B_WEIGHT = VERSION_B_WT
        self.counter = 0
        self.total_A = 0
        self.total_B = 0

    def getNextVersion(self):
        """
        Get which version the user should be allocated to
        """

        # Default to Version A
        current_version = 'VERSION_A'

        # Get the split point
        split = self.VERSION_A_WEIGHT / 100.0

        # Raise error if A and B weights do not add up to 100
        if ((self.VERSION_A_WEIGHT + self.VERSION_B_WEIGHT) != 100):
            print("Error: Weights do not add up to 100")
            current_version = 'VERSION_A'
            self.total_A += 1

        # Handle this edge case -- If A:B is 100:0
        elif self.VERSION_A_WEIGHT == 100:
            current_version = 'VERSION_A'
            self.total_A += 1

        # Handle this dge case -- If A:B is 0:100
        elif self.VERSION_B_WEIGHT == 100:
            current_version = 'VERSION_B'
            self.total_B += 1

        # Avoids divide by zero first time around, just allocate to Version A 
        elif self.counter == 0:
            current_version = 'VERSION_A'
            self.total_A += 1

        # It's neither of the edge or special cases, assign as per formula
        else:
            """
            Dividing 'total A allocations' by 'total allocations' will yield a number
            If this number is less than or equal to 'split' value then allocate user
            to Version A, otherwise allocate to Version B. Multiple iterations will yield
            a spread out distribution with reference to the 'split' point
            """
            if ((float(self.total_A) / float(self.counter)) <= split):
                current_version = 'VERSION_A'
                self.total_A += 1
            else:
                current_version = 'VERSION_B'
                self.total_B += 1

        self.counter += 1

        return current_version
