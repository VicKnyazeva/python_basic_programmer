# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_encode(text):
    result = ''
    count = 0
    prev_ch = '.'
    for curr_ch in text:
        if curr_ch == prev_ch:
            count += 1
            if count == 9:
                result += str(count) + prev_ch
                count = 0
        else:
            if count > 0:
                result += str(count) + prev_ch
            prev_ch = curr_ch
            count = 1

    if count > 0:
        result += str(count) + prev_ch

    return result


def rle_decode(encoded):
    result = ''
    count = 0
    for ch in encoded:
        if count == 0:
            count = int(ch)
        else:
            result += ch * count
            count = 0

    return result


def test(srctext):
    encoded = rle_encode(srctext)
    decoded = rle_decode(encoded)

    print('---')
    print('srctext =', srctext)
    print('encoded =', encoded)
    print('decoded =', decoded,
          '(совпадает с исходным текстом)' if srctext == decoded else '(оличатся от исходного текста)')


test("")
test("01234")
test("aa55 -@bbbcd8888ggggggggggggggggggg123")
