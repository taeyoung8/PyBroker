from pybroker import Strategy, YFinance, highest

def exec_fn(ctx):
    # Get the highest price over the past 10 days.
    high_10d = ctx.indicator('high_10d')
    # Buy if there's a new 10-day high.
    if not ctx.long_pos() and high_10d[-1] > high_10d[-2]:
        ctx.buy_shares = 100
        # Hold the position for 5 days.
        ctx.hold_bars = 5
        # Set a 2% stop loss.
        ctx.stop_loss_pct = 2

strategy = Strategy(YFinance(), start_date='1/1/2022', end_date='7/1/2022')
strategy.add_execution(
    exec_fn, ['AAPL', 'MSFT'], indicators=highest('high_10d', 'close', period=10))
# Run the backtest after a 20-day warm-up period.
result = strategy.backtest(warmup=20)

print(result)
