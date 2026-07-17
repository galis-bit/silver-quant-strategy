# SLV Buy-and-Hold Baseline

## Objective

Establish a passive benchmark for evaluating subsequent systematic strategies based on trend and volatility.

## Configuration

- Asset: SLV
- Period: 2010-01-01 to 2025-12-31
- Initial capital: 100,000 USD
- Data resolution: Daily
- Position: 100% long
- Benchmark: SLV
- Total orders: 1

## Results

| Metric | Value |
|---|---:|
| Initial equity | 100,000 USD |
| Final equity | 373,001.72 USD |
| Net profit | 273.00% |
| Annualized return | 8.57% |
| Annualized volatility | 24.20% |
| Sharpe ratio | 0.291 |
| Sortino ratio | 0.319 |
| Maximum drawdown | 76.20% |
| Total fees | 28.94 USD |
| Total orders | 1 |

## Interpretation

The passive investment produced substantial long-term growth, increasing the initial capital from 100,000 USD to approximately 373,002 USD.

However, the strategy experienced a maximum drawdown of 76.2%, indicating a very high level of downside risk. Its annualized volatility was 24.2%, while the Sharpe ratio was only 0.291.

These results support the project's research objective: evaluating whether a trend-following strategy with volatility control can reduce severe drawdowns and improve risk-adjusted performance relative to passive ownership of SLV.

Trade-level statistics are not meaningful for this benchmark because the position remained open at the end of the backtest.
