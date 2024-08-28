class HammingDistance:
    @staticmethod
    def compute(str1, str2):
        if len(str1) != len(str2):
            raise ValueError("Strings must be of the same length.")
        return sum(el1 != el2 for el1, el2 in zip(str1, str2))
