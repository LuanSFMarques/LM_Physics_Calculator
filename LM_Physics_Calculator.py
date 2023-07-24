from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from pint import UnitRegistry

global colors
colors = ["#d6c5c5","#c18b8b","#343f56","#74737a","#a2a5ab","#293244","#404244"]

mainMenu = Tk()
mainMenu.title("LM Physics Calculator")
mainMenu.geometry("600x380")
mainMenu.configure(bg=colors[4])
mainMenu.resizable(False, False)

def open_UnitConverter():
    root_uc = Toplevel()
    root_uc.title("Unit Converter - Menu")
    root_uc.geometry('500x350')
    root_uc.resizable(False, False)
    root_uc.configure(bg=colors[4])
    def open_length():
        u_c_root = Toplevel()
        u_c_root.title("Unit Converter - Length")
        u_c_root.geometry("628x263")
        u_c_root.resizable(False, False)

        frame = Frame(u_c_root)
        frame.configure(bg='#a2a5ab')
        frame.pack()

        def convert():
            number = first_entry.get()
            unit1 = first_unit.get().lower()
            unit2 = second_unit.get().lower()
            testx = 0
            try:
                test = float(number)
                testx = 1
            except:
                messagebox.showerror(title="ERROR", message="Invalid Number!")

            if testx == 1:
                number = float(number)
                unity = UnitRegistry()

                if unit1 == "meter":
                    number *= unity.meter
                elif unit1 == "Kilometer":
                    number *= unity.Kilometer
                elif unit1 == "centimeter":
                    number *= unity.centimeter
                elif unit1 == "millimeter":
                    number *= unity.millimeter
                elif unit1 == "mile":
                    number *= unity.mile
                elif unit1 == "foot":
                    number *= unity.foot
                convertion = str(number.to(unit2)).split()
                convertion = round(float(convertion[0]),6)
                second_entry.config(state="normal")
                second_entry.delete(0, END)
                second_entry.insert(0,convertion)
                second_entry.config(state="readonly")

        UnitConverter = Label(frame, text="Unit Converter - Lenght", font="Times 30", bg=colors[4], fg=colors[2])
        from_label = Label(frame, text="From:", bg=colors[4], font="Times 15", fg=colors[2])
        to_label = Label(frame, text="To:", bg=colors[4], font="Times 15", fg=colors[2])
        first_entry = Entry(frame, bg="white", font="Times 15", width=25)
        second_entry = Entry(frame, bg="white", font="Times 15",state='readonly', width=25)
        first_unit = ttk.Combobox(frame, values=["Meter","Kilometer", "Centimeter", "Millimeter", "Mile", "Foot"], font="Times 15")
        first_unit.current(0)
        second_unit = ttk.Combobox(frame, values=["Meter","Kilometer", "Centimeter", "Millimeter", "Mile", "Foot"], font="Times 15")
        second_unit.current(1)
        button_convert = Button(frame, text="Convert", command=convert, bg=colors[2], fg="white", font="Times 15", relief='sunken')

        UnitConverter.grid(row=0,column=0,columnspan=2,padx=10,pady=20)
        from_label.grid(row=1,column=0)
        to_label.grid(row=1,column=1)
        first_entry.grid(row=2,column=0, padx=30,pady=(0,20))
        second_entry.grid(row=2,column=1, padx=30,pady=(0,20))
        first_unit.grid(row=3,column=0, pady=(10,0))
        second_unit.grid(row=3,column=1, pady=(10,0))
        button_convert.grid(row=4, column=0, columnspan=2, sticky="news", pady=10, padx=10)
    def open_temperature():
        temper_root = Toplevel()
        temper_root.title("Unit Converter - Temperature")
        temper_root.geometry("628x263")
        temper_root.resizable(False, False)

        #---------------------------------------------------------------------------------
        def c_to_k(value):
            return value + 273.15
        def c_to_f(value):
            return ((value*9)/5)+32
        def k_to_c(value):
            return value - 273.15
        def k_to_f(value):
            return (((value-273.15)*9)/5)+32
        def f_to_c(value):
            return ((value-32)*5)/9
        def f_to_k(value):
            return (((value-32)*5)/9)+273.15
        #---------------------------------------------------------------------------------

        def convert():
            number = first_entry.get()
            testx=0
            try:
                test = float(number)
                testx=1
            except:
                messagebox.showerror(title="ERROR", message="Invalid Number!")
            if testx==1:
                number = float(number)
                unit1 = first_unit.get()
                unit2 = second_unit.get()
                if unit1 == unit2:
                    result = number
                else:
                    if unit1 == "Celsius":
                        if unit2 == "Kelvin":
                            result=c_to_k(number)
                        else:
                            result=c_to_f(number)
                    elif unit1 == "Kelvin":
                        if unit2 == "Celsius":
                            result=k_to_c(number)
                        else:
                            result=k_to_f(number)
                    elif unit1 == "Fahrenheit":
                        if unit2 == "Celsius":
                            result=f_to_c(number)
                        else:
                            result=f_to_k(number)
                second_entry.config(state="normal")
                second_entry.delete(0,END)
                second_entry.insert(0,result)
                second_entry.config(state="readonly")
        frame_temper = Frame(temper_root,bg=colors[4])
        frame_temper.pack()

        UnitConverter = Label(frame_temper, text="Unit Converter - Temperature", font="Times 30", bg=colors[4], fg=colors[2])
        from_label = Label(frame_temper, text="From:", bg=colors[4], font="Times 15", fg=colors[2])
        to_label = Label(frame_temper, text="To:", bg=colors[4], font="Times 15", fg=colors[2])
        first_entry = Entry(frame_temper, bg="white", font="Times 15", width=25)
        second_entry = Entry(frame_temper, bg="white", font="Times 15",state='readonly', width=25)
        first_unit = ttk.Combobox(frame_temper, values=["Celsius","Kelvin", "Fahrenheit"], font="Times 15")
        first_unit.current(0)
        second_unit = ttk.Combobox(frame_temper, values=["Celsius","Kelvin", "Fahrenheit"], font="Times 15")
        second_unit.current(1)
        button_convert = Button(frame_temper, text="Convert", command=convert, bg=colors[2], fg="white", font="Times 15", relief='sunken')

        UnitConverter.grid(row=0,column=0,columnspan=2,padx=10,pady=20)
        from_label.grid(row=1,column=0)
        to_label.grid(row=1,column=1)
        first_entry.grid(row=2,column=0, padx=30,pady=(0,20))
        second_entry.grid(row=2,column=1, padx=30,pady=(0,20))
        first_unit.grid(row=3,column=0, pady=(10,0))
        second_unit.grid(row=3,column=1, pady=(10,0))
        button_convert.grid(row=4, column=0, columnspan=2, sticky="news", pady=10, padx=10)
    def open_time():
        temper_root = Toplevel()
        temper_root.title("Unit Converter - Time")
        temper_root.geometry("628x263")
        temper_root.resizable(False, False)

        #---------------------------------------------------------------------------------
        def s_to_min(value):
            return value/60
        def s_to_h(value):
            return value/3600
        def s_to_d(value):
            return value/86400
        def s_to_mil(value):
            return value*1000
        #======================================
        def min_to_s(value):
            return value*60
        def min_to_h(value):
            return value/60
        def min_to_d(value):
            return value*0.0006944444
        def min_to_mil(value):
            return value*60000
        #======================================
        def h_to_s(value):
            return value*3600
        def h_to_min(value):
            return value*60
        def h_to_d(value):
            return value*0.0416666667
        def h_to_mil(value):
            return value*3600000
        #======================================
        def d_to_s(value):
            return value*86400
        def d_to_min(value):
            return value*1440
        def d_to_h(value):
            return value*24
        def d_to_mil(value):
            return value*86400000
        #======================================
        def mil_to_s(value):
            return value*0.001
        def mil_to_min(value):
            return value*0.0000166667
        def mil_to_h(value):
            return value/3600000
        def mil_to_d(value):
            return value/86400000
        #---------------------------------------------------------------------------------

        def convert():
            number = first_entry.get()
            testx=0
            try:
                test = float(number)
                testx=1
            except:
                messagebox.showerror(title="ERROR", message="Invalid Number!")
            if testx==1:
                number = float(number)
                unit1,unit2 = first_unit.get(),second_unit.get()
                if unit1 == unit2:
                    second_entry.config(state="normal")
                    second_entry.delete(0,END)
                    second_entry.insert(0,number)
                    second_entry.config(state="readonly")
                else:
                    if unit1 == "Second":
                        if unit2 == "Minute":
                            result = s_to_min(number)
                        elif unit2 == "Hour":
                            result = s_to_h(number)
                        elif unit2 == "Day":
                            result = s_to_d(number)
                        elif unit2 == "Millisecond":
                            result = s_to_mil(number)
                    elif unit1 == "Minute":
                        if unit2 == "Second":
                            result = min_to_s(number)
                        elif unit2 == "Hour":
                            result = min_to_h(number)
                        elif unit2 == "Day":
                            result = min_to_d(number)
                        elif unit2 == "Millisecond":
                            result = min_to_mil(number)
                    elif unit1 == "Hour":
                        if unit2 == "Second":
                            result = h_to_s(number)
                        elif unit2 == "Minute":
                            result = h_to_min(number)
                        elif unit2 == "Day":
                            result = h_to_d(number)
                        elif unit2 == "Millisecond":
                            result = h_to_mil(number)
                    elif unit1 == "Day":
                        if unit2 == "Second":
                            result = d_to_s(number)
                        elif unit2 == "Minute":
                            result = d_to_min(number)
                        elif unit2 == "Hour":
                            result = d_to_h(number)
                        elif unit2 == "Millisecond":
                            result = d_to_mil(number)
                    elif unit1 == "Millisecond":
                        if unit2 == "Second":
                            result = mil_to_s(number)
                        elif unit2 == "Minute":
                            result = mil_to_min(number)
                        elif unit2 == "Hour":
                            result = mil_to_h(number)
                        elif unit2 == "Day":
                            result = mil_to_d(number)
                    second_entry.config(state="normal")
                    second_entry.delete(0,END)
                    second_entry.insert(0,result)
                    second_entry.config(state="readonly")
        frame_temper = Frame(temper_root,bg=colors[4])
        frame_temper.pack()

        UnitConverter = Label(frame_temper, text="Unit Converter - Time", font="Times 30", bg=colors[4], fg=colors[2])
        from_label = Label(frame_temper, text="From:", bg=colors[4], font="Times 15", fg=colors[2])
        to_label = Label(frame_temper, text="To:", bg=colors[4], font="Times 15", fg=colors[2])
        first_entry = Entry(frame_temper, bg="white", font="Times 15", width=25)
        second_entry = Entry(frame_temper, bg="white", font="Times 15",state='readonly', width=25)
        first_unit = ttk.Combobox(frame_temper, values=["Second","Minute", "Hour", "Day", "Millisecond"], font="Times 15")
        first_unit.current(0)
        second_unit = ttk.Combobox(frame_temper, values=["Second","Minute", "Hour", "Day", "Millisecond"], font="Times 15")
        second_unit.current(1)
        button_convert = Button(frame_temper, text="Convert", command=convert, bg=colors[2], fg="white", font="Times 15", relief='sunken')

        UnitConverter.grid(row=0,column=0,columnspan=2,padx=10,pady=20)
        from_label.grid(row=1,column=0)
        to_label.grid(row=1,column=1)
        first_entry.grid(row=2,column=0, padx=30,pady=(0,20))
        second_entry.grid(row=2,column=1, padx=30,pady=(0,20))
        first_unit.grid(row=3,column=0, pady=(10,0))
        second_unit.grid(row=3,column=1, pady=(10,0))
        button_convert.grid(row=4, column=0, columnspan=2, sticky="news", pady=10, padx=10)
    def open_speed():
        speed_root = Toplevel()
        speed_root.title("Unit Converter - Speed")
        speed_root.geometry("628x263")
        speed_root.resizable(False, False)


        #---------------------------------------------------------------------------------

        def ms_to_kh(i_value):
            i_value*=3.6
            return i_value
        def ms_to_mh(i_value):
            i_value*=2.2369362921
            return i_value
        def ms_to_mm(i_value):
            i_value*=3600
            return i_value
        def ms_to_km(i_value):
            i_value*=0.06
            return i_value
        #===============================
        def kh_to_ms(i_value):
            i_value/=3.6
            return i_value
        def kh_to_mh(i_value):
            i_value*=0.6213711922
            return i_value
        def kh_to_mm(i_value):
            i_value*=16.66666666
            return i_value
        def kh_to_km(i_value):
            i_value*=0.016666666
            return i_value
        #===============================
        def mh_to_ms(i_value):
            i_value*=0.44704
            return i_value
        def mh_to_kh(i_value):
            i_value*=1.609344
            return i_value
        def mh_to_mm(i_value):
            i_value*=26.8224
            return i_value
        def mh_to_km(i_value):
            i_value*=0.0268224
            return i_value
        #===============================
        def mm_to_ms(i_value):
            i_value*=0.016666666
            return i_value
        def mm_to_kh(i_value):
            i_value*=0.06
            return i_value
        def mm_to_mh(i_value):
            i_value*=0.0372822715
            return i_value
        def mm_to_km(i_value):
            i_value*=0.001
            return i_value
        #===============================
        def km_to_ms(i_value):
            i_value*=16.66666666
            return i_value
        def km_to_kh(i_value):
            i_value*=60
            return i_value
        def km_to_mh(i_value):
            i_value*=37.282271534
            return i_value
        def km_to_mm(i_value):
            i_value*=1000
            return i_value
        #---------------------------------------------------------------------------------

        def convert():
            value1 = first_entry.get()
            testx= 0
            try:
                test = float(value1)
                testx = 1
            except:
                messagebox.showerror(title="ERROR", message="Invalid Number!")
            if testx == 1:
                value1 = float(value1)
                unit1 = first_unit.get()
                unit2 = second_unit.get()
                if unit1 == unit2:
                    second_entry.config(state="normal")
                    second_entry.delete(0,END)
                    second_entry.insert(0,value1)
                    second_entry.config(state="readonly")
                else:
                    if str(unit1) == "Meter/Second":
                        if str(unit2) == "Kilometer/Hour":
                            result = ms_to_kh(value1)
                        elif str(unit2) == "Mile/Hour":
                            result = ms_to_mh(value1)
                        elif str(unit2) == "Meter/Minute":
                            result = ms_to_mm(value1)
                        elif str(unit2) == "Kilometer/Minute":
                            result = ms_to_km(value1)
                    elif str(unit1) == "Kilometer/Hour":
                        if str(unit2) == "Meter/Second":
                            result = kh_to_ms(value1)
                        elif str(unit2) == "Mile/Hour":
                            result = kh_to_mh(value1)
                        elif str(unit2) == "Meter/Minute":
                            result = kh_to_mm(value1)
                        elif str(unit2) == "Kilometer/Minute":
                            result = kh_to_km(value1)
                    elif str(unit1) == "Mile/Hour":
                        if str(unit2) == "Meter/Second":
                            result = mh_to_ms(value1)
                        elif str(unit2) == "Kilometer/Hour":
                            result = mh_to_kh(value1)
                        elif str(unit2) == "Meter/Minute":
                            result = mh_to_mm(value1)
                        elif str(unit2) == "Kilometer/Minute":
                            result = mh_to_km(value1)
                    elif str(unit1) == "Meter/Minute":
                        if str(unit2) == "Meter/Second":
                            result = mm_to_ms(value1)
                        elif str(unit2) == "Kilometer/Hour":
                            result = mm_to_kh(value1)
                        elif str(unit2) == "Mile/Hour":
                            result = mm_to_mh(value1)
                        elif str(unit2) == "Kilometer/Minute":
                            result = mm_to_km(value1)
                    elif str(unit1) == "Kilometer/Minute":
                        if str(unit2) == "Meter/Second":
                            result = km_to_ms(value1)
                        elif str(unit2) == "Kilometer/Hour":
                            result = km_to_kh(value1)
                        elif str(unit2) == "Mile/Hour":
                            result = km_to_mh(value1)
                        elif str(unit2) == "Meter/Minute":
                            result = km_to_mm(value1)
                    second_entry.config(state="normal")
                    second_entry.delete(0,END)
                    second_entry.insert(0,result)
                    second_entry.config(state="readonly")
                

        frame_speed = Frame(speed_root,bg=colors[4])
        frame_speed.pack()

        UnitConverter = Label(frame_speed, text="Unit Converter - Speed", font="Times 30", bg=colors[4], fg=colors[2])
        from_label = Label(frame_speed, text="From:", bg=colors[4], font="Times 15", fg=colors[2])
        to_label = Label(frame_speed, text="To:", bg=colors[4], font="Times 15", fg=colors[2])
        first_entry = Entry(frame_speed, bg="white", font="Times 15", width=25)
        second_entry = Entry(frame_speed, bg="white", font="Times 15",state='readonly', width=25)
        first_unit = ttk.Combobox(frame_speed, values=["Meter/Second","Kilometer/Hour", "Mile/Hour", "Meter/Minute", "Kilometer/Minute"], font="Times 15")
        first_unit.current(0)
        second_unit = ttk.Combobox(frame_speed, values=["Meter/Second","Kilometer/Hour", "Mile/Hour", "Meter/Minute", "Kilometer/Minute"], font="Times 15")
        second_unit.current(1)
        button_convert = Button(frame_speed, text="Convert", command=convert, bg=colors[2], fg="white", font="Times 15", relief='sunken')

        UnitConverter.grid(row=0,column=0,columnspan=2,padx=10,pady=20)
        from_label.grid(row=1,column=0)
        to_label.grid(row=1,column=1)
        first_entry.grid(row=2,column=0, padx=30,pady=(0,20))
        second_entry.grid(row=2,column=1, padx=30,pady=(0,20))
        first_unit.grid(row=3,column=0, pady=(10,0))
        second_unit.grid(row=3,column=1, pady=(10,0))
        button_convert.grid(row=4, column=0, columnspan=2, sticky="news", pady=10, padx=10)

    #---------------------------------------------------------------------------------------------------------------------------------FUNCTIONS end

    frame_uc = Frame(root_uc, bg=colors[4])
    frame_uc.pack()

    title_label = Label(frame_uc,text="Unit Converter - Menu", font="Times 30", bg=colors[4], fg=colors[2])
    subtitle_label = Label(frame_uc,text="Select a converter type", bg=colors[4], font="Times 20", fg=colors[2])

    length_button = Button(frame_uc, text="Length Convertion",command=open_length, bg=colors[2], font="Times 15", fg="white", relief='sunken')
    temper_button = Button(frame_uc, text="Temperature Convertion",command=open_temperature, bg=colors[5], font="Times 15", fg="white", relief='sunken')
    time_button = Button(frame_uc, text="Time Convertion",command=open_time, bg=colors[2], font="Times 15", fg="white", relief='sunken')
    weight_button = Button(frame_uc, text="Speed Convertion",command=open_speed, bg=colors[5], font="Times 15", fg="white", relief='sunken')

    title_label.grid(row=0, column=0,pady=(15,0))
    subtitle_label.grid(row=1, column=0,pady=10)

    length_button.grid(row=2,column=0,sticky=NSEW,pady=5)
    temper_button.grid(row=3,column=0,sticky=NSEW,pady=5)
    time_button.grid(row=4,column=0,sticky=NSEW,pady=5)
    weight_button.grid(row=5,column=0,sticky=NSEW,pady=5)
def open_BasicPhysics():
    root_uc = Toplevel()
    root_uc.title("Basic Physics - Menu")
    root_uc.geometry('500x350')
    root_uc.resizable(False, False)
    root_uc.configure(bg=colors[4])
    #---------------------------------------------------------------------------------------------------------------------------------FUNCTIONS start
    def open_velocity():
        root_force = Toplevel()
        root_force.title("Basic Physics - Velocity Calculator")
        root_force.configure(bg=colors[4])
        root_force.geometry("580x300")
        root_force.resizable(False, False)

        def forceCalculator():
            value1=distance_entry.get()
            value2=time_entry.get()
            value3=velocity_entry.get()
            test_list = [value1,value2,value3]
            converter_list = []
            count=0
            for each in test_list:
                if each == "":
                    count += 1
                else:
                    converter_list.append(each)
            if count != 1:
                messagebox.showerror(title="ERROR", message="There should be only one empty variable to determine")
            else:
                try:
                    test=float(converter_list[0])+float(converter_list[1])
                except:
                    messagebox.showerror(title="ERROR", message="Invalid number!") 
                    return
                if value2!='' and value3!='':
                    value2,value3 = float(value2),float(value3)
                    result = value2*value3
                    distance_entry.insert(0, result)
                elif value2!="" and value1!="":
                    value2,value1 = float(value2),float(value1)
                    result = value1/value2
                    velocity_entry.insert(0, result)
                else:
                    value3,value1 = float(value3),float(value1)
                    result = value1/value3
                    time_entry.insert(0, result)

        def clear():
            distance_entry.delete(0,END)
            time_entry.delete(0,END)
            velocity_entry.delete(0,END)

        frame = Frame(root_force)
        frame.configure(bg=colors[4])
        frame.pack()

        title_label=Label(frame, text="Basic Physics - Velocity Calculator",font="Times 30", bg=colors[4], fg=colors[2])
        distance_label = Label(frame, text="Distance (m)",font="Times 15", fg=colors[2],bg=colors[4])
        distance_entry = Entry(frame,font="Times 15")
        time_label = Label(frame, text="Time (s)",font="Times 15", fg=colors[2],bg=colors[4])
        time_entry = Entry(frame,font="Times 15")
        velocity_label = Label(frame, text="Velocity (m/s)",font="Times 15", fg=colors[2],bg=colors[4])
        velocity_entry = Entry(frame,font="Times 15")
        button_calculate = Button(frame,bg=colors[5],text="Calculate",font="Times 15", fg='white',relief="sunken",command=forceCalculator)
        button_clear = Button(frame,bg=colors[5],text="Clear",font="Times 15", fg='white',relief="sunken",width=10,command=clear)

        title_label.grid(row=0,column=0,columnspan=2,pady=10)
        distance_label.grid(row=1,column=0,sticky=E,pady=3)
        distance_entry.grid(row=1,column=1,sticky=W,pady=3)
        time_label.grid(row=2,column=0,sticky=E,pady=3)
        time_entry.grid(row=2,column=1,sticky=W,pady=3)
        velocity_label.grid(row=3,column=0,sticky=E,pady=3)
        velocity_entry.grid(row=3,column=1,sticky=W,pady=3)
        button_calculate.grid(row=4,column=0,columnspan=2,sticky=EW,pady=10)
        button_clear.grid(row=5,column=0,columnspan=2,pady=10)
    def open_force():
        root_force = Toplevel()
        root_force.title("Basic Physics - Force Calculator")
        root_force.configure(bg=colors[4])
        root_force.geometry("580x300")
        root_force.resizable(False, False)
        def forceCalculator():
            value1=force_entry.get()
            value2=mass_entry.get()
            value3=acceleration_entry.get()
            test_list = [value1,value2,value3]
            converter_list = []
            count=0
            for each in test_list:
                if each == "":
                    count += 1
                else:
                    converter_list.append(each)
            if count != 1:
                messagebox.showerror(title="ERROR", message="There should be only one empty variable to determine")
            else:
                try:
                    test=float(converter_list[0])+float(converter_list[1])
                except:
                    messagebox.showerror(title="ERROR", message="Invalid number!") 
                    return
                if value2!='' and value3!='':
                    value2,value3 = float(value2),float(value3)
                    result = value2*value3
                    force_entry.insert(0, result)
                elif value2!="" and value1!="":
                    value2,value1 = float(value2),float(value1)
                    result = value1/value2
                    acceleration_entry.insert(0, result)
                else:
                    value3,value1 = float(value3),float(value1)
                    result = value1/value3
                    mass_entry.insert(0, result)

        def clear():
            force_entry.delete(0,END)
            acceleration_entry.delete(0,END)
            mass_entry.delete(0,END)
        frame = Frame(root_force)
        frame.configure(bg=colors[4])
        frame.pack()

        title_label=Label(frame, text="Basic Physics - Force Calculator",font="Times 30", bg=colors[4], fg=colors[2])
        force_label = Label(frame, text="Force (N)",font="Times 15", fg=colors[2],bg=colors[4])
        force_entry = Entry(frame,font="Times 15")
        mass_label = Label(frame, text="Mass (Kg)",font="Times 15", fg=colors[2],bg=colors[4])
        mass_entry = Entry(frame,font="Times 15")
        acceleration_label = Label(frame, text="Acceleration (m/s**2)",font="Times 15", fg=colors[2],bg=colors[4])
        acceleration_entry = Entry(frame,font="Times 15")
        button_calculate = Button(frame,bg=colors[5],text="Calculate",font="Times 15", fg='white',relief="sunken",command=forceCalculator)
        button_clear = Button(frame,bg=colors[5],text="Clear",font="Times 15", fg='white',relief="sunken",width=10,command=clear)

        title_label.grid(row=0,column=0,columnspan=2,pady=10)
        force_label.grid(row=1,column=0,sticky=E,pady=3)
        force_entry.grid(row=1,column=1,sticky=W,pady=3)
        mass_label.grid(row=2,column=0,sticky=E,pady=3)
        mass_entry.grid(row=2,column=1,sticky=W,pady=3)
        acceleration_label.grid(row=3,column=0,sticky=E,pady=3)
        acceleration_entry.grid(row=3,column=1,sticky=W,pady=3)
        button_calculate.grid(row=4,column=0,columnspan=2,sticky=EW,pady=10)
        button_clear.grid(row=5,column=0,columnspan=2,pady=10)
    def open_acceleration():
        root_force = Toplevel()
        root_force.title("Basic Physics - Acceleration Calculator")
        root_force.configure(bg=colors[4])
        root_force.geometry("650x320")
        #root_force.resizable(False, False)
        def forceCalculator():
            value1=initial_speed_entry.get()
            value2=final_speed_entry.get()
            value3=time_entry.get()
            value4=acceleration_entry.get()
            test_list = [value1,value2,value3,value4]
            converter_list = []
            count=0
            for each in test_list:
                if each == "":
                    count += 1
                else:
                    converter_list.append(each)
            if count != 1:
                messagebox.showerror(title="ERROR", message="There should be only one empty variable to determine")
            else:
                try:
                    test1,test2,test3=float(converter_list[0]),float(converter_list[1]),float(converter_list[2])
                except:
                    messagebox.showerror(title="ERROR", message="Invalid number!") 
                    return
                if value1!='' and value2!='' and value3!='':
                    final_value = (test2-test1)/test3
                    acceleration_entry.insert(0,final_value)
                elif value1!="" and value3!="" and value4!="":
                    final_value = test1+(test3*test2)
                    final_speed_entry.insert(0,final_value)
                elif value1!="" and value2!="" and value4!="":
                    final_value = (test2-test1)/test3
                    if float(final_value) < 0:
                        final_value = str(final_value) + " (Negative Time)"
                    time_entry.insert(0,final_value)
                elif value2!="" and value3!="" and value4!="":
                    final_value = (test2*test3)-test1
                    final_value = "-" + str(final_value)
                    initial_speed_entry.insert(0,final_value)
                print(final_value)
        def clear():
            initial_speed_entry.delete(0,END)
            final_speed_entry.delete(0,END)
            time_entry.delete(0,END)
            acceleration_entry.delete(0,END)
        frame = Frame(root_force)
        frame.configure(bg=colors[4])
        frame.pack()

        title_label=Label(frame, text="Basic Physics - Acceleration Calculator",font="Times 30", bg=colors[4], fg=colors[2])
        initial_speed_label = Label(frame, text="Initial Speed (m/s)",font="Times 15", fg=colors[2],bg=colors[4])
        initial_speed_entry = Entry(frame,font="Times 15")
        final_speed_label = Label(frame, text="Final Speed (m/s)",font="Times 15", fg=colors[2],bg=colors[4])
        final_speed_entry = Entry(frame,font="Times 15")
        time_label = Label(frame, text="Time (s)",font="Times 15", fg=colors[2],bg=colors[4])
        time_entry = Entry(frame,font="Times 15")
        acceleration_label = Label(frame, text="Acceleration (m/s**2)",font="Times 15", fg=colors[2],bg=colors[4])
        acceleration_entry = Entry(frame,font="Times 15")
        button_calculate = Button(frame,bg=colors[5],text="Calculate",font="Times 15", fg='white',relief="sunken",command=forceCalculator)
        button_clear = Button(frame,bg=colors[5],text="Clear",font="Times 15", fg='white',relief="sunken",width=10,command=clear)

        title_label.grid(row=0,column=0,columnspan=2,pady=10)
        initial_speed_label.grid(row=1,column=0,sticky=E,pady=3)
        initial_speed_entry.grid(row=1,column=1,sticky=W,pady=3)
        final_speed_label.grid(row=2,column=0,sticky=E,pady=3)
        final_speed_entry.grid(row=2,column=1,sticky=W,pady=3)
        time_label.grid(row=3,column=0,sticky=E,pady=3)
        time_entry.grid(row=3,column=1,sticky=W,pady=3)
        acceleration_label.grid(row=4,column=0,sticky=E,pady=3)
        acceleration_entry.grid(row=4,column=1,sticky=W,pady=3)
        button_calculate.grid(row=5,column=0,columnspan=2,sticky=EW,pady=10)
        button_clear.grid(row=6,column=0,columnspan=2,pady=10)
    def planet_weight():
        root_force = Toplevel()
        root_force.title("Basic Physics - Weight in Planets")
        root_force.configure(bg=colors[4])
        root_force.geometry("580x430")
        root_force.resizable(False, False)

        def calculate():
            testx=0
            try:
                test = float(weight_entry.get())
                testx=1
            except:
                messagebox.showerror(title="ERROR", message="Invalid Number!")
            if testx==1:
                value = weight_entry.get()
                value = float(value)

                moon_value=value*0.167
                mercury_value=value*0.4
                venus_value=value*0.9
                mars_value=value*0.4
                jupiter_value=value*2.3
                saturn_value=value*1.1
                neptune_value=value*1.2
                uranus_value=value*0.9
                pluto_value=value*0.1

                moon_entry.config(state="normal")
                moon_entry.delete(0,END)
                mercury_entry.config(state="normal")
                mercury_entry.delete(0,END)
                venus_entry.config(state="normal")
                venus_entry.delete(0,END)
                mars_entry.config(state="normal")
                mars_entry.delete(0,END)
                jupiter_entry.config(state="normal")
                jupiter_entry.delete(0,END)
                saturn_entry.config(state="normal")
                saturn_entry.delete(0,END)
                neptune_entry.config(state="normal")
                neptune_entry.delete(0,END)
                uranus_entry.config(state="normal")
                uranus_entry.delete(0,END)
                pluto_entry.config(state="normal")
                pluto_entry.delete(0,END)
                moon_entry.insert(0,moon_value)
                mercury_entry.insert(0,mercury_value)
                venus_entry.insert(0,venus_value)
                mars_entry.insert(0,mars_value)
                jupiter_entry.insert(0,jupiter_value)
                saturn_entry.insert(0,saturn_value)
                neptune_entry.insert(0,neptune_value)
                uranus_entry.insert(0,uranus_value)
                pluto_entry.insert(0,pluto_value)
                moon_entry.config(state="readonly")
                mercury_entry.config(state="readonly")
                venus_entry.config(state="readonly")
                mars_entry.config(state="readonly")
                jupiter_entry.config(state="readonly")
                saturn_entry.config(state="readonly")
                neptune_entry.config(state="readonly")
                uranus_entry.config(state="readonly")
                pluto_entry.config(state="readonly")

        frame = Frame(root_force)
        frame.configure(bg=colors[4])
        frame.pack()

        title_label=Label(frame, text="Basic Physics - Weight in Planets",font="Times 30", bg=colors[4], fg=colors[2])
        weight_label = Label(frame, text="Your Weight (Kg)",font="Times 15", fg=colors[2],bg=colors[4])
        weight_entry = Entry(frame,font="Times 15")
        button = Button(frame, font="Times 15",text="calculate",command=calculate, bg=colors[2], fg="white")
        moon_label = Label(frame, font="Times 15",text="Moon: ",bg=colors[4])
        moon_entry = Entry(frame, font="Times 15",state="readonly")
        mercury_label = Label(frame, font="Times 15",text="Mercury: ",bg=colors[4])
        mercury_entry = Entry(frame, font="Times 15",state="readonly")
        venus_label = Label(frame, font="Times 15",text="Venus: ",bg=colors[4])
        venus_entry = Entry(frame, font="Times 15",state="readonly")
        mars_label = Label(frame, font="Times 15",text="Mars: ",bg=colors[4])
        mars_entry = Entry(frame, font="Times 15",state="readonly")
        jupiter_label = Label(frame, font="Times 15",text="Jupiter: ",bg=colors[4])
        jupiter_entry = Entry(frame, font="Times 15",state="readonly")
        saturn_label = Label(frame, font="Times 15",text="Saturn: ",bg=colors[4])
        saturn_entry = Entry(frame, font="Times 15",state="readonly")
        neptune_label = Label(frame, font="Times 15",text="Neptune: ",bg=colors[4])
        neptune_entry = Entry(frame, font="Times 15",state="readonly")
        uranus_label = Label(frame, font="Times 15",text="Uranus: ",bg=colors[4])
        uranus_entry = Entry(frame, font="Times 15",state="readonly")
        pluto_label = Label(frame, font="Times 15",text="Pluto: ",bg=colors[4])
        pluto_entry = Entry(frame, font="Times 15",state="readonly")



        title_label.grid(row=0,column=0,columnspan=2,pady=10)
        weight_label.grid(row=1,column=0,sticky=E,pady=3)
        weight_entry.grid(row=1,column=1,sticky=W,pady=3)
        button.grid(row=2,column=0,columnspan=2,sticky=EW,pady=10)
        moon_label.grid(row=3,column=0, sticky="E")
        moon_entry.grid(row=3,column=1, sticky="W")
        mercury_label.grid(row=4,column=0, sticky="E")
        mercury_entry.grid(row=4,column=1, sticky="W")
        venus_label.grid(row=5,column=0, sticky="E")
        venus_entry.grid(row=5,column=1, sticky="W")
        mars_label.grid(row=6,column=0, sticky="E") 
        mars_entry.grid(row=6,column=1, sticky="W") 
        jupiter_label.grid(row=7,column=0, sticky="E")
        jupiter_entry.grid(row=7,column=1, sticky="W")
        saturn_label.grid(row=8,column=0, sticky="E")
        saturn_entry.grid(row=8,column=1, sticky="W")
        neptune_label.grid(row=9,column=0, sticky="E")
        neptune_entry.grid(row=9,column=1, sticky="W")
        uranus_label.grid(row=10,column=0, sticky="E")
        uranus_entry.grid(row=10,column=1, sticky="W")
        pluto_label.grid(row=11,column=0, sticky="E")
        pluto_entry.grid(row=11,column=1, sticky="W")
    #---------------------------------------------------------------------------------------------------------------------------------FUNCTIONS end

    frame_uc = Frame(root_uc, bg=colors[4])
    frame_uc.pack()

    title_label = Label(frame_uc,text="Basic Physics - Menu", font="Times 30", bg=colors[4], fg=colors[2])
    subtitle_label = Label(frame_uc,text="Select one calculator type", bg=colors[4], font="Times 20", fg=colors[2])

    length_button = Button(frame_uc, text="Velocity Calculator",command=open_velocity, bg=colors[2], font="Times 15", fg="white", relief='sunken')
    temper_button = Button(frame_uc, text="Force Calculator",command=open_force, bg=colors[5], font="Times 15", fg="white", relief='sunken')
    time_button = Button(frame_uc, text="Acceleration Calculator",command=open_acceleration, bg=colors[2], font="Times 15", fg="white", relief='sunken')
    weight_button = Button(frame_uc, text="Weight in planets",command=planet_weight, bg=colors[5], font="Times 15", fg="white", relief='sunken')

    title_label.grid(row=0, column=0,pady=(15,0))
    subtitle_label.grid(row=1, column=0,pady=10)

    length_button.grid(row=2,column=0,sticky=NSEW,pady=5)
    temper_button.grid(row=3,column=0,sticky=NSEW,pady=5)
    time_button.grid(row=4,column=0,sticky=NSEW,pady=5)
    weight_button.grid(row=5,column=0,sticky=NSEW,pady=5)


frame = Frame(mainMenu, bg=colors[4])
frame.pack()

title_label = Label(frame,text="LM Physics Calculator", font="Times 35", bg=colors[4], fg=colors[2])
subtitle_label = Label(frame,text="Select a category", bg=colors[4], font="Times 25", fg=colors[2])
button1 = Button(frame, text="Unit Converter", bg=colors[2], font="Times 20", fg="white", relief='sunken', command=open_UnitConverter)
button2 = Button(frame, text="Basic Physics", bg=colors[5], font="Times 20", fg="white", relief='sunken', command=open_BasicPhysics)
credits_label_one = Label(frame,text="Made by Luan de Souza Ferreira Marques",bg=colors[4], font="Times 15", fg=colors[6])
credits_label_two = Label(frame,text="Github: https://github.com/LuanSFMarques",bg=colors[4], font="Times 15", fg=colors[6])


title_label.grid(row=0, column=0,pady=(15,0),padx=20)
subtitle_label.grid(row=1, column=0,pady=10)
button1.grid(row=2,column=0,sticky=NSEW,pady=5,padx=10)
button2.grid(row=3,column=0,sticky=NSEW,pady=5,padx=10)
credits_label_one.grid(row=4,column=0,pady=(40,5))
credits_label_two.grid(row=5,column=0,pady=(5))



mainMenu.mainloop()