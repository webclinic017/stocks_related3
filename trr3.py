using AlphaVantage
using DataFrames, StatsPlots, Dates
gr(size=(800,470))
# Get daily S&P 500 data
spy = time_series_daily("SPY", datatype="csv");
# Convert to a DataFrame
data = DataFrame(spy[1]);
# Add column names
data = rename(data, Symbol.(vcat(spy[2]...)));
# Convert timestamp column to Date type
data[!, :timestamp] = Dates.Date.(data[!, :timestamp]);
data[!, :open] = Float64.(data[!, :open])
# Plot the timeseries
plot(data[!, :timestamp], data[!, :open], label=["Open"])
savefig("sp500.png")
