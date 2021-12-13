
# Question 1 : Book, Business, Education, Entertainment, Finance, Food&Drink

# Question 2 : Social Networking
SELECT prime_genre, rating_count_tot FROM example.apple
GROUP BY prime_genre Order by count(rating_count_tot) desc;
#Social Networking	2974676

#Question 3 :  Games  = 169
SELECT count(track_name), prime_genre FROM example.apple
GROUP BY prime_genre
ORDER BY count(track_name) desc;

#Question 4: Medical = 1
SELECT count(track_name), prime_genre FROM example.apple
GROUP BY prime_genre
ORDER BY count(track_name) asc;
------------------
#Question 5:
SELECT track_name, rating_count_tot FROM example.apple
GROUP BY prime_genre
ORDER BY rating_count_tot desc;

#Facebook	2974676
#Pandora - Music & Radio	1126879
#Bible	985920
#eBay: Best App to Buy, Sell, Save! Online Shopping	262241
#WeatherBug - Local Weather, Radar, Maps, Alerts	188583
#Evernote - stay organized	161065

# Question 6:
SELECT track_name, user_rating FROM example.apple
GROUP BY prime_genre
ORDER BY user_rating desc;

#Bible	4.5
#PCalc - The Best Calculator	4.5
#Mileage Log | Fahrtenbuch	4.5
#Juxtaposer	4.5
#Star Walk - Find Stars And Planets in Sky Above	4.5
	
	
# Question 7

# Question 8

#Question 9 Bible, Ebay, Evernote, OpenTable are apps that are ther bests rated and most rated by users

# Question 10: Bible, Evernote and Open Table

	
# Question 11:	
	

USE COMMON 