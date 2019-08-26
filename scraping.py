import requests
import pyfiglet
from bs4 import BeautifulSoup
import random 
from time import sleep

def scraping():
	baseURL="http://quotes.toscrape.com"
	url="/page/1"
	quotesDB = {}
# helper function for scrapping the given baseURL
	def scrapper(baseURL):
		print(f"Now Scrapping {baseURL}")
		soup = BeautifulSoup(requests.get(baseURL).text, "html.parser")
		quotes = soup.find_all("div", class_="quote")
		next_btn = soup.find("nav")
		next_btn = next_btn.find("li", class_="next")
		return quotes,next_btn

# helper function for retriveing the bio of the author, used for the hint functionality 
	def hintRetriver(quotesDB,quote):
		bio = quotesDB[quote][1]
		# print(bio)
		soup = BeautifulSoup(requests.get(baseURL+bio).text, "html.parser")
		authDetails = soup.find(class_="author-details")
		authInfo = soup.find_all("p")
		hint = authInfo[1].find(class_="author-born-date").get_text() + ". " + authInfo[1].find(class_="author-born-location").get_text()
		authName = authDetails.find(class_="author-title").get_text()
		firstLetterHint = authName[0]
		lastnameLength = len(authName.split(" ")[1])
		# print(f"hint1: {hint}\nFirst Letter: {firstLetterHint}\nLastname length: {lastnameLength}")
		return [lastnameLength,firstLetterHint,hint]

	quotes,next_btn = scrapper(baseURL)
	print(next_btn.find('a')['href'])

# populate DB
	while url:
		url = baseURL+str(next_btn.find('a')['href']) if next_btn else None
		quotes,next_btn = scrapper(url)
		for quote in quotes:
			qtext = quote.find(class_='text').get_text()
			qAuthor = quote.find(class_="author").get_text()
			authorHref = quote.find("a")['href']
			quotesDB[qtext] = [qAuthor,authorHref]
		#test print 
			print(f"Quote: {qtext}\nAuthor: {qAuthor}\nAuthor bio: {authorHref}")
			print("==============")
		url = next_btn.find("a")["href"] if next_btn else None
		sleep(1)

#commented code was test code
	# bio=quotesDB["“I have never let my schooling interfere with my education.”"][1]
	# print(bio)
	# soup = BeautifulSoup(requests.get(baseURL+bio).text, "html.parser")
	# authDetails = soup.find(class_="author-details")
	# authInfo = soup.find_all("p")
	# hint = authInfo[1].find(class_="author-born-date").get_text() + ", " + authInfo[1].find(class_="author-born-location").get_text()
	# print(hint)


	def game():
		print(pyfiglet.figlet_format(" THE GUESSING GAME "))
		#initilize variables, 7 attempts, pick random quote from our dict, and retreive the relvant hints
		attempts = 7
		randomQuote = random.choice(list(quotesDB.keys()))
		hints = hintRetriver(quotesDB,randomQuote)
		answer = quotesDB[randomQuote][0].upper()
		firstname,lastname = answer.split(" ")[0],answer.split(" ")[1]
	#test print for validation
		print(firstname,lastname,answer)

		print("You got 7 attempts to try and guess the Quote Author!")
		print(" ===== Picking out a random QUOTE!! HOW EXCITING ======")
	#display picked quote
		print(f"{randomQuote}") #- {quotesDB[randomQuote][0]}
		
		while attempts > 0:
			usr_input=input("Provide a guess! enter HINT for help, can be used up to 3 times: ")
			if usr_input.upper() == "HINT":
				if len(hints)<=0:
					print("You are out of hints!")
					continue
				print(hints.pop())
				continue
			if ((usr_input.upper() == firstname) or (usr_input.upper() == lastname) or (usr_input.upper() == answer)):
				print("You got that right!!")
				print(pyfiglet.figlet_format(" !!! CONGRATZ !!! "))
				break
			else:
				attempts-=1
				if attempts == 0:
					print("Sorry you ran out of guesses...")
					print(f"The answer was {answer}")
					break
				print(f"wrong answer habebi, number of attempts left : {attempts}")

		playagain = input("Want to play again?")
		if playagain.upper().startswith('Y'):
			game()
		else:
			print(pyfiglet.figlet_format("Goodbye"))

	game()







scraping()