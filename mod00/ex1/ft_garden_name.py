# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_name.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: olyen <olyen@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/18 20:55:12 by olyen             #+#    #+#              #
#    Updated: 2026/10/20 18:12:58 by olyen            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_garden_name():
	name: str
	name = input("Enter garden name:")
	print("Garden: " + name + "\nStatus: Growing well!")


def main():
	ft_garden_name()


if __name__ == "__main__":
	main()