#
# strings vs bytes
# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values
#

def main():
    # define some starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b) # b'ABCD'
    
    s = "This is a string"
    print(s) # This is a string
    
    # Try combining them
    # print(s+b) # TypeError: can only concatenate str (not "bytes") to str
    
    # Bytes and strings need to be properly encoded and decoded
    # before you can work on them together
    s2 = b.decode("utf-8")
    print(s+s2) # This is a stringABCD
    
    b2 = s.encode("utf-8")
    print(b+b2) # b'ABCDThis is a string'

    # encode the string as utf-32
    b3 = s.encode("utf-32")
    print(b3) # b'\xff\xfe\x00\x00T\x00\x00\x00h\x00\x00\x00i\x00\x00\x00s\x00\x00\x00 \x00\x00\x00i\x00\x00\x00s\x00\x00\x00 \x00\x00\x00a\x00\x00\x00 \x00\x00\x00s\x00\x00\x00t\x00\x00\x00r\x00\x00\x00i\x00\x00\x00n\x00\x00\x00g\x00\x00\x00'

if __name__ == "__main__":
    main()
