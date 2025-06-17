# My library

This is an application to create summaries of the books you have read
The books are objects of form

```json
{
  "book_id": "kjk87",
  "name": "Dune",
  "year": 1970,  
  "author_list": ["Frank Herbert"],
  "is_nonfiction": false,
  "genre": "Science-Fiction",
  "labels": [],
  "image_url": "",
  "rating": 4,
  "abstract": "Short summary",
  "summary": "longer summary"
}
```

The backend is a FastAPI server written in python while the HTML contains HTMX (server-side rendering).

Dependencies are managed by Poetry. To install all dependencies just type

```shell
poetry install
```

If you want to enhance the code and need another dependency use

```shell
poetry add <new_module>
```

## Run the application

```shell
cd src/my_library
fastapi dev main.py
#or 
poetry run fastapi dev main.py
```

The FastAPI CLI uses Uvicorn (an ASGI web server) internally to run the application.

By default the application opens on port 8000. For production you might use `fastapi run`. This listens on IP `0.0.0.0`, 
which is fine when it runs inside a container. You can use a HTTPS proxy (with which the users then communicate) like nginx or caddy
before the FastAPI app (see the FastAPI [docs](https://fastapi.tiangolo.com/deployment/https/#lets-encrypt)).


https://systemweakness.com/learning-the-basics-of-authentication-with-go-and-htmx-836ae455cec2

https://www.googleapis.com/books/v1/volumes?q=dune+inauthor:herbert
"http://books.google.com/books/content?id=_ojXNuzgHRcC&printsec=frontcover&img=1&zoom=1&edge=curl&imgtk=AFLRE73ETPhL4LzhiYpZNe1pgNFYBs8eQi7-LceexLPQLgAM1fjCVXK1p0QsTksh7HbGQHs2PbbvM41wlk07U25ZUfVNrgAm7YBMg073yYeqpNmj7uSaYnwtfQot3GHtbhnqd1VUMbQd&source=gbs_api"

