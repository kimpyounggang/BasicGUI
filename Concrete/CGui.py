

from property import QtWidgets,QtGui,QtCharts,QtCore
from property import os

from Singletone.Singletone import Singletone


class CGui():
    def __init__(self,Ppointer):
        self.Ppointer = Ppointer

    def GuiChart(self):
        # 데이터 생성
        set0 = QtCharts.QBarSet("Jane")
        set1 = QtCharts.QBarSet("John")
        set2 = QtCharts.QBarSet("Axel")

        set0 << 1 << 2 << 3 << 4
        set1 << 5 << 0 << 0 << 4
        set2 << 3 << 5 << 8 << 13

        # 막대 시리즈 생성
        series = QtCharts.QBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)

        # 차트 생성
        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle("Simple Bar Chart")

        # 축 생성 및 설정
        categories = ["2008", "2009", "2010", "2011"]
        axis = QtCharts.QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        # 차트 뷰 생성
        chart_view = QtCharts.QChartView(chart)
        return chart_view
        
    def GuiMainTab(self):
        self.MainLeftTab   = QtWidgets.QTabWidget()
        
    def GuiLeftWon():
        groupbox = QtWidgets.QGroupBox()
        vbox = QtWidgets.QVBoxLayout()
        vbox_h_r = QtWidgets.QVBoxLayout()
        vbox_h = QtWidgets.QHBoxLayout()
        add_robot_btn = QtWidgets.QPushButton('+Add Robot')
        # add_robot_btn.clicked.connect(lambda: CTabControl.RCreate_1_Select_Picture(self,Ppointer))
        button_group = QtWidgets.QButtonGroup()
        # button_group.buttonToggled.connect(lambda val: CTabControl._BtnGroupSelectRobot(Ppointer,val))
        vbox_h.addWidget(add_robot_btn)
        vbox.addLayout(vbox_h_r)
        vbox.addLayout(vbox_h)
        groupbox.setLayout(vbox)
        vbox.addStretch()
        return groupbox
        
    def GuiLeftBtc():
        groupbox = QtWidgets.QGroupBox()
        vbox = QtWidgets.QVBoxLayout()
        vbox_h_r = QtWidgets.QVBoxLayout()
        vbox_h = QtWidgets.QHBoxLayout()
        add_robot_btn = QtWidgets.QPushButton('+Add Robot')
        # add_robot_btn.clicked.connect(lambda: CTabControl.RCreate_1_Select_Picture(self,Ppointer))
        button_group = QtWidgets.QButtonGroup()
        # button_group.buttonToggled.connect(lambda val: CTabControl._BtnGroupSelectRobot(Ppointer,val))
        vbox_h.addWidget(add_robot_btn)
        vbox.addLayout(vbox_h_r)
        vbox.addLayout(vbox_h)
        groupbox.setLayout(vbox)
        vbox.addStretch()
        return groupbox
        
    def GuiLeftUsdt():
        groupbox = QtWidgets.QGroupBox()
        vbox = QtWidgets.QVBoxLayout()
        vbox_h_r = QtWidgets.QVBoxLayout()
        vbox_h = QtWidgets.QHBoxLayout()
        add_robot_btn = QtWidgets.QPushButton('+Add Robot')
        # add_robot_btn.clicked.connect(lambda: CTabControl.RCreate_1_Select_Picture(self,Ppointer))
        button_group = QtWidgets.QButtonGroup()
        # button_group.buttonToggled.connect(lambda val: CTabControl._BtnGroupSelectRobot(Ppointer,val))
        vbox_h.addWidget(add_robot_btn)
        vbox.addLayout(vbox_h_r)
        vbox.addLayout(vbox_h)
        groupbox.setLayout(vbox)
        vbox.addStretch()
        return groupbox
    
    def GuiLeftMine():
        groupbox = QtWidgets.QGroupBox()
        vbox = QtWidgets.QVBoxLayout()
        vbox_h_r = QtWidgets.QVBoxLayout()
        vbox_h = QtWidgets.QHBoxLayout()
        add_robot_btn = QtWidgets.QPushButton('+Add Robot')
        # add_robot_btn.clicked.connect(lambda: CTabControl.RCreate_1_Select_Picture(self,Ppointer))
        button_group = QtWidgets.QButtonGroup()
        # button_group.buttonToggled.connect(lambda val: CTabControl._BtnGroupSelectRobot(Ppointer,val))
        vbox_h.addWidget(add_robot_btn)
        vbox.addLayout(vbox_h_r)
        vbox.addLayout(vbox_h)
        groupbox.setLayout(vbox)
        vbox.addStretch()
        return groupbox
    
    
    def Tools(self,BToolBar,*args,**kwargs):
        
        if 'visible' in kwargs: visible = kwargs['visible']
        else: visible = False
        if 'toolbarname' in kwargs: toolbarname = kwargs['toolbarname']
        if 'area' in kwargs: area = kwargs['area']
        setattr(self,toolbarname, QtWidgets.QToolBar(toolbarname))
        if 'rule' in kwargs:
            rule = kwargs['rule']
            getattr(self,toolbarname).setToolButtonStyle(getattr(getattr(QtCore,'Qt'),Singletone.rule_icon[rule]))
        if len(args)>1:
            for btn_name in args:
                def check_file_exists(file_path):
                    if os.path.exists(file_path):
                        return True
                    else:
                        return False
                if check_file_exists(f"DATA/icon/{btn_name}.png"): path = f"DATA/icon/{btn_name}.png"
                else: path = f"Viewer/DATA/icon/{btn_name}.png"
                setattr(self,btn_name,QtWidgets.QAction(QtGui.QIcon(path), btn_name))
                getattr(self,toolbarname).addSeparator()
                getattr(getattr(self, toolbarname),'addAction')(getattr(self,btn_name))
                getattr(self,btn_name).triggered.connect(getattr(BToolBar,f'{btn_name}_def'))
        else:
            if len(args)>0:
                getattr(self,toolbarname).addWidget(args[0])
                getattr(self,toolbarname).setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
                    
        if 'left' in area:
            getattr(getattr(self,toolbarname),'setMaximumWidth')(280)
        getattr(self,'addToolBar')( getattr(getattr(QtCore,'Qt'),Singletone.toolbarareas[area]), getattr(self,toolbarname))
        getattr(self,toolbarname).setVisible(visible)

    def Menu_Bar(self,BBar,Pmenu,dict,*args,**kwargs):
        name = kwargs['name']
        name = name.replace(' ','')
        if 'difname' in kwargs: 
            difname = kwargs['difname']
            defname = difname
        else: 
            defname = name
        if 'kinds' in kwargs: 
            kinds = kwargs['kinds']
            if kinds=='action':
                addwidget = 'addAction'
                if name == '파일':name = '     파일'
                setattr(self, defname, getattr(Pmenu,'addMenu')(name))
                getattr(self,defname).addSeparator() 
            else:
                addwidget = 'addWidget'
        for i in args:
                setattr(self,f'{defname}_{i}', getattr(QtWidgets,dict[kinds])(i))
                getattr(getattr(self, defname),addwidget)(getattr(self,f'{defname}_{i}'))
                if kinds=='action':
                    getattr(self,f'{defname}_{i}').triggered.connect(getattr(BBar,f'{defname}_{i}_def'))
                    
        
        
        
class MyTabWidget(QtWidgets.QTabWidget):
    def __init__(self):
        super().__init__()
        self.currentChanged.connect(self.TabChanged)

    def TabChanged(self, index):
        Singletone.tab_index = index
            