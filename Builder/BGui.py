


from property import QtWidgets,QtGui,QtCharts

from Concrete.CGui import CGui,MyTabWidget
from Singletone.Singletone import Singletone

from .BToolBar import BToolBar
from .BBar import BBar

class BGui():
    def __init__(self,Ppointer):
        self.Ppointer = Ppointer

    def Windows(self):
        self.setAcceptDrops(True)
        self.setWindowTitle("     Trader")
        self.resize(1500,1500)
        self.menuBar().setNativeMenuBar(False)
        
    def GuiCenter(self):
        self.Center = MyTabWidget()
        
        self.layout1 = QtWidgets.QVBoxLayout()
        self.layout2 = QtWidgets.QVBoxLayout()
        
        self.Tab_1 = QtWidgets.QWidget()
        self.Tab_2 = QtWidgets.QWidget()
        
        self.Tab_1.setLayout(self.layout1)
        self.Tab_2.setLayout(self.layout2)
        
        chart_view = CGui.GuiChart(self)
        self.layout1.addWidget(chart_view)
        
        self.layout2.addWidget(chart_view)
        
        self.Center.addTab(self.Tab_1,'KRW')
        self.Center.addTab(self.Tab_2,'USDT')
        self.setCentralWidget(self.Center)
        # Tab1 in
        
    
    def GuiLeftTab(self):
        self.MainLeftTab = QtWidgets.QTabWidget()
        self.MainLeftTab.addTab(CGui.GuiLeftWon(),'원화')
        self.MainLeftTab.addTab(CGui.GuiLeftBtc(),'BTC')
        self.MainLeftTab.addTab(CGui.GuiLeftUsdt(),'USDT')
        self.MainLeftTab.addTab(CGui.GuiLeftMine(),'보유')
        CGui.Tools(self,BToolBar,self.MainLeftTab,toolbarname='tabs',area='left',visible=True)
    
    def GuiMenuBar(self):
        CGui.Menu_Bar(self,BBar,self.menuBar(),Singletone.widget_kinds,
                     'Open','Save','Quit',kinds='action',name='파일',difname='file')

        # CGui.Menu_Bar(self,BBar,self.menuBar(),Singletone.widget_kinds,
        #                                   'ToolTip',kinds='action',name='mm')

    def GuiToolBar(self):
        CGui.Tools(self,BToolBar,'test','test1','test2',
                        toolbarname='MenuProc',rule='undertext',area='top',visible=True)
    