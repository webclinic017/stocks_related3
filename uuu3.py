import datetime
import backtrader as bt
import pandas as pd
import pickle
import math

"""
You have a number of issues. 
1. Establish cerebro in `macd_stock_test2` 
2. Call the `run_test_macd` from if __name__ == "__main__":
3. Add in print log
4. Add in order and trade notify.
5. Don't pass in the strategy, create it in `macd_stock_test2`.
6. Change name of GoldCross class to python standard.

"""


def run_test_macd():
    # with open("sp500tickers.pickle", "rb") as f:
    #     tickers = pickle.load(f)
    tickers = ["TSLA", "FB"]
    for ticker in tickers:
        macd_stock_test2(ticker)


def macd_stock_test2(ticker):
    # print("stock test")
    # print("ticker")
    cerebro = bt.Cerebro()
    cerebro.addstrategy(GoldCross)

    cerebro.broker.set_cash(1000000)
    # ticker_prices = pd.read_csv(
    #     "stock_dfs/{}.csv".format(ticker), index_col="Date", parse_dates=True
    # )

    # print(ticker_prices)
    # ticker prices
    # feed = bt.feeds.PandasData(dataname=ticker_prices)
    # print(feed)
    # print(ticker)
    feed = bt.feeds.YahooFinanceData(
        dataname=ticker,
        timeframe=bt.TimeFrame.Days,
        fromdate=datetime.datetime(2019, 1, 1),
        todate=datetime.datetime(2020, 12, 31),
        reverse=False,
    )
    cerebro.adddata(feed)

    # cerebro.addsizer(bt.sizers.FixedSize, stake=1000)
    # cerebro.addanalyzer(btanalyzers.DrawDown, _name='drawdown')
    # cerebro.addanalyzer(btanalyzers.DrawDown, _name='returns')

    print("starting portfolio value: %.2f" % cerebro.broker.getvalue())
    cerebro.run()

    print('\n\n',"final portfolio value: %.2f" % cerebro.broker.getvalue())
    # cerebro.addanalyzer(SQN)
    #
    # cerebro.addwriter(bt.WriterFile, csv=args.writercsv, rounding=2)
    # cerebro.plot(style='candle')


class GoldCross(bt.Strategy):

    # set parameters to define fast and slow
    params = (
        ("fast", 40),
        ("slow", 150),
        ("order_percentage", 0.99),
        ("ticker", "stock"),
    )

    # define constractors
    def __init__(self):
        print("position size:", self.position.size)

        self.fast_moving_average = bt.indicators.EMA(
            self.data.close, period=self.params.fast, plotname="40 day moving average"
        )

        self.slow_moving_average = bt.indicators.EMA(
            self.data.close, period=self.params.slow, plotname="150 day moving average"
        )

        self.crossover = bt.indicators.CrossOver(
            self.fast_moving_average, self.slow_moving_average
        )

    def log(self, txt, dt=None):
        """ Logging function fot this strategy"""
        dt = dt or self.data.datetime[0]
        if isinstance(dt, float):
            dt = bt.num2date(dt)
        print("%s, %s" % (dt.date(), txt))

    def notify_order(self, order):
        """ Triggered upon changes to orders. """

        # Suppress notification if it is just a submitted order.
        if order.status == order.Submitted:
            return

        # Print out the date, security name, order number and status.
        dt, dn = self.datetime.date(), order.data._name
        type = "Buy" if order.isbuy() else "Sell"
        self.log(
            f"{order.data._name:<6} Order: {order.ref:3d}\tType: {type:<5}\tStatus"
            f" {order.getstatusname():<8} \t"
            f"Size: {order.created.size:9.4f} Price: {order.created.price:9.4f} "
            f"Position: {self.getposition(order.data).size}"
        )
        if order.status == order.Margin:
            return

        # Check if an order has been completed
        if order.status in [order.Completed]:
            self.log(
                f"{order.data._name:<6} {('BUY' if order.isbuy() else 'SELL'):<5} "
                # f"EXECUTED for: {dn} "
                f"Price: {order.executed.price:6.2f} "
                f"Cost: {order.executed.value:6.2f} "
                f"Comm: {order.executed.comm:4.2f} "
                f"Size: {order.created.size:9.4f} "
            )

    def notify_trade(self, trade):
        """Provides notification of closed trades."""
        if trade.isclosed:
            self.log(
                "{} Closed: PnL Gross {}, Net {},".format(
                    trade.data._name,
                    round(trade.pnl, 2),
                    round(trade.pnlcomm, 1),
                )
            )

    def next(self):
        if self.position.size == 0:
            if self.crossover > 0:
                amount_to_invest = self.params.order_percentage * self.broker.cash
                self.size = math.floor(amount_to_invest / self.data.close)

                self.log(
                    "Buy {} shares of {} at {}".format(
                        self.size,
                        self.params.ticker,
                        self.data.close[0],
                    )
                )
                self.buy(size=self.size)

        if self.position.size > 0:
            if self.crossover < 0:
                self.log(
                    "Sell {} shares of {} at {}".format(
                        self.size, self.params.ticker, self.data.close[0],
                    )
                )
                self.sell(size=self.size)


if __name__ == "__main__":
    run_test_macd()

