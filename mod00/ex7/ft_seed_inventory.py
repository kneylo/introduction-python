# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: olyen <olyen@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/21 10:59:57 by olyen             #+#    #+#              #
#    Updated: 2026/10/21 20:27:11 by olyen            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def	ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	if unit == "packets":
		print(seed_type.title(), "seeds: ", quantity, "packets available")
	elif unit == "grams":
		print(seed_type.title(), "seeds: ", quantity, "grams total")
	elif unit == "area":
		print(seed_type.title(), "seeds: ", quantity, "square meters")
	else:
		print("Unknown unit type")
	return


def main():
	ft_seed_inventory(sys.argv[1], int(sys.argv[2]), sys.argv[3])


if __name__ == "__main__":
		main()