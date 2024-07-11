# React Refresher

## Learning Goals

- React Components

- Props

- State management

- useEffect

- Fetch requests

- Server requests

## Getting Started

Begin with `pipenv install` and `pipenv shell`. From there, `cd server`.

You will need to initialize the database. Use `flask db init` followed by `flask db migrate` and `flask db upgrade`. You should also run the seed file with `python seed.py`. It's suggested that you look at the seed file so you understand how it works.

To start your flask application run `python app.py`.

In a seperate terminal `cd client` followed by `npm install` and `npm run dev`.

When fetching data you'll use this endpoint: `http://localhost:5555`

Finally and very importantly... delete the `db.json`! You won't be needing it now that we have flask.