from Model.Model import Model
from View.View import View
from Presenter.Presenter import Presenter
from PySide6.QtWidgets import QApplication
import sys


def main():
    app = QApplication(sys.argv)

    m = Model()
    v = View()
    p = Presenter(m, v)
    v.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
