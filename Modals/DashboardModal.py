from PyQt5 import QtSql, QtGui
from PyQt5.QtWidgets import *
import os
import os.path


class DashboardModal:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.base_dir, "TMS.db")

    def createDB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(self.db_path)

        if not db.open():
            QMessageBox.critical(None, qApp.tr("Cannot open database"),
                                 qApp.tr("Unable to establish a database connection.\n"
                                         "This sofware needs SQLite support. Please read "
                                         "the Qt SQL driver documentation for information "
                                         "how to build it.\n\n" "Click Cancel to exit."),
                                 QMessageBox.Cancel)

            return False

        query = QtSql.QSqlQuery()

        query.exec_("create table sportsmen(id int primary key, "
                    "firstname varchar(20), lastname varchar(20))")

        query.exec_("insert into sportsmen values(101, 'Roger', 'Federer')")
        query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo')")
        query.exec_("insert into sportsmen values(103, 'Ussain', 'Bolt')")
        query.exec_("insert into sportsmen values(104, 'Sachin', 'Tendulkar')")
        query.exec_("insert into sportsmen values(105, 'Saina', 'Nehwal')")
        return True


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    my_instance = DashboardModal()
    my_instance.createDB()
