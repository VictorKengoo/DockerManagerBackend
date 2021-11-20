# Docker Manager - Backend

## How to install

Download and install python 3.8+ and pip.

To help you installing pip, use these commands:

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

```
python get-pip.py
```
If you want to create a new self environment, install `virtualenv` and install the dependencies on a virtual environment. For that you need to:
Install `virtualenv`:
```
pip install virtualenv
```

Create a virtual env:
```
virtualenv -p python venv
```

Start virtualenv with this command:
```
venv/Scripts/activate.bat
```

On the root of the project run the pip install on the text file requirements (the requirements.txt will help you to install others libs that will be usefull):

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
