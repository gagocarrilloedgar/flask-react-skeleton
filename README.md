# Minimal flask-react-skeleton

This is a minimal unoppinionated skeleton that uses Flask with Pyhton and React with Vite, SWC & JS.

## Technologies

- [Flask]()
- [React]()
- [Vite]()
- [Flask SQL alchemy]()
- [Docker & Docker compose]()

## Installation

Go to [Pre requisites](#pre-requisites) and make sure you have everything


```sh
#Clone the repo
git clone https://github.com/gagocarrilloedgar/flask-react-skeleton
```

Go to the project directory

```bash
  cd flask-react-skeleton
```

## Run locally

### Frontend

Go to the front-end folder
```bash
  cd frontend
```

Install dependencies
```bash
  npm install
```

Start the server
```bash
  npm run dev
```

### Backend
Go to the backend folder

```bash
  cd Backend
```

1. Install the python packages: `$ pipenv install`
2. Create an .env file based on the .env.example: `$ cp .env.example .env` (the ones provided should be enough, you don't need to modify anything).
3. Start the environment: `$ pipenv shell`
4. Launch docker: `$pipenv run launch_docker`
5. DB already initiated
   1. Migrate the migrations: `$ pipenv run migrate` (skip if you have not made changes to the models on the `./src/api/models.py`)
   2. Run the migrations: `$ pipenv run upgrade`
   3. Run the application: `$ pipenv run start`
6. DB not started
   1. Init the db: `$ pipenv run init`
   2. Go to step 5

Once you are done you can stop the docker container using:

```sh
docker compose down
```


## Pre-requisites

#### Docker & Docker compose

In order to be able to start using this tempalte you need to docker installed.

We will use **docker** and **docker compons**e in order to be able to have a local instance of a db (the one provided is a postgreSQL config).

Here you have the links to the oficial documentation:

- [Docker on mac](https://docs.docker.com/desktop/install/mac-install/)
- [Docker on windos](https://docs.docker.com/desktop/install/windows-install/)
- [Docker on linux](https://docs.docker.com/desktop/install/linux-install/)
- [Docker compose](https://docs.docker.com/compose/install/), this should be included with docker desktop.

### Python & pipenv

You need to have at least _python 3.8_ and pipenv installed.

To install ptyhon follow:

- [Mac](https://docs.python-guide.org/starting/install3/osx/)
- [Windows](https://www.python.org/downloads/)

Then install pipenv:

- [Windows](https://www.pythontutorial.net/python-basics/install-pipenv-windows/)

**Mac:**

```sh
python3 -m pip install pip --upgrade
python3 -m pip install pipenv
## Verify using
pipenv
```

### Node

- [Node website](https://nodejs.org/en/download)

## License
[MIT](https://choosealicense.com/licenses/mit/)


## Authors

- [@gagocarrilloedgar](https://www.github.com/gagocarrilloedgar)


