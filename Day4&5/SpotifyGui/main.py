from SpotifyView import SpotifyMainView
from PyQt5.QtWidgets import QApplication
import sys
# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = SpotifyMainView()
    # model = evaluateExpression



    # Create instances of the model and the controller

    # PyCalcCtrl(model=model, view=view)

    view.show()
    # Execute the calculator's main loop
    sys.exit(pycalc.exec_())


if __name__ == '__main__':
    main()
