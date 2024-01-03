
class StockSpanner:
    def __init__(self):
        self.prices = []
        self.spans = []

    def next(self, price: int) -> int:
        span = 1
        while self.prices and price >= self.prices[-1]:
            span += self.spans.pop()
            self.prices.pop()
        self.prices.append(price)
        self.spans.append(span)
        return span

