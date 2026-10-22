# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: olyen <olyen@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/20 21:54:10 by olyen             #+#    #+#              #
#    Updated: 2026/10/20 22:13:25 by olyen            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_count_harvest_iterative():
	days: int = int(input("Days until harvest: "))
	for i in range(1, days + 1):
		print("Day", i)
	print("Harvest time!")


'''
def main():
	ft_count_harvest_iterative()


if __name__ == "__main__":
	main()
'''