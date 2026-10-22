# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: olyen <olyen@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/20 18:07:49 by olyen             #+#    #+#              #
#    Updated: 2026/10/20 18:20:29 by olyen            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_water_reminder():
	last_watering: int = int(input("Days since last watering:"))
	if last_watering > 2:
		print("Water the plants!")
	else:
		print("Plants are fine")