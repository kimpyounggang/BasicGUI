


class Singletone():
    def __init__(self):
        # self.Ppointer = Ppointer
        pass
    
    def BuildSupporter(self):
        Singletone.widget_kinds = {"btn" : "QPushButton", "lineedit" : "QLineEdit",
                                    "listWd" : "QListWidget","label" : "QLabel", "action" : "QAction"}
        Singletone.rule_icon = {"undertext":"ToolButtonTextUnderIcon"}
        Singletone.toolbarareas = {"top":"TopToolBarArea","right":"RightToolBarArea","bottom":"BottomToolBarArea","left":"LeftToolBarArea"}
        
    def Signals(self):
        Singletone.tab_index = 0
        
    def Parameters(self):
        pass
        
        