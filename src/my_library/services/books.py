import requests
import time


def get_book_covers(book_title: str, author_name: str) -> list[str]:
    """
    Present user with a list of covers based on book title and last name of first author
    https://developers.google.com/books/docs/v1/using?hl=de#PerformingSearch

    :param book_title:
    :param author_name: full name of first/main author
    :return: a list of urls for image thumbnails of book covers that match title and author
    """
    name_parts = author_name.split(' ')
    if len(name_parts) < 2:
        return []
    last_name = name_parts[-1]
    title_without_spaces = book_title.replace(' ', '%20')
    query_string = f"{title_without_spaces}+inauthor:{last_name}"
    params = {'q': query_string,
              'langRestrict': 'de',
              'maxResults': '4',
              'printType': 'books'
              }
    query_url = f"https://www.googleapis.com/books/v1/volumes"
    response = requests.get(query_url, params=params)
    data = response.json()
    link_list = [b['selfLink'] for b in data['items']]
    thumbnail_urls = []
    for link in link_list:
        resp = requests.get(link)
        if resp:
            obj = resp.json()
            try:
                thumbnail_urls.append(obj['volumeInfo']['imageLinks']['thumbnail'])
            except Exception as e:
                # not all books may have a cover image
                #print(e)
                pass
        time.sleep(1)
    return thumbnail_urls


#print(get_book_covers("Harry Potter und der Halbblutprinz", "JK Rowling"))