import random

def generate_code(src, length):
    # print('length: %d' % length)
    str=''
    while len(str)<length:
        str=str+random.choice(src)
    # print('vorcher_code: %s' % str)
    return str

if __name__=='__main__':
    src= 'abcdefghijklmnopqrstuvwxyz1234567890[]\\;:{}\'\"|,./<>?!@#$5^&*()-_ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(1,201):
        print('vorcher code # %d: %s' % (i, generate_code(src,16)))