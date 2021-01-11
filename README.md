# django-news-portal

## Structure:

- `<host>/` - Home page
- `<host>/news` - Page list with new the news
- `<host>/news/<number>` - Page with details news, number is article id. Each news page has a unique link.

News store in json file. JSON file contain an array of objects with the obligatory fields created, text, title, and link

        [{
            "created": "2020-02-22 16:40:00",
            "text": "A new star appeared in the sky.",
            "title": "A star is born",
            "link": 9234732
        },...]

The created field should contain a date in the format `%Y-%m-%d %H:%M:%S`.