# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: olyen <olyen@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/20 03:17:37 by olyen             #+#    #+#              #
#    Updated: 2026/10/20 18:13:03 by olyen            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
	plant_age: int = int(input("Enter plant age in days:"))
	if plant_age > 60:
		print("Plant is ready to harvest!")
	else:
		print("Plant need more time to grow.")