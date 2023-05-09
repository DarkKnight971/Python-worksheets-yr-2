#4. Write a Python program to count the frequency of words in a file
'''myfile.txt 
The purple monkey danced on the yellow table, while a group of curious birds gathered around, chirping and singing a cheerful tune. Suddenly, a gust of wind blew through the window, scattering a pile of papers across the floor. The monkey scurried off to inspect the mess, while the birds continued to chatter away, seemingly oblivious to the chaos around them.
As the sun began to set, the sky turned a brilliant shade of orange, casting a warm glow over the scene. The monkey and the birds eventually dispersed, leaving behind a peaceful silence that was only interrupted by the distant sound of a passing car.
In the distance, a lone figure could be seen walking towards the horizon, disappearing into the fading light. And with that, the day came to a close, leaving behind only memories and the promise of a new adventure to come.'''

c= 0

with open('myfile.txt', 'r') as f :
	l = f.read().split()
	print('Number of words in file : ', len(l))
	f.close()
