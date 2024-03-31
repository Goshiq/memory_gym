class DB:
    """
    Это эмулятор БД.
    Данные хранятся упорядоченно по количеству очков в кортеже (points, name).
    """
    def __init__(self):
        self.data = []

    def get_top_five(self):
        return self.data[:5]

    def write_result(self, points, name):
        place = len([v for v in self.data if v[0] >= points])
        self.data.insert(place, (points, name))

        return place, name
