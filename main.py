from Rounder.rounder import rounder
TEST_NUM: int = 0


def run_test(rounded_value: float, expected_value: float) -> None:
	'''
	prints if the test passes or not

	Parameters
	----------
	rounded_value : float
		rounded value that has already been calculated
	expected_value : float
		expected correct answer
	'''
	global TEST_NUM
	passed = True if rounded_value == expected_value else False
	TEST_NUM += 1

	prefix = f'Test #{TEST_NUM} '
	text = prefix + 'passed' if passed else prefix + 'failed'
	print(text)
	if not passed:
		print(f'Rounded value: {rounded_value} | Expected: {expected_value}')


# test #3-#13 were taken with permission from here:
# https://github.com/Aethese/rounder/blob/main/tests.py
run_test( rounder(1.454545687975), 2 )
run_test( rounder(1.445, 1), 1.5 )
run_test( rounder(3.45631, 3), 3.456 )  # fails, doesn't cut off excess numbers
#run_test( round(3.45631, 3), 3.456 ) <- uncomment this to see round do this test correctly
run_test( rounder(3.45691, 3), 3.457 )  # suprisingly passes because excess is cut off
run_test( rounder('aethese #1', 1), 0 )  # no built-in checks to see if passed in value is what we expect
run_test( rounder(3.14, 5), 0 )  # no built-in checks here either
run_test( rounder(3.99, 1), 4 )  # failes, we somehow get 3.1 LMAO
run_test( rounder(3.44512), 4 )  # suprisingly passes??? ok
run_test( rounder(2.444444444445), 3 )
run_test( rounder(-3.5), -4 )  # returns -2 LOL
run_test( rounder(-3.3445), -3 )
run_test( rounder(-3.447), -4 )  # errors when you try to format the float lol
run_test( rounder(3.123124914285135135134, 3), 3.123 )  # idek how the answer given was calculated
