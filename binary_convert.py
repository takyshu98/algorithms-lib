def convert_from_decimal_to_binary(decimal, output_digits):
  binary = ''
  for i in range(output_digits - 1, -1, -1):
    # 対象10進数の2進数表現において右シフト（= ÷ 2）を繰り返しその桁のbitが立っているか検査する
    if decimal >> i & 1:
      binary += '1'
    else:
      binary += '0'
  return binary

def main():
    print('target decimal = ', end='')
    decimal = int(input())

    print('format(decimal, \'b\').zfill(3)  =', format(decimal, 'b').zfill(10))
    print('convert_from_decimal_to_binary =', convert_from_decimal_to_binary(decimal, 10))

if __name__ == '__main__':
    main()