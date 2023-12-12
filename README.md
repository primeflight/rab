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

## Response

```bash
[
    {
    "MARCA": "PPAJN",
    "PROPRIETARIO": "SKYJET BRASIL SERV.AEREOS SA",
    "OUTROSPROPRIETARIOS": null,
    "SGUF": "RJ",
    "CPFCNPJ": "86.977.642/0001-60",
    "NMOPERADOR": null,
    "OUTROSOPERADORES": null,
    "UFOPERADOR": null,
    "CPFCGC": null,
    "NRCERTMATRICULA": "00000000",
    "NRSERIE": "48258",
    "CDCATEGORIA": " ",
    "CDTIPO": "DC10",
    "DSMODELO": null,
    "NMFABRICANTE": null,
    "CDCLS": null,
    "NRPMD": "000000",
    "CDTIPOICAO": null,
    "NRTRIPULACAOMIN": "00",
    "NRPASSAGEIROSMAX": "000",
    "NRASSENTOS": "000",
    "NRANOFABRICACAO": null,
    "DTVALIDADECVA": null,
    "DTVALIDADECA": "300999",
    "DTCANC": "2010-01-28 00:00:00.000",
    "DSMOTIVOCANC": "Nº MATRICULA SEM PADRAO",
    "CDINTERDICAO": "M4",
    "CDMARCANAC1": null,
    "CDMARCANAC2": null,
    "CDMARCANAC3": null,
    "CDMARCAESTRANGEIRA": null,
    "DSGRAVAME": "RESERVADAS AS MARCAS",
    "DT_MATRICULA": ""
  },
  ...
]
```