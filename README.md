# Installation

#### Clone the repository

`https://github.com/ayushsubedi/empty_flask/`

### Rename

Rename empty_flask (folders and imports) to new project name

### Change remote url 

`git remote set-url origin https://github.com/USERNAME/REPOSITORY.git`


#### CD into the cloned directory and create a virtualenv

`python -m venv env`


### Enable virtualenv

`.\env\Scripts\activate`


### Enable virtualenv (windows)

`.\env\Scripts\activate`

### Install dependency packages from requirements.txt

`pip install -r requirements.txt`

### Run flask app
`source FLASK_APP="app.py"`
`flask run`

### Run flask app (windows)
`$env:FLASK_APP="app.py"`
`flask run`

# Running with docker

```
if __name__ == '__main__':
    application.run(host= '0.0.0.0', debug=True)
```

### Build
```docker build -f Dockerfile -t docker_flask .```

### Run
```docker run -p 5000:5000 -ti docker_flask /bin/bash -c "cd /src && source activate ml && python run.py"```

