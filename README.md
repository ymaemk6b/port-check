# port-check

A small utility that checks TCP reachability with configurable timeouts.

## Why

I kept rewriting the same thirty lines in every project, so I pulled them out.

## Install

```bash
pip install port-check
```

## Usage

```python
from port_check import portCheck

result = portCheck("example")
print(result)
```

## Notes

- No runtime dependencies outside the standard library.
- Tested on Python 3.9 and newer.

## License

MIT
