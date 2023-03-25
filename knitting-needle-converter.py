size_japanese_to_mm = {0: 2.10, 1: 2.40, 2: 2.70, 3: 3.00, 4: 3.30, 5: 3.60, 6: 3.90, 7: 4.20, 8: 4.50, 9: 4.80, 10: 5.10, 11: 5.40, 12: 5.70, 13: 6.00, 14: 6.30, 15: 6.60}

size_amarican_to_mm = {0: 2.00, 1: 2.25, 2: 2.75, 3: 3.25, 4: 3.50, 5: 3.75, 6: 4.00, 7: 4.50, 8: 5.00, 9: 5.50, 10: 6.00, 10.5: 6.50, 11: 8.00, 13: 9.00, 15: 10.00, 17: 12.75, 19: 15.00, 35: 19.00, 50: 25.00}

class Needle:
    def __init__(self, sizemm, size_japanese, size_american):
        self.sizemm = sizemm
        self.size_japanese = size_japanese
        self.size_american = size_american
    
