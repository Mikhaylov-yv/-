import pandas as pd

class Get_data:
    def __init__(self):
        self.df = pd.read_csv('../data/Gen_data.csv', index_col = 0)
        self.i = 0
    def get_data(self):
        self.i += 1
        if self.i >= self.df.shape[0]: self.i = 0
        return self.df.loc[self.df.index[self.i], 'Уровень']


class Resolution:
    def __init__(self):
        self.histori_list = []
        self.delta = 0
    def get_rez(self, ur):
        self.histori_list.append(ur)
        if len(self.histori_list) > 2:
            if self.histori_list[-1] < self.histori_list[-2]:
                self.delta = self.histori_list[-1] - self.histori_list[-2]
                return True
        return False





if __name__ == "__main__":
    d = Get_data()
    s = Resolution()
    while True:
        ur = d.get_data()
        print(ur, s.get_rez(ur))