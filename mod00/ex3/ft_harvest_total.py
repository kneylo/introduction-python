# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: olyen <olyen@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/20 01:04:44 by olyen             #+#    #+#              #
#    Updated: 2026/10/20 03:16:20 by olyen            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_harvest_total():
	day1: int =	int(input("Day 1 harvest:"))
	day2: int = int(input("Day 2 harvest:"))
	day3: int = int(input("Day 3 harvest:"))
	print("Total harvest:", (day1 + day2 + day3))


def main():
	ft_harvest_total()


if __name__ == "__main__":
	main() 
