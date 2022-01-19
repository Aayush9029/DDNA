# Program that encodes and decodes string to DNA sequence
# It's like base64 but for DNA and worse :D


class DDNA:
    def __init__(self):
        self.bases = {
            "00": "A",
            "01": "C",
            "10": "G",
            "11": "T"
        }
        self.bases_rev = {
            "A": "00",
            "C": "01",
            "G": "10",
            "T": "11"
        }

    def convert_to_string(self, bits):
        """
        Converts bits to string
        Parametes:
            Binary bits 1's and 0's        
        Returns:
            String (sentences, words)
        """
        string = ""
        for i in range(0, len(bits), 8):
            char_bin = bits[i:i+8]
            char_int = int(char_bin, 2)
            char = chr(char_int)
            string += char
        return string

    def convert_to_bits(self, string):
        """
        Converts string to bits
        Parameters:
            String (sentences, words)
        
        Returns:
            Binary bits 1's and 0's
        """

        bits = ""
        for char in string:
            # convert char to int
            char_int = ord(char)
            # convert int to binary
            char_bin = bin(char_int)[2:]
            # add 0's to binary to make it 8 bits
            char_bin = char_bin.zfill(8)
            bits += char_bin
        return bits

    
    def encode(self, string):
        """"
        Encodes String to DNA bases
        Parameters:
            String (sentences, words)
        
        Returns:
            DNA sequence ACTG ATAT...
        """

        bits = self.convert_to_bits(string)

        encoded_bits = ""
        for i in range(0, len(bits), 2):
            encoded_bits += self.bases[bits[i:i+2]]
        return encoded_bits
    
    def decode(self, string):
        """"
        Decodes DNA bases to String
        Parameters:
            DNA sequence ACTG ATAT...
        
        Returns:
            String (sentences, words)
        """
        bits = ""
        for char in string:
            bits += self.bases_rev[char]
        
        return self.convert_to_string(bits)






encoded = DDNA().encode("A Quick Brown Fox")
print(encoded)

decoded = DDNA().decode(encoded)
print(decoded)

        
    


