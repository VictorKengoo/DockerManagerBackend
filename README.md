# Docker Manager - Backend

## How to install

Download and install python 3.6+ and pip. If you wanta more isolate environment, you can install `virtualenv` and install the dependencies on a virtual environment. For that you need to:

Add pip command into your machine:

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

```
python get-pip.py
```

Install:
```
pip install virtualenv
```

Create a virtual env:
```
virtualenv -p python venv
```

Start virtualenv:
```
venv/Scripts/activate.bat
```

Then on the root of the project run:

Linux:

```
pip3 install -r requirements.txt
```
Windows:
```
pip install -r requirements.txt
```

Or simply install python and install its dependencies.

## Running

Execute on your terminal:

```
uvicorn app:app --port 8000 --reload
```
