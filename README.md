# hedge-fund-analysis

multilinear regression analysis of hedge fund returns against systematic risk factors. built with pandas, statsmodels, and matplotlib.

## what it does

- fits a multilinear OLS regression model of hedge fund returns against 18 risk factors
- selects significant factors using p-value thresholds and compares full vs reduced model performance
- evaluates model assumptions via residual plot, q-q plot, and breusch-pagan heteroskedasticity test
- compares hedge fund performance against a passive factor portfolio using sharpe ratio, annualised volatility, and maximum drawdown
- assesses beta stationarity using rolling regressions and augmented dickey-fuller tests

## report

written analysis is in `report/`. you may read its .md source or the compiled pdf :)

## structure

```
├── src/
│   ├── main.py          # entry point — runs full analysis pipeline
│   ├── config.py        # data paths, column names, factor list
│   ├── loader.py        # data loading and cleaning
│   ├── model.py         # OLS factor model
│   ├── evaluation.py    # residual plot, q-q plot, heteroskedasticity test
│   ├── risk.py          # sharpe ratio, volatility, drawdown
│   └── stationarity.py  # rolling betas, ADF tests
├── data/
│   └── data.xlsx
├── plots/               # output plots saved here
└── report/
    └── report.md
    └── report.pdf
```

## setup

```bash
git clone https://github.com/iamzainrizwan/hedge-fund-analysis
cd hedge-fund-analysis
uv sync
```

## run

```bash
uv run src/main.py
```

plots are saved to `plots/`.

## ai usage

ai tools were used only as a debugging aid and for clarifying library and statistical concept usage. no full solutions or analytical conclusions were sourced from ai. the final codebase and written analysis were implemented, reviewed, and tested independently.
