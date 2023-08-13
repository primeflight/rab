# rab

Wrapper Python [Registro Aeronáutico Brasileiro (RAB)](https://www.gov.br/anac/pt-br/sistemas/rab)

# Commands Make

```bash
make install-dev
make format
make lint
make test
make coverage
```


# Example

## Search aircraft

```python
from rab.aircraft import Search

search = Search()
aircraft = search.aircraft("PPAJN")

print(aircraft)
```

## Get data RAB

```python
from rab.aircraft import Search

data = Search().get_data()

print(data)
```