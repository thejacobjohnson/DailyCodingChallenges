import random

def reverse_bits(bit_number):
    print('{:032b}'.format(bit_number))
    reversed_bits = (~bit_number)+2**32 # ~ returns bit complement. 2**32 creates unsigned 32 bit
    print('{:032b}'.format(reversed_bits))
    return reversed_bits

bit_number = random.randint(1,2**32-1) # generate random 32bit int
reverse_bits(bit_number)
