def reverse_slicing(s):
    print("reverse_slicing:")
    print(s)
    return s[::-1]


def create_mask():
    # From: http://www.cdg.org/technology/cdma_technology/a_ross/LongCode.asp
    lbytes = [42, 35, 33, 31, 27, 26, 25, 22, 21, 19, 18, 17, 16, 10, 7, 6, 5, 3, 2, 1]
#             42, 35, 33, 31, 27, 26, 25, 22, 21, 19, 18, 17, 16, 10, 7, 6, 5, 3, 2, 1


    # from tz.txt
    #lbytes = [42, 41, 40, 39, 37, 36, 35, 32, 26, 25, 24, 23, 21, 20, 17, 16, 15, 11, 9, 7, 1]
    
    # from TZ revert
    # Polinomial[42] = {1 1 1 1 0 1 1 1 0 0 1 0 0 0 0 0 1 1 1 1 0 1 1 0 0 1 1 1 0 0 0 1 0 1 0 1 0 0 0 0 0 1};
    lbytes = [1, 2, 3, 4, 6, 7, 8, 11, 17, 18, 19, 20, 22, 23, 26, 27, 28, 32, 34, 36, 42]
    #----------------------------------------------------------------------------------

    res = 0
    for s in lbytes:
        res = (1 << (s - 1)) | res
    
    return res

if __name__ == "__main__":
    mask = create_mask()
    print("FMASKX:\n{} {}".format(hex(mask), bin(mask)))

    print("RMASKX:\n{}".format(reverse_slicing(bin(mask))))

    print('test:\n', reverse_slicing('111101110010000011110110011100010101000001'))
    # 1011010000000000 B400
    # 0000000000101101 002D

    #3CA29D0CCCF 0011 1100 1010 0010 1001 1101 0000 1100 1100 1100 1111

'''
If you need bit k (k = 0 ..15), you can do the following:

return (lfsr >> k) & 1;
This shifts the register kbit positions to the right and masks the least significant bit.
'''
# 13C69DAC953
# 13C69DAC953