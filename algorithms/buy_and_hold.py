from AlgorithmImports import *


class SilverBuyAndHoldAlgorithm(QCAlgorithm):
    """Buy-and-hold benchmark for SLV."""

    def initialize(self) -> None:
        # Backtest configuration
        self.set_start_date(2010, 1, 1)
        self.set_end_date(2025, 12, 31)
        self.set_cash(100_000)

        # Subscribe to daily SLV data
        self.silver = self.add_equity(
            "SLV",
            Resolution.DAILY
        ).symbol

        # Compare the portfolio against SLV itself
        self.set_benchmark(self.silver)

    def on_data(self, data: Slice) -> None:
        # Wait until SLV data is available.
        if not data.contains_key(self.silver):
            return

        # Buy once and hold for the rest of the backtest.
        if not self.portfolio.invested:
            self.set_holdings(self.silver, 1.0)
