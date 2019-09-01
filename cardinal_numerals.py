#!/usr/bin/env python3
def integer_to_vietnamese_numeral(n):
	if type(n) is not int:
		raise TypeError('Not an integer!')
	elif n < 0:
		raise ValueError('Not a positive integer!')
	elif n > 999999999999:
		raise OverflowError('Overflow Value!')
	dict0_10 = {
		'0': 'không',
		'1': 'một',
		'2': 'hai',
		'3': 'ba',
		'4': 'bốn',
		'5': 'năm',
		'6': 'sáu',
		'7': 'bảy',
		'8': 'tám',
		'9': 'chín',
		'10': 'mười',
	}

	dict01_09 = {
		'00': ''
	}
	for i in range(1,10,1):
		key = '0' + str(i)
		dict01_09[key] = 'lẻ ' + dict0_10[str(i)]

	dict11_19 = {}
	for i in range(1,10,1):
		key = '1' + str(i)
		if i == 5:
			dict11_19[key] = 'mười lăm'
		else:
			dict11_19[key] = 'mười ' + dict0_10[str(i)]

	dict20_99 = {}
	for i in range(2,10,1):
		for j in range(10):
			key = str(i) + str(j)
			if j == 0:
				dict20_99[key] = dict0_10[str(i)] + ' mươi'
			elif j == 1:
				dict20_99[key] = dict0_10[str(i)] + ' mươi mốt'
			elif j == 5:
				dict20_99[key] = dict0_10[str(i)] + ' mươi lăm'
			else:
				dict20_99[key] = dict0_10[str(i)] + ' mươi ' + dict0_10[str(j)]

	list_n = []
	while n >= 1000:
		block = n % 1000
		list_n.append(block)
		n = n // 1000
	list_n.append(n)
	print(list_n)


integer_to_vietnamese_numeral(96)
integer_to_vietnamese_numeral(405)
integer_to_vietnamese_numeral(1915)
integer_to_vietnamese_numeral(5061)
integer_to_vietnamese_numeral(1002003)
integer_to_vietnamese_numeral(1000000)
integer_to_vietnamese_numeral(1030000)
integer_to_vietnamese_numeral(1002003)
integer_to_vietnamese_numeral(1002003004)
integer_to_vietnamese_numeral(1002000004)
integer_to_vietnamese_numeral(100000004)
integer_to_vietnamese_numeral(999999999999)