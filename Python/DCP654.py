def main():
    given_string = 'jiujitsu'
    unique_chars = set(given_string)
    print(get_substring_length(given_string, unique_chars))
        
def get_substring_length(given_string, unique_chars):
    length = len(given_string)
    for j in range(0, len(given_string)):
        substring_length  = len(unique_chars) + j
        for i in range (0, len(given_string) - (substring_length) + 1):
            print(given_string[i:substring_length+i])
            if set(given_string[i:substring_length+i]) == unique_chars:
                return substring_length
    return length

def test_case():
    given_string = 'aaahaaa'
    unique_chars = set(given_string)
    print(get_substring_length(given_string, unique_chars))

test_case()