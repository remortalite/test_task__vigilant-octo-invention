# Test assignment for FUNBOX

## Description

Task: https://funbox.ru/q/python.pdf

## Install and run

1. First, you should start Redis on 6378 port. You can use docker with makefile recipe like this:

```bash
make run-docker
```

If you need to stop docker redis process, enter `make stop-docker`

2. Run the app using:

```bash
make run
```

Then go to `http://localhost:5000/visited_sites` and have fun (not really, but yeah).