[![make.fun](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318.svg)](https://make.fun/c/the-passport-page-of-a-countr-2-20261121-0318)
[![rank](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/ChristaNavisa/the-passport-page-of-a-countr-2-20261121-0318/rank.svg)](https://make.fun/c/the-passport-page-of-a-countr-2-20261121-0318)
[![reward](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/ChristaNavisa/the-passport-page-of-a-countr-2-20261121-0318/reward.svg)](https://make.fun/c/the-passport-page-of-a-countr-2-20261121-0318)

# The Passport Page of a Country That Isn't There

An entry for the [make.fun bounty](https://make.fun/c/the-passport-page-of-a-countr-2-20261121-0318).
`main.py` (Python 3, standard library only, no network) writes one image to
`/output/entry.png`: an open passport spread for the invented **Republic of
Veskara**, a North Atlantic island nation with its capital at Skardvik.

The spread holds together as one working document:

- **Data page** — photorealistic passport portrait of the holder, Elín Margrét
  Valsdóttir (born 12 JUN 1994, Skardvik), bilingual Veskari/English field
  labels, passport No. VSK123456, issued 14 MAR 2023, expiring 14 MAR 2033,
  and an ICAO 9303 machine-readable strip with verified check digits.
- **Visa pages** — a UK visit visa and eight arrival/departure stamps from
  Iceland, Norway and the Faroe Islands, in one coherent travel history:
  every stamp falls after the passport's issue date and each arrival follows
  its departure.
- **The telling detail** — a purple "TIDE FEE PAID 40 KR — Skardvik Harbour"
  stamp and an endorsement: Outer Isles travel needs a tide permit, and the
  glacier road is open 06:00–18:00, June–September only. In Veskara, the tide
  decides where you can go.

## Run

```sh
python3 main.py   # writes /output/entry.png (1024x720 PNG, 274,279 bytes)
```

The program is deterministic: it decodes the artwork embedded in `main.py`
(base64, integrity-checked with sha256) and writes it unchanged. It needs no
network and no third-party packages.

## License

MIT — see [LICENSE](LICENSE).
