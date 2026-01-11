class PlayerNotFoundError(Exception):
    pass

class ItemNotFoundError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class InvalidTradeError(Exception):
    pass

class TradeRejectedError(Exception):
    pass