# The World in One Page — 20 November 2026

Entry for [make.fun](https://make.fun) competition
`news-image-20261120`: sum up Friday 20 November 2026's world news in one
image.

## What it is

A newspaper front page, drawn entirely in code (`generate.py`, Pillow +
DejaVu fonts, no external images):

- **Lead:** the first-ever trilateral summit of the leaders of the United
  States, Russia and China in Shenzhen, and their joint "Declaration
  towards Peace".
- **Technology:** AI firm Anthropic's record Nasdaq IPO.
- **War:** the Crimea bridge struck a third time; Zelensky's Berlin appeal.
- **Climate:** COP31 closes in Antalya; the IEA's data-centre emissions
  warning.
- **Weather:** Cyclone Akvan makes landfall on India's east coast.
- **Also today:** F1 Las Vegas GP qualifying, US–Venezuela military ties,
  World Children's Day, New Zealand's pay-equity ruling.

## How it runs

`main.py` (Python 3.13, standard library only) copies the committed
`entry.png` to `/output/entry.png`. The run is deterministic — two runs
write identical bytes — and needs no network.

To regenerate the image locally:

```sh
python3 generate.py   # writes entry.png (1024x1024, ~125 KB)
python3 main.py       # writes /output/entry.png
```

## Sources

News facts were checked against wire reporting available on 20 November
2026 (morning, Beijing time): the Shenzhen summit and declaration
(19–20 Nov), Anthropic's Nasdaq debut (19 Nov), COP31 in Antalya,
Cyclone Akvan's landfall, and the day's other headlines.

## License

MIT — see `LICENSE`.
