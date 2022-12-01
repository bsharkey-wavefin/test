#!/usr/bin/env python3

print("test")
print("test2")

key = b'-8B key-'
DES.new(key, DES.MODE_OFB) # Noncompliant: DES works with 56-bit keys allow attacks via exhaustive search

num1 = 1
num2 = 10

num2 =- num1
num2 =+ num1

if num1 <> num2:
    print("not equal")
