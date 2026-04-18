# Python Folder

This folder now supports two kinds of Python work:

1. `app.py` for the FastAPI service
2. `dsa/` for normal Python practice scripts

## Run FastAPI

```bash
docker compose up python
```

Or locally:

```bash
cd python
pip install -r requirements.txt
python app.py
```

## Run DSA Scripts

From the repo root:

```bash
python3 python/dsa/prime_number.py
python3 python/dsa/list_stack.py
python3 python/dsa/list_queue.py
python3 python/dsa/singly_linked_list.py
python3 python/run_dsa.py
```

From inside the container:

```bash
docker compose exec python python dsa/prime_number.py
docker compose exec python python dsa/list_stack.py
docker compose exec python python dsa/list_queue.py
docker compose exec python python dsa/singly_linked_list.py
```

## Starter Topics Added

- Prime number check and prime list
- Stack using Python list
- Queue using Python list
- Singly linked list
