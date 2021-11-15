from app_store_scraper import AppStore
from pprint import pprint

spotify = AppStore(country="us", app_name="spotify")
spotify.review(how_many=3000)

listReviews = []
for review in spotify.reviews:
    if review['rating'] > 1 and review['date'].year > 2019:
        lowerString = review['review'].lower()
        if 'tab' in lowerString:
            review['word'] = 'tab'
            listReviews.append(review)
        elif 'library' in lowerString:
            review['word'] = 'library'
            listReviews.append(review)


pprint("List Reviews")
pprint(listReviews)
pprint(len(listReviews))
