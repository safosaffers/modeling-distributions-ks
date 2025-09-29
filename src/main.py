from Model.Model import Model
from View.View import View
from Presenter.Presenter import Presenter
from PySide6.QtWidgets import QApplication
import tempfile
import sys
import ctypes
import os

# Уникальный идентификатор приложения
myappid = 'Company.Product.Version'

# Установка AppUserModelID (только для Windows)
if sys.platform == 'win32':
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except AttributeError:
        pass  # Функция недоступна на старых версиях Windows

# Логика с удалением splash-файла (работает в Nuitka onefile режиме)
if "NUITKA_ONEFILE_PARENT" in os.environ:
    splash_filename = os.path.join(
        tempfile.gettempdir(),
        "onefile_%d_splash_feedback.tmp" % int(
            os.environ["NUITKA_ONEFILE_PARENT"]),
    )
    try:
        if os.path.exists(splash_filename):
            os.unlink(splash_filename)
    except Exception as e:
        print(f"Could not remove splash file: {e}", file=sys.stderr)


def main():
    app = QApplication(sys.argv)

    m = Model()
    v = View()
    p = Presenter(m, v)
    v.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
