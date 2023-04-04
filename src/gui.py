import wx

class LoggingToolGUI(wx.Frame):
    def __init__(self, parent, title):
        super(LoggingToolGUI, self).__init__(parent, title=title, size=(300, 200))

        self.panel = wx.Panel(self)

        self.log_level_text = wx.StaticText(self.panel, label="Log Level:")
        self.log_level_choices = ['DEBUG', 'INFO', 'WARNING', 'ERROR']
        self.log_level_dropdown = wx.ComboBox(self.panel, choices=self.log_level_choices, style=wx.CB_READONLY)

        self.save_log_text = wx.StaticText(self.panel, label="Save Log to:")
        self.save_log_input = wx.TextCtrl(self.panel, value='logs/logging_tool.log')

        self.save_errors_text = wx.StaticText(self.panel, label="Save Errors to:")
        self.save_errors_input = wx.TextCtrl(self.panel, value='logs/error.log')

        self.activate_button = wx.Button(self.panel, label="Activate")

        self.__set_properties()
        self.__do_layout()
        self.__bind_events()

    def __set_properties(self):
        self.log_level_dropdown.SetSelection(0)

    def __do_layout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        sizer.Add(self.log_level_text, 0, wx.ALL, 5)
        sizer.Add(self.log_level_dropdown, 0, wx.ALL | wx.EXPAND, 5)

        sizer.Add(self.save_log_text, 0, wx.ALL, 5)
        sizer.Add(self.save_log_input, 0, wx.ALL | wx.EXPAND, 5)

        sizer.Add(self.save_errors_text, 0, wx.ALL, 5)
        sizer.Add(self.save_errors_input, 0, wx.ALL | wx.EXPAND, 5)

        sizer.Add(self.activate_button, 0, wx.ALL | wx.EXPAND, 5)

        self.panel.SetSizer(sizer)

    def __bind_events(self):
        self.activate_button.Bind(wx.EVT_BUTTON, self.on_activate_button)

    def on_activate_button(self, event):
        log_level = getattr(logging, self.log_level_dropdown.GetValue())
        logging.basicConfig(level=log_level, filename=self.save_log_input.GetValue())
        logger = logging.getLogger(__name__)
        logger.addHandler(logging.FileHandler(self.save_errors_input.GetValue()))

        # Do the actual work of the tool here
        
        wx.MessageBox('Logging Tool Activated!', 'Info', wx.OK | wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = wx.App()
    frame = LoggingToolGUI(None, 'Logging Tool')
    frame.Show(True)
    app.MainLoop()
