
from property import QtWidgets,sys

from Builder.BGui import BGui
from Singletone.Singletone import Singletone
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        Singletone.BuildSupporter(self)
        Singletone.Signals(self)
        
        ## 메인 탭 생성
        BGui.Windows(self)
        BGui.GuiCenter(self)
        BGui.GuiLeftTab(self)
        BGui.GuiMenuBar(self)
        BGui.GuiToolBar(self)
        ##
        
if __name__ == '__main__':
    app =  QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
    
