class OverlapCoefficient:
    @staticmethod
    def compute(str1, str2):
        set1 = set(str1)
        set2 = set(str2)
        intersection = len(set1.intersection(set2))
        smaller_set_size = min(len(set1), len(set2))
        return intersection / smaller_set_size
