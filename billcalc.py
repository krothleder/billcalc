


def tip_given(bill_amt, tip_percent):
	tip = bill_amt*tip_percent
	return tip


def total_bill(tip_amt, bill_amt):
	total = bill_amt + tip_amt
	return total



def split_bill(bill_amt, num_people):
	split = bill_amt/num_people
	return split

# bill_amt = 10
# tip_percent = .1
# tip_amt = tip_given(bill_amt,tip_percent)
# print tip_amt


# print total_bill(tip_amt, bill_amt)

# print split_bill(bill_amt,10)


def main():
	# print total_bill(.1,10) 
	user_input = int(raw_input("Select 1 to calculate tip or 2 to split the bill:" + " "))
	if (user_input == 1):
		bill_input = float(raw_input("What is the bill amount?" + " "))
		tip_percent = float(raw_input("What is the tip percentage?" + " "))
		tip_amount = tip_given(bill_input, tip_percent)
		print "tip amount", tip_amount
		bill_amount_test = total_bill(tip_amount,bill_input)
		# bill_total = total_bill(tip_amount, bill_input)
		print "bill_total", bill_amount_test
		
		# print bill_total

		bill_split = raw_input("Do you want the bill split?")
		if (bill_split == 'yes'):
			split_ways = int(raw_input("How many ways do you want to split?"))
			split_bill_test = split_bill(bill_amount_test,split_ways)
			print split_bill_test




	elif (user_input ==2):
		total_bill = float(raw_input("What is the total bill?" + " "))
		num_people = int(raw_input("How many people to split amongst?" + " "))
		cost_pp = split_bill(total_bill,num_people)		
		print cost_pp

if __name__ == '__main__':
	main()












