# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: olyen <olyen@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/20 22:02:54 by olyen             #+#    #+#              #
#    Updated: 2026/10/20 23:37:11 by olyen            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#works well with only one function
def ft_count_harvest_recursive(harvest=None, day=1):
	if harvest == None:
		harvest = int(input("Days until harvest: "))

	if day > harvest:
		print("Harvest time!")
		return

	print("Day", day)
	ft_count_harvest_recursive(harvest, day + 1)


#almost work
'''
def	count_days(days, x):
	if x == days + 1:
		return (print("Harvest time"))
	else:
		return (print("Day", x))
		

def ft_count_harvest_recursive():
	days: int = int(input("Days until harvest: "))
	#x: int = 0
	for x in range(1, days):
		count_days(days + 1, x)
		x += 1
	if count_days(days, x) == "Harvest time":
		return
'''
	
'''
def	main():
	ft_count_harvest_recursive()


if __name__ == "__main__":
	main()
'''