import argparse

def check_number(number):
  value = str(number)
  return check_double(value)*check_increasing(value)

def check_double(string):
  prev_digit = ''
  for digit in string:
    if not prev_digit:
      prev_digit = digit
      continue
    if digit == prev_digit:
      return 1
    prev_digit = digit
  return 0

def check_increasing(string):
  prev_digit = -1
  for digit in string:
    digit = int(digit)
    if prev_digit == -1:
      prev_digit = digit
      continue
    if digit < prev_digit:
      return 0
    prev_digit = digit
  return 1

parser = argparse.ArgumentParser(description='Day 4 Part 1')
parser.add_argument('range', help='The range of numbers to look at (number-number)')
args = parser.parse_args()

start = int(args.range.split('-')[0])
end = int(args.range.split('-')[1])

number = start
valid = 0
while number <= end:
  valid += check_number(number)
  number+=1

print(valid)