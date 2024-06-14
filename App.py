import os
import tkinter as tk
import tkinter.messagebox as mb
from tkinter import ttk
from PIL import Image, ImageTk
from QLSP import *
from User import *

PATH_DIRECTORY = os.path.dirname(__file__)
PATH_IMG = os.path.join(PATH_DIRECTORY, "img")


def create_dropdown(event, menu):
    try:
        menu.tk_popup(event.x_root, event.y_root)
    finally:
        menu.grab_release()


class App:
    def __init__(self):
        self.qlsp = QLSP("products.json")
        self.users = UserData("user.json")
        self.main = tk.Tk()
        self.main.withdraw()
        self.Login = tk.Toplevel(self.main)
        self.LoginPage(self.Login, "Đăng nhập", (400, 600))
        # self.ManageWin2  = tk.Toplevel(self.main)
        # self.ManagePage2(self.ManageWin2,"dad",(850,800))
        self.main.mainloop()

    def DestroyWin(self, main, window):
        window.destroy()
        main.destroy()

    def TopLevelPage(self, window, title, size):
        window.protocol(
            "WM_DELETE_WINDOW", lambda m=self.main, w=window: self.DestroyWin(m, w)
        )
        window.title(title)
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width / 2) - (size[0] / 2)
        y = (screen_height / 2) - (size[1] / 2) - 30
        window.geometry(f"{size[0]}x{size[1]}+{int(x)}+{int(y)}")
        window.minsize(size[0], size[1])
        window.iconbitmap(os.path.join(PATH_IMG, "logo.ico"))

    def LoginPage(self, window, title, size):
        self.TopLevelPage(window, title, size)
        window.resizable(False, False)
        load_img = Image.open(os.path.join(PATH_IMG, "bg.png"))
        render_img = ImageTk.PhotoImage(load_img)
        bg = tk.Label(window, image=render_img)
        bg.place(x=0, y=0, rely=0)

        load_img2 = Image.open(os.path.join(PATH_IMG, "user.png"))
        newsize = (160, 160)
        resize_load2 = load_img2.resize(newsize, Image.LANCZOS)
        render_img2 = ImageTk.PhotoImage(resize_load2)
        user_img = tk.Label(window, image=render_img2)
        user_img.place(
            x=(size[0] - newsize[0]) / 2, y=50, relheight=0.25, relwidth=0.38
        )
        title_login = tk.Label(
            window,
            text="Login",
            bg="#B39AFF",
            fg="white",
            font=("Helvetica", 28, "bold"),
        )
        title_login.place(anchor="center", relx=0.5, rely=0.39)
        user_frame = tk.LabelFrame(
            window,
            text="Username",
            bg="#F81186",
            fg="lightblue",
            font=("Times New Roman", 12, "bold"),
        )
        user_frame.place(anchor="center", relx=0.5, rely=0.55, relwidth=0.7, height=60)
        user_entry = tk.Entry(user_frame, font=("Times New Roman", 15))
        user_entry.pack(fill="both", expand=True, padx=5, pady=5)
        pw_frame = tk.LabelFrame(
            window,
            text="Password",
            bg="#F81186",
            fg="lightblue",
            font=("Times New Roman", 12, "bold"),
        )
        pw_frame.place(anchor="center", relx=0.5, rely=0.66, relwidth=0.7, height=60)
        pw_entry = tk.Entry(pw_frame, font=("Times New Roman", 15), show="*")
        pw_entry.pack(fill="both", expand=True, padx=5, pady=5)
        register_label = tk.Label(
            window,
            text="Register Account",
            bg="#F81186",
            fg="lightblue",
            font=("Times New Roman", 12, "bold"),
        )
        register_label.pack(pady=(450, 0), padx=60, anchor="e")
        register_label.bind("<Button-1>", self.ChangeToRegister)
        login_btn = tk.Button(
            window,
            text="Login",
            bg="#B39AFF",
            fg="white",
            font=("Times New Roman", 15, "bold"),
            borderwidth=1,
            command=lambda us=user_entry, pw=pw_entry: self.LoginBTN(us, pw),
        )
        login_btn.pack(pady=(20, 0), ipadx=15, ipady=5)
        window.mainloop()

    def InfoPage(self, window, title, size, user):
        window.title(title)
        username = user["username"]
        email = user["email"]
        level = user["level"]
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width / 2) - (size[0] / 2)
        y = (screen_height / 2) - (size[1] / 2) - 30
        window.geometry(f"{size[0]}x{size[1]}+{int(x)}+{int(y)}")
        window.minsize(size[0], size[1])
        window.iconbitmap(os.path.join(PATH_IMG, "logo.ico"))
        window.resizable(False, False)
        load_img = Image.open(os.path.join(PATH_IMG, "bg.png"))
        render_img = ImageTk.PhotoImage(load_img)
        bg = tk.Label(window, image=render_img)
        bg.place(x=0, y=0, rely=0)

        load_img2 = Image.open(os.path.join(PATH_IMG, "user.png"))
        newsize = (160, 160)
        resize_load2 = load_img2.resize(newsize, Image.LANCZOS)
        render_img2 = ImageTk.PhotoImage(resize_load2)
        user_img = tk.Label(window, image=render_img2)
        user_img.place(
            x=(size[0] - newsize[0]) / 2, y=50, relheight=0.25, relwidth=0.38
        )
        title_login = tk.Label(
            window,
            text="Your Account",
            bg="#B39AFF",
            fg="white",
            font=("Helvetica", 28, "bold"),
        )
        title_login.place(anchor="center", relx=0.5, rely=0.39)
        user_frame = tk.LabelFrame(
            window,
            text="Username",
            bg="#A699FD",
            fg="darkred",
            font=("Times New Roman", 12, "bold"),
        )
        user_frame.pack(fill="both", padx=50, pady=(350, 5))
        user_entry = tk.Label(
            user_frame, text=f"{username}", font=("Times New Roman", 15)
        )
        user_entry.pack(fill="both", expand=True, padx=5, pady=5)
        email_frame = tk.LabelFrame(
            window,
            text="Email",
            bg="#A699FD",
            fg="darkred",
            font=("Times New Roman", 12, "bold"),
        )
        email_frame.pack(fill="both", padx=50, pady=5)
        email_entry = tk.Label(
            email_frame, text=f"{email}", font=("Times New Roman", 15)
        )
        email_entry.pack(fill="both", expand=True, padx=5, pady=5)

        level_frame = tk.LabelFrame(
            window,
            text="LEVEL",
            bg="#A699FD",
            fg="darkred",
            font=("Times New Roman", 12, "bold"),
        )
        level_frame.pack(fill="both", padx=50, pady=5)
        level_entry = tk.Label(
            level_frame, text=f"{level}", font=("Times New Roman", 15)
        )
        level_entry.pack(fill="both", expand=True, padx=5, pady=5)
        window.mainloop()

    def RegisterPage(self, window, title, size):
        self.TopLevelPage(window, title, size)
        window.resizable(False, False)
        load_img = Image.open(os.path.join(PATH_IMG, "bg.png"))
        render_img = ImageTk.PhotoImage(load_img)
        bg = tk.Label(window, image=render_img)
        bg.place(x=0, y=0, rely=0)
        title_page = tk.Label(
            window,
            text="Create Account",
            bg="#A699FD",
            fg="white",
            font=("Times New Roman", 28, "bold"),
        )
        title_page.pack(pady=(0, 10), fill="both", ipady=10)

        user_frame = tk.LabelFrame(
            window,
            text="Username",
            bg="#A699FD",
            fg="darkred",
            font=("Times New Roman", 12, "bold"),
        )
        user_frame.pack(fill="both", padx=50, pady=(30, 5))
        user_entry = tk.Entry(user_frame, font=("Times New Roman", 15))
        user_entry.pack(fill="both", expand=True, padx=5, pady=5)
        email_frame = tk.LabelFrame(
            window,
            text="Email",
            bg="#A699FD",
            fg="darkred",
            font=("Times New Roman", 12, "bold"),
        )
        email_frame.pack(fill="both", padx=50, pady=5)
        email_entry = tk.Entry(email_frame, font=("Times New Roman", 15))
        email_entry.pack(fill="both", expand=True, padx=5, pady=5)
        pw_frame = tk.LabelFrame(
            window,
            text="Password",
            bg="#A699FD",
            fg="darkred",
            font=("Times New Roman", 12, "bold"),
        )
        pw_frame.pack(fill="both", padx=50, pady=5)
        pw_entry = tk.Entry(pw_frame, font=("Times New Roman", 15), show="*")
        pw_entry.pack(fill="both", expand=True, padx=5, pady=5)
        repw_frame = tk.LabelFrame(
            window,
            text="Confirm Password",
            bg="#F81186",
            fg="lightblue",
            font=("Times New Roman", 12, "bold"),
        )
        repw_frame.pack(fill="both", padx=50, pady=5)
        repw_entry = tk.Entry(repw_frame, font=("Times New Roman", 15), show="*")
        repw_entry.pack(fill="both", expand=True, padx=5, pady=5)
        level_frame = tk.LabelFrame(
            window,
            text="LEVEL",
            bg="#F81186",
            fg="lightblue",
            font=("Times New Roman", 12, "bold"),
        )
        level_frame.pack(fill="both", padx=50, pady=5)
        level_entry = ttk.Combobox(
            level_frame,
            values=["Level 1", "Level 2"],
            font=("Times New Roman", 12, "bold"),
        )
        level_entry.pack(fill="both", expand=True, padx=5, pady=5)
        regis_btn = tk.Button(
            window,
            text="Sign Up",
            bg="#B39AFF",
            fg="white",
            font=("Times New Roman", 15, "bold"),
            borderwidth=1,
            command=lambda us=user_entry, e=email_entry, pw=pw_entry, repw=repw_entry, lv=level_entry: self.RegisterBTN(
                us, e, pw, repw, lv
            ),
        )
        regis_btn.pack(pady=10)
        frame = tk.Frame(window)
        frame.pack()
        login_label = tk.Label(
            frame,
            text="Already have an account?",
            bg="#FD4493",
            fg="white",
            font=("Times New Roman", 15, "bold"),
        )
        login_label.grid(row=0, column=0)
        login_label2 = tk.Label(
            frame,
            text="Login",
            bg="#F051A4",
            fg="darkred",
            font=("Times New Roman", 15, "bold"),
        )
        login_label2.grid(row=0, column=1)
        login_label2.bind("<Button-1>", self.ChangeToLogin)
        window.mainloop()

    def ChangeToRegister(self, e):
        self.Login.destroy()
        self.Register = tk.Toplevel(self.main)
        self.RegisterPage(self.Register, "Đăng kí", (400, 600))

    def ChangeToLogin(self, e):
        self.Register.destroy()
        self.Login = tk.Toplevel(self.main)
        self.LoginPage(self.Login, "Đăng nhập", (400, 600))

    def ManagePage(self, window, title, size):
        self.TopLevelPage(window, title, size)
        menu_frame = tk.Frame(window)
        menu_frame.pack(fill="both")
        acc_label = tk.Label(
            menu_frame, text="Account", font=("Helvetica", 13), fg="gray"
        )
        acc_label.pack(anchor="w", padx=20)
        accmenu = tk.Menu(window, tearoff=0, font=("Helvetica", 13), fg="gray")
        accmenu.add_command(
            label="Info", command=lambda us=self.user: self.Info_BTN(us)
        )
        accmenu.add_command(
            label="Log Out", command=lambda win=self.ManageWin: self.LogOut(win)
        )
        acc_label.bind("<Button-1>", lambda event: create_dropdown(event, accmenu))
        frame1 = tk.Frame(window)
        frame1.pack(fill="both")
        frame2 = tk.Frame(window)
        frame2.pack(fill="both", expand=True)
        frame3 = tk.Frame(window)
        frame3.pack(fill="both", pady=(0, 20))
        filter_product_frame = tk.LabelFrame(
            frame1, font=("Time New Roman", 15, "bold"), text="Lọc sản phẩm"
        )
        filter_product_frame.columnconfigure((0, 2, 3, 4, 6), weight=2)
        filter_product_frame.columnconfigure((1, 5, 7), weight=1)
        filter_product_frame.pack(fill="x", padx=20)

        pro_label_filter = ttk.Label(filter_product_frame, text="Sản phẩm:")
        pro_label_filter.grid(row=0, column=0, pady=10, padx=5, sticky=tk.E)
        pro_entry_filter = ttk.Entry(filter_product_frame)
        pro_entry_filter.grid(row=0, column=1, padx=(5, 10), pady=10, sticky=tk.W)
        sort_label_filter = ttk.Label(filter_product_frame, text="Sắp xếp theo:")
        sort_label_filter.grid(row=1, column=0, pady=10, padx=5, sticky=tk.E)
        sort_entry_filter = ttk.Combobox(
            filter_product_frame,
            values=[
                "Giá tăng dần",
                "Giá giảm dần",
                "Hàng tồn kho tăng dần",
                "Hàng tồn kho giảm dần",
            ],
        )
        sort_entry_filter.grid(row=1, column=1, padx=(5, 10), pady=10, sticky=tk.W)

        price_label_filter = ttk.Label(filter_product_frame, text="Giá:")
        price_label_filter.grid(row=0, column=3, sticky=tk.E)
        price_entry_filter = ttk.Combobox(
            filter_product_frame,
            values=["<  50 000", "< 100 000", "< 200 000", ">=200 000"],
        )
        price_entry_filter.grid(row=0, column=4, padx=(5, 10), pady=10, sticky=tk.W)

        status_label_filter = ttk.Label(filter_product_frame, text="Trạng thái:")
        status_label_filter.grid(row=0, column=5, sticky=tk.E)
        status_entry_filter = ttk.Combobox(
            filter_product_frame, values=["Còn hàng", "Hết hàng"]
        )
        status_entry_filter.grid(row=0, column=6, padx=(5, 10), pady=10, sticky=tk.W)

        list_product_frame = tk.LabelFrame(
            frame2, font=("Time New Roman", 15, "bold"), text="Danh sách sản phẩm"
        )
        list_product_frame.pack(fill="both", expand=True, padx=20)

        list_products = ttk.Treeview(list_product_frame, style="mystyle.Treeview")

        # style list products
        style = ttk.Style()
        style.configure(
            "mystyle.Treeview",
            highlightthickness=0,
            bd=0,
            font=(None, 13),
            rowheight=30,
        )  # Modify the font of the body
        style.configure(
            "mystyle.Treeview.Heading", font=("Calibri", 14, "bold")
        )  # Modify the font of the headings

        verscrlbar = ttk.Scrollbar(
            list_product_frame, orient="vertical", command=list_products.yview
        )

        # scrollbar list product
        verscrlbar.pack(side="right", fill="y")

        # Configuring treeview
        list_products.configure(xscrollcommand=verscrlbar.set)

        list_products["columns"] = ["ID", "Tên sản phẩm", "Mô tả", "Giá", "Tồn kho"]
        list_products.column("#0", width=0, stretch=tk.NO)
        list_products.column(
            "ID",
            width=70,
            anchor="w",
        )
        list_products.column(
            "Tên sản phẩm",
            width=200,
            minwidth=15,
            anchor="w",
        )
        list_products.column(
            "Mô tả",
            width=260,
            minwidth=40,
            anchor="w",
        )
        list_products.column("Giá", width=80, anchor="e")
        list_products.column("Tồn kho", width=80, anchor="center")

        list_products.heading("#0", text="")
        list_products.heading("ID", text="ID", anchor="center")
        list_products.heading("Tên sản phẩm", text="Tên sản phẩm", anchor="center")
        list_products.heading("Mô tả", text="Mô tả", anchor="center")
        list_products.heading("Giá", text="Giá", anchor="center")
        list_products.heading("Tồn kho", text="Tồn kho", anchor="center")

        self.LoadProducts(list_products, self.qlsp.products)

        list_products.pack(expand=True, fill="both")

        info_product = tk.LabelFrame(
            frame3, font=("Time New Roman", 15, "bold"), text="Chi tiết sản phẩm"
        )
        info_product.pack(fill="both", expand=True, padx=20)
        info_product.columnconfigure((1, 3, 4), weight=1)
        info_product.columnconfigure((2, 5), weight=2)
        info_id_label = ttk.Label(info_product, text="ID", font=("Time New Roman", 12))
        info_id_label.grid(row=1, column=0, padx=(70, 20), pady=10, sticky="w")
        info_id_entry = tk.Text(
            info_product, height=1, width=20, font=("Time New Roman", 12)
        )
        info_id_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        info_name_label = ttk.Label(
            info_product, text="Tên", font=("Time New Roman", 12)
        )
        info_name_label.grid(row=0, column=0, padx=(70, 20), pady=10, sticky="w")
        info_name_entry = tk.Text(
            info_product, height=3, width=20, font=("Time New Roman", 12)
        )
        info_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        info_des_label = ttk.Label(
            info_product, text="Mô tả", font=("Time New Roman", 12)
        )
        info_des_label.grid(row=0, column=2, padx=20, pady=30, sticky="e")
        info_des_entry = tk.Text(
            info_product, height=4, width=20, font=("Time New Roman", 12)
        )
        info_des_entry.grid(row=0, column=3, padx=10, pady=10, sticky="w")
        info_price_label = ttk.Label(
            info_product, text="Giá", font=("Time New Roman", 12)
        )
        info_price_label.grid(row=1, column=2, padx=20, pady=10, sticky="e")
        info_price_entry = tk.Text(
            info_product, height=1, width=20, font=("Time New Roman", 12)
        )
        info_price_entry.grid(row=1, column=3, padx=10, pady=10, sticky="w")
        info_instock_label = ttk.Label(
            info_product, text="Tồn kho", font=("Time New Roman", 12)
        )
        info_instock_label.grid(row=2, column=0, padx=(70, 20), pady=10, sticky="w")
        info_instock_entry = tk.Text(
            info_product, height=1, width=20, font=("Time New Roman", 12)
        )
        info_instock_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        list_products.bind(
            "<ButtonRelease-1>",
            lambda event, lp=list_products, id=info_id_entry, name=info_name_entry, des=info_des_entry, price=info_price_entry, instock=info_instock_entry: self.selectItem(
                lp, id, name, des, price, instock
            ),
        )

        Insert_btn = ttk.Button(
            info_product,
            text="Thêm",
            command=lambda qlsp=self.qlsp, lp=list_products, id=info_id_entry, name=info_name_entry, des=info_des_entry, price=info_price_entry, instock=info_instock_entry: self.InsertBTN(
                qlsp, lp, id, name, des, price, instock
            ),
        )
        Insert_btn.grid(row=0, column=5, sticky="n", padx=20)
        Update_btn = ttk.Button(
            info_product,
            text="Sửa",
            command=lambda qlsp=self.qlsp, lp=list_products, id=info_id_entry, name=info_name_entry, des=info_des_entry, price=info_price_entry, instock=info_instock_entry: self.UpdateBTN(
                qlsp, lp, id, name, des, price, instock
            ),
        )
        Update_btn.grid(row=0, column=5)
        Delete_btn = ttk.Button(
            info_product,
            text="Xóa",
            command=lambda qlsp=self.qlsp, lp=list_products, id=info_id_entry: self.DeletetBTN(
                qlsp, lp, id
            ),
        )
        Delete_btn.grid(row=0, column=5, sticky="s")
        GetAPI_btn = ttk.Button(
            info_product,
            text="Get API",
            command=lambda lp=list_products, href="https://vudev1412.github.io/Apijson/sanpham.json": self.GetAPI(
                lp, href
            ),
        )
        GetAPI_btn.grid(row=1, column=5)
        Refresh_btn = ttk.Button(
            info_product,
            text="Refresh",
            command=lambda lp=list_products: self.Refresh(lp),
        )
        Refresh_btn.grid(row=2, column=5)
        find_button = ttk.Button(
            filter_product_frame,
            text="Tìm",
            command=lambda lp=list_products, pro=pro_entry_filter: self.Find_BTN(
                lp, pro
            ),
        )
        find_button.grid(row=0, column=2, sticky="w", padx=10, pady=10)
        filter_button = ttk.Button(
            filter_product_frame,
            text="Lọc",
            command=lambda lp=list_products, price=price_entry_filter, status=status_entry_filter: self.Filter_BTN(
                lp, price, status
            ),
        )
        filter_button.grid(row=0, column=7, sticky="w", padx=10, pady=10)
        sort_button = ttk.Button(
            filter_product_frame,
            text="Sắp xếp",
            command=lambda lp=list_products, se=sort_entry_filter: self.SortBTN(lp, se),
        )
        sort_button.grid(row=1, column=2, sticky="w", padx=10, pady=10)
        window.mainloop()

    def ManagePage2(self, window, title, size):
        self.TopLevelPage(window, title, size)
        menu_frame = tk.Frame(window)
        menu_frame.pack(fill="both")
        acc_label = tk.Label(
            menu_frame, text="Account", font=("Helvetica", 13), fg="gray"
        )
        acc_label.pack(anchor="w", padx=20)
        accmenu = tk.Menu(window, tearoff=0, font=("Helvetica", 13), fg="gray")
        accmenu.add_command(
            label="Info", command=lambda us=self.user: self.Info_BTN(us)
        )
        accmenu.add_command(
            label="Log Out", command=lambda win=self.ManageWin2: self.LogOut(win)
        )
        acc_label.bind("<Button-1>", lambda event: create_dropdown(event, accmenu))
        frame1 = tk.Frame(window)
        frame1.pack(fill="both")
        frame2 = tk.Frame(window)
        frame2.pack(fill="both", expand=True)
        frame3 = tk.Frame(window)
        frame3.pack(fill="both", pady=(0, 20))

        filter_product_frame = tk.LabelFrame(
            frame1, font=("Time New Roman", 15, "bold"), text="Lọc sản phẩm"
        )
        filter_product_frame.columnconfigure((0, 2, 3, 4, 6), weight=2)
        filter_product_frame.columnconfigure((1, 5, 7), weight=1)
        filter_product_frame.pack(fill="x", padx=20)

        pro_label_filter = ttk.Label(filter_product_frame, text="Sản phẩm:")
        pro_label_filter.grid(row=0, column=0, pady=10, padx=5, sticky=tk.E)
        pro_entry_filter = ttk.Entry(filter_product_frame)
        pro_entry_filter.grid(row=0, column=1, padx=(5, 10), pady=10, sticky=tk.W)
        sort_label_filter = ttk.Label(filter_product_frame, text="Sắp xếp theo:")
        sort_label_filter.grid(row=1, column=0, pady=10, padx=5, sticky=tk.E)
        sort_entry_filter = ttk.Combobox(
            filter_product_frame,
            values=[
                "Giá tăng dần",
                "Giá giảm dần",
                "Hàng tồn kho tăng dần",
                "Hàng tồn kho giảm dần",
            ],
        )
        sort_entry_filter.grid(row=1, column=1, padx=(5, 10), pady=10, sticky=tk.W)

        price_label_filter = ttk.Label(filter_product_frame, text="Giá:")
        price_label_filter.grid(row=0, column=3, sticky=tk.E)
        price_entry_filter = ttk.Combobox(
            filter_product_frame,
            values=["<  50 000", "< 100 000", "< 200 000", ">=200 000"],
        )
        price_entry_filter.grid(row=0, column=4, padx=(5, 10), pady=10, sticky=tk.W)

        status_label_filter = ttk.Label(filter_product_frame, text="Trạng thái:")
        status_label_filter.grid(row=0, column=5, sticky=tk.E)
        status_entry_filter = ttk.Combobox(
            filter_product_frame, values=["Còn hàng", "Hết hàng"]
        )
        status_entry_filter.grid(row=0, column=6, padx=(5, 10), pady=10, sticky=tk.W)

        list_product_frame = tk.LabelFrame(
            frame2, font=("Time New Roman", 15, "bold"), text="Danh sách sản phẩm"
        )
        list_product_frame.pack(fill="both", expand=True, padx=20)

        list_products = ttk.Treeview(list_product_frame, style="mystyle.Treeview")

        # style list products
        style = ttk.Style()
        style.configure(
            "mystyle.Treeview",
            highlightthickness=0,
            bd=0,
            font=(None, 13),
            rowheight=30,
        )  # Modify the font of the body
        style.configure(
            "mystyle.Treeview.Heading", font=("Calibri", 14, "bold")
        )  # Modify the font of the headings

        verscrlbar = ttk.Scrollbar(
            list_product_frame, orient="vertical", command=list_products.yview
        )

        # scrollbar list product
        verscrlbar.pack(
            side="right",
            fill="y",
        )

        # Configuring treeview
        list_products.configure(xscrollcommand=verscrlbar.set)

        list_products["columns"] = ["ID", "Tên sản phẩm", "Mô tả", "Giá", "Tồn kho"]
        list_products.column("#0", width=0, stretch=tk.NO)
        list_products.column(
            "ID",
            width=70,
            anchor="w",
        )
        list_products.column(
            "Tên sản phẩm",
            width=200,
            minwidth=15,
            anchor="w",
        )
        list_products.column(
            "Mô tả",
            width=260,
            minwidth=40,
            anchor="w",
        )
        list_products.column("Giá", width=80, anchor="e")
        list_products.column("Tồn kho", width=80, anchor="center")

        list_products.heading("#0", text="")
        list_products.heading("ID", text="ID", anchor="center")
        list_products.heading("Tên sản phẩm", text="Tên sản phẩm", anchor="center")
        list_products.heading("Mô tả", text="Mô tả", anchor="center")
        list_products.heading("Giá", text="Giá", anchor="center")
        list_products.heading("Tồn kho", text="Tồn kho", anchor="center")

        self.LoadProducts(list_products, self.qlsp.products)

        list_products.pack(expand=True, fill="both")

        info_product = tk.LabelFrame(
            frame3, font=("Time New Roman", 15, "bold"), text="Chi tiết sản phẩm"
        )
        info_product.pack(fill="both", expand=True, padx=20)
        info_product.columnconfigure((1, 3, 4), weight=1)
        info_product.columnconfigure((2, 5), weight=2)
        info_id_label = ttk.Label(info_product, text="ID", font=("Time New Roman", 12))
        info_id_label.grid(row=1, column=0, padx=(70, 20), pady=10, sticky="w")
        info_id_entry = tk.Text(
            info_product, height=1, width=20, font=("Time New Roman", 12)
        )
        info_id_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        info_name_label = ttk.Label(
            info_product, text="Tên", font=("Time New Roman", 12)
        )
        info_name_label.grid(row=0, column=0, padx=(70, 20), pady=10, sticky="w")
        info_name_entry = tk.Text(
            info_product, height=3, width=20, font=("Time New Roman", 12)
        )
        info_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        info_des_label = ttk.Label(
            info_product, text="Mô tả", font=("Time New Roman", 12)
        )
        info_des_label.grid(row=0, column=2, padx=20, pady=30, sticky="e")
        info_des_entry = tk.Text(
            info_product, height=4, width=20, font=("Time New Roman", 12)
        )
        info_des_entry.grid(row=0, column=3, padx=10, pady=10, sticky="w")
        info_price_label = ttk.Label(
            info_product, text="Giá", font=("Time New Roman", 12)
        )
        info_price_label.grid(row=1, column=2, padx=20, pady=10, sticky="e")
        info_price_entry = tk.Text(
            info_product, height=1, width=20, font=("Time New Roman", 12)
        )
        info_price_entry.grid(row=1, column=3, padx=10, pady=10, sticky="w")
        info_instock_label = ttk.Label(
            info_product, text="Tồn kho", font=("Time New Roman", 12)
        )
        info_instock_label.grid(row=2, column=0, padx=(70, 20), pady=10, sticky="w")
        info_instock_entry = tk.Text(
            info_product, height=1, width=20, font=("Time New Roman", 12)
        )
        info_instock_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        list_products.bind(
            "<ButtonRelease-1>",
            lambda event, lp=list_products, id=info_id_entry, name=info_name_entry, des=info_des_entry, price=info_price_entry, instock=info_instock_entry: self.selectItem(
                lp, id, name, des, price, instock
            ),
        )

        Refresh_btn = ttk.Button(
            info_product,
            text="Refresh",
            command=lambda lp=list_products: self.Refresh(lp),
        )
        Refresh_btn.grid(row=2, column=5)
        find_button = ttk.Button(
            filter_product_frame,
            text="Tìm",
            command=lambda lp=list_products, pro=pro_entry_filter: self.Find_BTN(
                lp, pro
            ),
        )
        find_button.grid(row=0, column=2, sticky="w", padx=10, pady=10)
        filter_button = ttk.Button(
            filter_product_frame,
            text="Lọc",
            command=lambda lp=list_products, price=price_entry_filter, status=status_entry_filter: self.Filter_BTN(
                lp, price, status
            ),
        )
        filter_button.grid(row=0, column=7, sticky="w", padx=10, pady=10)
        sort_button = ttk.Button(
            filter_product_frame,
            text="Sắp xếp",
            command=lambda lp=list_products, se=sort_entry_filter: self.SortBTN(lp, se),
        )
        sort_button.grid(row=1, column=2, sticky="w", padx=10, pady=10)
        window.mainloop()

    def Info_BTN(self, user):
        self.Info = tk.Toplevel(self.main)
        self.InfoPage(self.Info, "Thông tin tài khoản", (400, 600), user)

    def LogOut(self, window):
        res = mb.askyesno("Xác nhận", "Bạn có chắc chắn muốn đăng xuất?")
        if res:
            window.destroy()
            self.Login = tk.Toplevel(self.main)
            self.LoginPage(self.Login, "Đăng nhập", (400, 600))

    def LoginBTN(self, username, password):
        us = username.get().strip()
        pw = password.get().strip()
        if us == "" or pw == "":
            mb.showwarning("Cảnh báo", "Không được bỏ trống thông tin")
            return
        else:
            check = self.users.CheckUser(us, pw)
            if check == 0:
                mb.showinfo("Thông báo", "Sai tên đăng nhập hoặc mật khẩu")
            else:
                mb.showinfo("Thông báo", "Đăng nhập thành công")
                if check["level"] == "Level 1":
                    self.user = check
                    self.Login.destroy()
                    self.ManageWin = tk.Toplevel(self.main)
                    self.ManagePage(self.ManageWin, "Quản lý sản phẩm", (850, 800))

                else:
                    self.user = check
                    self.Login.destroy()
                    self.ManageWin2 = tk.Toplevel(self.main)
                    self.ManagePage2(self.ManageWin2, "Quản lý sản phẩm", (850, 800))

    def RegisterBTN(self, username, email, password, repassword, level):
        us = username.get()
        e = email.get()
        pw = password.get()
        repw = repassword.get()
        lv = level.get()
        if us == "" or e == "" or pw == "" or repw == "" or lv == "":
            mb.showwarning("Cảnh báo", "Vui lòng điền đầy đủ thông tin")
            return
        newuser = User(us, e, pw, lv).DictUser()
        check = self.users.Add(newuser, repw)
        if check == 0:
            mb.showwarning(
                "Cảnh báo",
                "Mật khẩu phải có ít nhất 8 kí tự bao gồm chữ cái viết thường, viết hoa, chữ số, kí tự đặc biệt",
            )
        elif check == -1:
            mb.showwarning("Cảnh báo", "Nhập lại mật khẩu không đúng")
        elif check == -2:
            mb.showwarning("Cảnh báo", "Sai định dạng email")
        elif check == -3:
            mb.showwarning("Cảnh báo", "Vui lòng chọn đúng level")
        elif check == -4:
            mb.showwarning("Cảnh báo", "username này đã tồn tại")
        elif check == -5:
            mb.showwarning("Cảnh báo", "email này đã được đăng kí")
        else:
            mb.showinfo("Thông báo", "Tài khoản đã được đăng kí thành công")
            self.Register.destroy()
            self.Login = tk.Toplevel(self.main)
            self.LoginPage(self.Login, "Đăng nhập", (400, 600))

    def SortBTN(self, list_products, sort_entry):
        mode = sort_entry.get()
        if mode == "":
            mb.showwarning("Cảnh báo", "Vui lòng chọn điều kiện sắp xếp")
            return
        if (
            mode != "Giá tăng dần"
            and mode != "Giá giảm dần"
            and mode != "Hàng tồn kho tăng dần"
            and mode != "Hàng tồn kho giảm dần"
        ):
            mb.showwarning("Cảnh báo", "Vui lòng chọn điều kiện trong trường")
            return
        self.ClearProducts(list_products)
        sorted_list = self.qlsp.Sort(mode)
        self.LoadProducts(list_products, sorted_list)

    def Find_BTN(self, list_products, pro_entry_filter):
        pro = pro_entry_filter.get()

        if pro != "":
            pro = pro.lower()
            self.ClearProducts(list_products)
            for product in self.qlsp.products:
                if pro in product["id"].lower() or pro in product["name"].lower():

                    value = list(product.values())
                    list_products.insert("", index="end", values=value)

        else:
            mb.showwarning("Cảnh báo", "Vui lòng nhập ID để tìm sản phẩm")

    def Filter_BTN(self, list_products, price_entry_filter, status_entry_filter):
        price = price_entry_filter.get()
        status = status_entry_filter.get()
        if price == "" or status == "":
            mb.showwarning("Cảnh báo", "Chọn giá và trạng thái để lọc")
            return 0
        self.ClearProducts(list_products)
        for product in self.qlsp.products:
            if status == "Hết hàng":
                if price == "<  50 000":
                    if product["in_stock"] < 1 and product["price"] < 50000:
                        value = list(product.values())
                        list_products.insert("", index="end", values=value)
                elif price == "< 100 000":
                    if product["in_stock"] < 1 and product["price"] < 100000:
                        value = list(product.values())
                        list_products.insert("", index="end", values=value)
                elif price == "< 200 000":
                    if product["in_stock"] < 1 and product["price"] < 200000:
                        value = list(product.values())
                        list_products.insert("", index="end", values=value)
                else:
                    if product["in_stock"] < 1 and product["price"] >= 200000:
                        value = list(product.values())
                        list_products.insert("", index="end", values=value)

            elif status == "Còn hàng":
                if price == "<  50 000":
                    if product["in_stock"] > 0 and product["price"] < 50000:
                        value = list(product.values())
                        list_products.insert("", index="end", values=value)
                elif price == "< 100 000":
                    if product["in_stock"] > 0 and product["price"] < 100000:
                        value = list(product.values())
                        list_products.insert("", index="end", values=value)
                elif price == "< 200 000":
                    if product["in_stock"] > 0 and product["price"] < 200000:
                        value = list(product.values())
                        list_products.insert("", index="end", values=value)
                else:
                    if product["in_stock"] > 0 and product["price"] >= 200000:
                        value = list(product.values())
                        list_products.insert("", index="end", values=value)

    def selectItem(
        self,
        list_products,
        info_id_entry,
        info_name_entry,
        info_des_entry,
        info_price_entry,
        info_instock_entry,
    ):
        try:
            curItem = list_products.focus()
            values_product = list(list_products.item(curItem).values())
            info_id_entry.delete(1.0, tk.END)
            info_id_entry.insert(tk.END, values_product[2][0])
            info_name_entry.delete(1.0, tk.END)
            info_name_entry.insert(tk.END, values_product[2][1])
            info_des_entry.delete(1.0, tk.END)
            info_des_entry.insert(tk.END, values_product[2][2])
            info_price_entry.delete(1.0, tk.END)
            info_price_entry.insert(tk.END, values_product[2][3])
            info_instock_entry.delete(1.0, tk.END)
            info_instock_entry.insert(tk.END, values_product[2][4])
        except:
            pass

    def InsertBTN(
        self,
        qlsp,
        list_products,
        info_id_entry,
        info_name_entry,
        info_des_entry,
        info_price_entry,
        info_instock_entry,
    ):
        id = info_id_entry.get("1.0", tk.END).strip()
        name = info_name_entry.get("1.0", tk.END).strip()
        des = info_des_entry.get("1.0", tk.END).strip()
        price = info_price_entry.get("1.0", tk.END).strip()
        instock = info_instock_entry.get("1.0", tk.END).strip()
        if id == "" or name == "" or des == "" or price == "" or instock == "":
            mb.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin")
            return 0
        try:
            price = int(price)
        except ValueError:
            mb.showwarning("Cảnh báo", "Giá tiền phải là chữ số")
        try:
            instock = int(instock)
        except ValueError:
            mb.showwarning("Cảnh báo", "Tồn kho phải là chữ số")
        if not id.startswith("SP"):
            mb.showwarning("Cảnh báo", "Mã sản phẩm phải bắt đầu bằng 'SP'")
        p = Product(id, name, des, price, instock).DictPro()
        check = qlsp.Add(p)
        if check == 0:
            mb.showerror("Lỗi", "Id sản phẩm này đã tồn tại trong danh sách")
        elif check == -1:
            mb.showerror("Lỗi", "Giá tiền sản phẩm phải lớn hơn 0")
        elif check == -2:
            mb.showerror("Lỗi", "Hàng tồn kho từ 0 trở lên")
        elif check == -3:
            mb.showerror("Lỗi", "Tên sản phẩm đã tồn tại trong danh sách")
        else:
            mb.showinfo("Thông báo", "Đã thêm thành công")
            self.Refresh(list_products)

    def DeletetBTN(self, qlsp, list_products, info_id_entry):
        id = info_id_entry.get("1.0", tk.END).strip()
        if id == "":
            mb.showwarning("Cảnh báo", "Vui lòng nhập mã sản phẩm")
        answer = mb.askyesno(
            title="Xác nhận", message=f"Bạn có chắc chắn muốn xóa sản phẩm mã {id}?"
        )
        if answer:
            check = qlsp.Delete(id)
        if check == 0:
            mb.showerror("Lỗi", f"Không có mã sản phẩm {id} trong danh sách")
        else:
            self.Refresh(list_products)
            mb.showinfo("Thông báo", f"Đã xóa sản phẩm có mã {id} thành công")

    def UpdateBTN(
        self,
        qlsp,
        list_products,
        info_id_entry,
        info_name_entry,
        info_des_entry,
        info_price_entry,
        info_instock_entry,
    ):
        curItem = list_products.focus()
        values_product = list(list_products.item(curItem).values())
        try:
            old_id = values_product[2][0]
        except:
            mb.showwarning("Cảnh báo", "Vui lòng chọn sản phẩm cần sửa")
            return 0
        id = info_id_entry.get("1.0", tk.END).strip()
        name = info_name_entry.get("1.0", tk.END).strip()
        des = info_des_entry.get("1.0", tk.END).strip()
        price = info_price_entry.get("1.0", tk.END).strip()
        instock = info_instock_entry.get("1.0", tk.END).strip()
        if id == "" or name == "" or des == "" or price == "" or instock == "":
            mb.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin")
            return 0
        try:
            price = int(price)
        except ValueError:
            mb.showwarning("Cảnh báo", "Giá tiền phải là chữ số")
        try:
            instock = int(instock)
        except ValueError:
            mb.showwarning("Cảnh báo", "Tồn kho phải là chữ số")
        if not id.startswith("SP"):
            mb.showwarning("Cảnh báo", "Mã sản phẩm phải bắt đầu bằng 'SP'")
            return 0
        p = Product(id, name, des, price, instock).DictPro()
        check = qlsp.Update(old_id, p)
        if check == 0:
            mb.showerror("Lỗi", f"Mã sản phẩm {old_id} không có trong danh sách")
        elif check == -1:
            mb.showerror("Lỗi", "Giá tiền sản phẩm phải lớn hơn 0")
        elif check == -2:
            mb.showerror("Lỗi", "Hàng tồn kho từ 0 trở lên")
        elif check == -3:
            mb.showerror("Lỗi", "Tên sản phẩm đã tồn tại trong danh sách")
        elif check == -4:
            mb.showerror("Lỗi", "Id sản phẩm đã tồn tại")
        else:
            mb.showinfo("Thông báo", "Đã sửa thành công")
            self.Refresh(list_products)

    def LoadProducts(self, list_products, qlsp_products):
        if len(qlsp_products) != 0:
            for product in qlsp_products:
                value = list(product.values())
                list_products.insert("", index="end", values=value)

    def ClearProducts(self, list_products):
        for product in list_products.get_children():
            list_products.delete(product)

    def GetAPI(self, list_products, href):
        self.qlsp.getAPI(f"{href}")
        self.qlsp.Read()
        self.Refresh(list_products)
        mb.showinfo("Thông Báo", "Đã lấy API thành công")

    def Refresh(self, list_products):
        self.ClearProducts(list_products)
        self.LoadProducts(list_products, self.qlsp.products)


if __name__ == "__main__":
    a = App()
