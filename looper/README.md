# Looper

In this script, we execute a command in a loop with fixed intervals and fixed try numbers untill we get successful excution result. 

## Setup 

Clone the project 

```bash
    git clone https://github.com/amirkmzh/python-scripts.git
```

Then, set the environment variables: 

```bash 
    export DWS_TESTER_COMMNAD=<command>
    export DWS_TESTER_THRESHOLD=<number of tries to execute the command> 
    export DWS_TESTER_INTERVAL=<time intervals between executing commands>
```

Go to the project directory:

```bash
    cd looper
```

Change the access permissions:
 ```bash
    sudo chmod a+x .
 ```

Run the application: 

```bash
    ./looper.py
```

