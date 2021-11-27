from src.helpers.errors.not_implemented_yet import NotImplementedYetException
# from sklearn.naive_bayes import GaussianNB

from src.common.contract.entity.learn import LearnContract


class BayesianLearn(LearnContract):
    gaussian_nb = None

    def __init__(self) -> None:
        raise NotImplementedYetException
        self.gaussian_nb = GaussianNB()

    def training(self, x, y):
        raise NotImplementedYetException
        # self.gaussian_nb.fit(x, y)

    def predict(self):
        raise NotImplementedYetException
        # self.gaussian_nb.predict([[0,0,1,2], [2,0,0,0]])
