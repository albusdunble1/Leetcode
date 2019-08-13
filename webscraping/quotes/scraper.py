from csv import DictReader, writer
import requests
from bs4 import BeautifulSoup
from random import choice
from time import sleep





with open('quotes.csv', 'w', newline='', encoding="utf-8") as file:
    csv_writer = writer(file)
    csv_writer.writerow(['author', 'quote', 'link'])

    url = 'http://quotes.toscrape.com'
    next = '/page/1'

    while next:
        res = requests.get(url+next)
        print(f'Scraping {url+next}...')
        data = BeautifulSoup(res.text, 'html.parser')
        quotes = data.find_all(class_='quote')
        print(f'{len(quotes)} quotes found!')

        for quote in quotes:
            text = quote.find(class_='text').get_text()
            author = quote.find(class_='author').get_text()
            link = quote.find(class_='author').find_next_sibling('a')['href']
            csv_writer.writerow([author, text, link])

        
        next = data.find(class_='pager').find(class_='next')
        if next: next = next.find('a')['href']
        else: next = None
        sleep(2)

with open('quotes.csv', 'r', encoding="utf-8") as file:
    csv_reader = list(DictReader(file))

    while True:
        rand_quote = choice(csv_reader)
        quote_text = rand_quote['quote']
        quote_author = rand_quote['author']
        author_last = quote_author.split()[-1]
        author_link = rand_quote['link']
        tries = 4

        
        print('Here\'s a quote:\n')
        print(quote_text)
        ans = input(f'\nWho said this? Guesses remaining: {tries}. ')
        if ans == quote_author:
            print('You guessed correctly! Congratulations!')
            again = input('Would you like to play again? (y/n)?')
            if again == 'n': break
            else: print('Great! Here we go again...\n')
        else:
            res = requests.get(url+author_link)
            data = BeautifulSoup(res.text, 'html.parser')
            birthdate = data.find(class_='author-born-date').get_text()
            birthplace = data.find(class_='author-born-location').get_text()
            

            while True:
                tries -= 1
                if tries == 3:
                    print(f'Here\'s a hint: The author was born in {birthdate} {birthplace}.\n')
                elif tries == 2:
                    print(f'Here\'s a hint: The author\'s first name starts with {quote_author[0]}\n')
                elif tries == 1:
                    print(f'Here\'s a hint: The author\'s last name starts with {author_last[0]}\n')
                else:
                    print(f'Sorry, you\'ve run out of guesses. The answer was {quote_author}\n')
                    break

                ans = input(f'Who said this? Guesses remaining: {tries}. ')
                if ans == quote_author:
                    print('You guessed correctly! Congratulations!\n')
                    break
                

            again = input('Would you like to play again? (y/n)?')
            if again == 'n': break
            else: print('Great! Here we go again...\n')

                






        


    
    


