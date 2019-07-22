# ABSplitter

Proportional distribution of users in unequal A/B testing

## Test

```
$ python test.py
```

## Usage

1. Initialize

```
dist = ABSplitter()
dist.reset(30.0, 70.0)  # a = 30%, b = 70%
```

2. Allocate your user

```
if dist.getNextVersion() == 'VERSION_A':
    user = "VERSION_A"
else:
    user = "VERSION_B"
```

See test.py for a reference implementation
