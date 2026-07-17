# Project Scope

## Primary objective

Develop and evaluate a reproducible systematic strategy for SLV using trend and volatility information.

## Included in version 1.0

- Daily SLV data
- Exploratory data analysis
- Long-or-cash strategies
- Buy-and-hold benchmark
- Trend-following indicators
- Volatility-based risk management
- Transaction costs
- Temporal validation
- QuantConnect backtests

## Excluded from version 1.0

- Real-money trading
- Intraday trading
- Short selling
- Leverage
- Options
- Silver futures
- Deep learning
- Claims of future price prediction
- Parameter selection using the final test period

## Research question

Can a trend-following strategy with volatility control reduce drawdowns and improve risk-adjusted performance compared with buying and holding SLV?

## Initial hypothesis

A strategy that invests in SLV during positive trends and reduces exposure during periods of high volatility may achieve a lower maximum drawdown and better risk-adjusted performance than a passive buy-and-hold investment.

## Main methodological risk

Overfitting the strategy to historical data.

## Mitigation

- Keep the initial strategy simple
- Use a limited number of parameters
- Separate development, validation and test periods
- Include transaction costs
- Report negative results
- Compare all strategies against buy and hold
