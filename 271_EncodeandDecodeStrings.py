# Example 1:
# Input: ["neet","code","love","you"]
# Output:["neet","code","love","you"]

# Example 2:
# Input: ["we","say",":","yes"]
# Output: ["we","say",":","yes"]
from typing import List

def encode(strs: List[str]) -> str:
    encoded_str = ""
    for s in strs:
        encoded_str += str(len(s)) + "#" + s
    return encoded_str

def decode(s: str) -> List[str]:
    decoded_list = []
    i = 0

    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        
        length = int(s[i:j])
        i = j + 1
        j = i + length

        word = s[i:j]
        decoded_list.append(word)     
        i = j
    return decoded_list


test1_s = ["neet","code","love","you"]
decode(encode(test1_s))
test1_encode_expected = "4#neet4#code4#love3#you"
test1_encode_actual = encode(test1_s)

test1_decode_expected = ["neet","code","love","you"]
test1_decode_actual = decode(encode(test1_s))

assert test1_encode_actual == test1_encode_expected, f"Test 1 encode actual is expected to be {test1_encode_expected} but is actually {test1_encode_actual}."
assert test1_decode_actual == test1_decode_expected, f"Test 1 decode actual is expected to be {test1_decode_expected} but is actually {test1_decode_actual}."
