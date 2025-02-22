#
# www.youtube.com/@mersthub_mentors
#


import yfinance as yf

data = yf.download("TSLA", start="2022-01-01",
                   end="2022-12-31")


if __name__ == "__main__":
    print(data.head())
