class Solution:
    def intToRoman(self, num: int) -> str:
        value_dict = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }
        buff = ""
        for roman, numeric in value_dict.items():
            num_symbols = num // numeric
            buff += num_symbols * roman
            num = num % numeric
            
        # cleanup
        buff = (buff
            .replace("DCCCC", "CM")
            .replace("CCCC", "CD")
            .replace("LXXXX", "XC")
            .replace("XXXX", "XL")
            .replace("VIIII", "IX")
            .replace("IIII", "IV")
        )
            
        return buff
