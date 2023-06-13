#!/usr/bin/env python

import math
hashcabinet_file = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def initialize_hash_obj(hashlength):
    """
    Initializes the hash object (array) with given length.
    
    Arguments:
    hashlength -- The length of the hash object.
    
    Returns:
    An array initialized with None values.
    """
    return [0] * hashlength

def convert_to_alphanumeric(value):
    """
    Converts the given value (0-25) to alphanumeric character.
    
    Arguments:
    value -- The value to convert.
    
    Returns:
    The corresponding alphanumeric character.
    """
    if 0 <= value <= 25:
        return hashcabinet_file[value]
    else:
        raise ValueError("Invalid value for conversion: {}".format(value))



def convert_from_alphanumeric(char):
    """
    Converts the given alphanumeric character to its value (0-25).
    
    Arguments:
    char -- The alphanumeric character to convert.
    
    Returns:
    The corresponding value (0-25).
    """
    if 'a' <= char <= 'z':
        return hashcabinet_file.index(char)
    else:
        raise ValueError("Invalid alphanumeric character: {}".format(char))


def is_prime(number):
    """
    Checks if the given number is prime.
    
    Arguments:
    number -- The number to check.
    
    Returns:
    True if the number is prime, False otherwise.
    """
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def find_greatest_prime(limit):
    """
    Finds the greatest prime number less than or equal to the given limit.
    
    Arguments:
    limit -- The upper limit to search for prime number.
    
    Returns:
    The greatest prime number less than or equal to the limit.
    """
    for num in range(limit, 1, -1):
        if is_prime(num):
            return num
    return 2  # If no prime number found, default to 2

def hash_function(hashobj, tobehashed, hash_signature):
    """
    Computes the hash value based on the given hash object, input string, and hash signature.
    
    Arguments:
    hashobj -- The hash object (array).
    tobehashed -- The input string to be hashed.
    hash_signature -- The lowest prime possible (hash signature).
    
    Returns:
    The updated hash object.
    """
    index = 0
    for char in tobehashed:
        if 'a' <= char <= 'z':
            value = convert_from_alphanumeric(char)
            index = index + hash_signature
            indexmod = index % len(hashobj)
            hashcounter = int(hashobj[indexmod])
            hashobj[indexmod] = (value + hashcounter) % 23
    
    return hashobj

def display_hash(hashobj):
    """
    Converts the hash object to a string and displays the hash.
    
    Arguments:
    hashobj -- The hash object (array).
    """
    hash_str = ''.join(convert_to_alphanumeric(value) for value in hashobj)
    print("Hash: ", hash_str)




# Main program
hashlength = int(input("Enter the hash length: "))
hashobj = initialize_hash_obj(hashlength)
tobehashed = input("Enter the input string to be hashed: ")
hash_signature =   find_greatest_prime(hashlength-1)

hashobj = hash_function(hashobj, tobehashed, hash_signature)

show_hashobj = input("Do you want to see the hash object? (yes/no): ")
if show_hashobj.lower() == "yes":
    for i in range(len(hashobj)):
        print(hashobj[i])

show_hash = input("Do you want to see the hash? (yes/no): ")
if show_hash.lower() == "yes":
    display_hash(hashobj)
