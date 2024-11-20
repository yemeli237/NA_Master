
# # import tkinter
# # import tkinter.messagebox
# # import customtkinter

# # customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# # customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


# # class App(customtkinter.CTk):
# #     def __init__(self):
# #         super().__init__()

# #         # configure window
# #         self.title("NA Master")
# #         self.geometry(f"{1080}x{720}")
# #         self.iconbitmap("icone.ico")

# #         # configure grid layout (4x4)
# #         self.grid_columnconfigure(1, weight=1)
# #         self.grid_columnconfigure((2, 3), weight=0)
# #         self.grid_rowconfigure((0, 1, 2), weight=1)

# #         # create sidebar frame with widgets
# #         self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
# #         self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
# #         self.sidebar_frame.grid_rowconfigure(4, weight=1)
# #         self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
# #         self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
# #         self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
# #         self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
# #         self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
# #         self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
# #         self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
# #         self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
# #         self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
# #         self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
# #         self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
# #                                                                        command=self.change_appearance_mode_event)
# #         self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
# #         self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
# #         self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
# #         self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
# #                                                                command=self.change_scaling_event)
# #         self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

# #         # create main entry and button
# #         self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
# #         self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

# #         self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
# #         self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

# #         # create textbox
# #         self.textbox = customtkinter.CTkTextbox(self, width=250)
# #         self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

# #         # create tabview
# #         self.tabview = customtkinter.CTkTabview(self, width=250)
# #         self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
# #         self.tabview.add("CTkTabview")
# #         self.tabview.add("Tab 2")
# #         self.tabview.add("Tab 3")
# #         self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
# #         self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

# #         self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False,
# #                                                         values=["Value 1", "Value 2", "Value Long Long Long"])
# #         self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
# #         self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("CTkTabview"),
# #                                                     values=["Value 1", "Value 2", "Value Long....."])
# #         self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
# #         self.string_input_button = customtkinter.CTkButton(self.tabview.tab("CTkTabview"), text="Open CTkInputDialog",
# #                                                            command=self.open_input_dialog_event)
# #         self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
# #         self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
# #         self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

# #         # create radiobutton frame
# #         self.radiobutton_frame = customtkinter.CTkFrame(self)
# #         self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
# #         self.radio_var = tkinter.IntVar(value=0)
# #         self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="CTkRadioButton Group:")
# #         self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
# #         self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
# #         self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
# #         self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
# #         self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
# #         self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
# #         self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

# #         # create slider and progressbar frame
# #         self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
# #         self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
# #         self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
# #         self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
# #         self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
# #         self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
# #         self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
# #         self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
# #         self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
# #         self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
# #         self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
# #         self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
# #         self.slider_2 = customtkinter.CTkSlider(self.slider_progressbar_frame, orientation="vertical")
# #         self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
# #         self.progressbar_3 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="vertical")
# #         self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

# #         # create scrollable frame
# #         self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="CTkScrollableFrame")
# #         self.scrollable_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
# #         self.scrollable_frame.grid_columnconfigure(0, weight=1)
# #         self.scrollable_frame_switches = []
# #         for i in range(100):
# #             switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
# #             switch.grid(row=i, column=0, padx=10, pady=(0, 20))
# #             self.scrollable_frame_switches.append(switch)

# #         # create checkbox and switch frame
# #         self.checkbox_slider_frame = customtkinter.CTkFrame(self)
# #         self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
# #         self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
# #         self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
# #         self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
# #         self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
# #         self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
# #         self.checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")

# #         # set default values
# #         self.sidebar_button_3.configure(state="disabled", text="Disabled CTkButton")
# #         self.checkbox_3.configure(state="disabled")
# #         self.checkbox_1.select()
# #         self.scrollable_frame_switches[0].select()
# #         self.scrollable_frame_switches[4].select()
# #         self.radio_button_3.configure(state="disabled")
# #         self.appearance_mode_optionemenu.set("Dark")
# #         self.scaling_optionemenu.set("100%")
# #         self.optionmenu_1.set("CTkOptionmenu")
# #         self.combobox_1.set("CTkComboBox")
# #         self.slider_1.configure(command=self.progressbar_2.set)
# #         self.slider_2.configure(command=self.progressbar_3.set)
# #         self.progressbar_1.configure(mode="indeterminnate")
# #         self.progressbar_1.start()
# #         self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
# #         self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
# #         self.seg_button_1.set("Value 2")

# #     def open_input_dialog_event(self):
# #         dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
# #         print("CTkInputDialog:", dialog.get_input())

# #     def change_appearance_mode_event(self, new_appearance_mode: str):
# #         customtkinter.set_appearance_mode(new_appearance_mode)

# #     def change_scaling_event(self, new_scaling: str):
# #         new_scaling_float = int(new_scaling.replace("%", "")) / 100
# #         customtkinter.set_widget_scaling(new_scaling_float)

# #     def sidebar_button_event(self):
# #         print("sidebar_button click")


# # if __name__ == "__main__":
# #     app = App()
# #     app.mainloop()

# import customtkinter as ctk
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# class ctkApp:
        
#     def __init__(self):
#         ctk.set_appearance_mode("dark")
#         self.root = ctk.CTk()
#         self.root.geometry("1200x400+200x200")
#         self.root.title("Dynamic Scatterplot")
#         self.root.update()
#         self.frame = ctk.CTkFrame(master=self.root,
#                                   height= self.root.winfo_height()*0.95,
#                                   width = self.root.winfo_width()*0.66,
#                                   fg_color="darkblue")
#         self.frame.place(relx=0.33, rely=0.025)
#         self.input =  ctk.CTkEntry(master=self.root,
#                                    placeholder_text=100,
#                                    justify='center',
#                                    width=300,
#                                    height=50,
#                                    fg_color="darkblue")
#         self.input.insert(0,100)
#         self.input.place(relx=0.025,rely=0.5)
#         self.slider = ctk.CTkSlider(master=self.root,
#                                     width=300,
#                                     height=20,
#                                     from_=1,
#                                     to=1000,
#                                     number_of_steps=999,
#                                     command=self.update_surface)
#         self.slider.place(relx= 0.025,rely=0.75) 
#         self.button = ctk.CTkButton(master = self.root,
#                                text="Update Graph",
#                                width=300,
#                                height=50,
#                                command=self.update_window)
#         self.button.place(relx=0.025,rely=0.25)
#         self.root.mainloop()
    
#     def update_window(self):
#         fig, ax = plt.subplots()
#         fig.set_size_inches(11,5.3)
#         global x,y,s,c
#         x,y,s,c = np.random.rand(4,int(self.input.get()))
#         ax.scatter(x,y,s*self.slider.get(),c)
#         ax.axis("off")
#         fig.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)
#         canvas = FigureCanvasTkAgg(fig,master=self.root)
#         canvas.draw()
#         canvas.get_tk_widget().place(relx=0.33, rely=0.025)
#         self.root.update()
        
#     def update_surface(self,other):
#         fig, ax = plt.subplots()
#         fig.set_size_inches(11,5.3)
#         ax.scatter(x,y,s*self.slider.get(),c)
#         ax.axis("off")
#         fig.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)
#         canvas = FigureCanvasTkAgg(fig,master=self.root)
#         canvas.draw()
#         canvas.get_tk_widget().place(relx=0.33, rely=0.025)
#         self.root.update()

# if __name__ == "__main__":        
#     CTK_Window = ctkApp()


# import sys
# import docx

# print(sys.path)
# print(docx.__file__)
