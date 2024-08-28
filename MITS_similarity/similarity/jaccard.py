class JaccardCoefficient:
    @staticmethod
    def compute(str1, str2):
        set1 = set(str1)
        set2 = set(str2)
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        return intersection / union
