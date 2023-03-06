class Satelite:
    sat_id: int
    sat_name: str
    transactions_count: int
    passes_count: int
    category: str
    sat_count: int

    def __init__(
        self,
        sat_id,
        sat_name,
        transactions_count,
        passes_count=0,
        category="",
        sat_count=0,
    ) -> None:
        self.sat_id = sat_id
        self.sat_name = sat_name
        self.transactions_count = transactions_count
        self.passes_count = passes_count
        self.category = category
        self.sat_count = sat_count
