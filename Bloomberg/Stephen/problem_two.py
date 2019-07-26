class StockMachine:
    def __init__(self):
        self.stocks = collections.defaultdict(int)

    def stock_sold(self, ticker, volume):
        self.stocks[ticker] += volume

    def top_k_volume(self, k):
        stocks = [(ticker, volume) for ticker, volume in self.stocks.items()]

        return self.quick_select(stocks, k)

    def quick_select(self, stocks, k):

        pivot_index = math.randint(len(stocks))

        selected_index = self.partition(pivot_index)

    def partition(self, stocks, pivot_index):
