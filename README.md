# morning-algorithms

# TODO add formatter & think about packaging

## Running solutions

Run from the repo root via the Makefile (puts the root on `PYTHONPATH` so
`from helpers... ` imports work):

```sh
make run FILE=patterns/fast-slow-pointers/palindrome-linked-list/solution.py
```

Then inside any solution just import the helpers directly:

```python
from helpers.linked_list import build, to_list
```

## Review list
grep -r "\- \[ \]" patterns/
