# Silver Trend & Volatility Strategy

Research and backtesting project focused on systematic strategies for the silver market using Python and QuantConnect.

## Project overview

This project investigates whether a trend-following strategy with volatility-based risk management can improve the risk-adjusted performance of a passive investment in SLV.

SLV is used as the initial instrument to obtain exposure to the silver market without introducing the additional complexity of futures contracts, expiration dates and contract rollovers.

## Research question

Can a trend-following strategy with volatility control reduce drawdowns and improve risk-adjusted performance compared with buying and holding SLV?

## Initial scope

- Asset: SLV
- Data frequency: Daily
- Positions: Long or cash
- Leverage: None
- Short selling: Disabled
- Benchmark: Buy and hold SLV
- Platform: QuantConnect
- Language: Python

## Planned stages

1. Exploratory data analysis
2. Buy-and-hold benchmark
3. Trend-following strategy
4. Volatility-based position sizing
5. Transaction cost modelling
6. Temporal and walk-forward validation
7. Optional machine learning extension
8. Paper-trading evaluation

## Repository structure

```text
research/    Exploratory analysis and notebooks
algorithms/  QuantConnect algorithms
reports/     Figures, results and conclusions
