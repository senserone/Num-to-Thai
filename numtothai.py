# < 100 billion
# precision 2
# don't write ','

num = input('insert number: ')

read_digit = ['', 'สิบ', 'ร้อย', 'พัน', 'หมื่น', 'แสน', 'ล้าน']
read_num = ['', 'หนึ่ง', 'สอง', 'สาม', 'สี่',
            'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า', 'สิบ']


def split(word):
    return [char for char in word]


def readNumber(integer_number):
    nums = split(integer_number)
    nums_len = len(nums) - 1
    result = ''

    for n in nums:
        if nums_len > 6:
            tmp_len = nums_len % 6
        else:
            tmp_len = nums_len

        if n == '2' and tmp_len == 1:
            result += 'ยี่'
        elif n == '1' and tmp_len == 1:
            result += ''
        elif len(integer_number) > 1 and n == '1' and (tmp_len == 0 or nums_len == 6) :
            result += 'เอ็ด'
        else:
            result += read_num[int(n)]

        if(n != '0' or nums_len == 6):
            result += read_digit[tmp_len]
        
        nums_len -= 1

    return result


try:
    x = float(num)
    if(len(num.split('.')) > 1):
        parts = num.split('.')
        if(int(parts[0]) > 0):
            print(readNumber(parts[0]),end='บาท')
        if(int(parts[1][:2]) > 0):
            print(readNumber(parts[1][:2]),end='สตางค์')
        else:
            print('ถ้วน')
    else:
        print(readNumber(num),end='บาทถ้วน')
except ValueError:
    print('This is not proper number.')
