from tabulate import tabulate

class User:
    data_user = {
        1: ["Rosy", "Basic Plan", 12, "rosy-123"],
        2: ["Anton", "Standard Plan", 9, "anton-123"],
        3: ["Agus", "Basic Plan", 1, "agus-123"],
        4: ["Budi", "Premium Plan", 5, "budi-123"],
        5: ["Shania", "Basic Plan", 6, "shania-123"]
    }

    list_plan = ["Basic Plan", "Standard Plan", "Premium Plan"]
    list_benefit = [
        [True, True, True, "Bisa Stream"],
        [True, True, True, "Bisa Download"],
        [True, True, True, "Kualitas SD"],
        [False, True, True, "Kualitas HD"],
        [False, False, True, "Kualitas UHD"],
        [1, 2, 4, "Number of Devices"],
        ["3rd party Movie only", "Basic Plan Content + Sports", "Basic Plan + Standard Plan + PacFlix Original Series", "Jenis Konten"],
        [120_000, 160_000, 200_000, "Harga"]
    ]
    headers = ["Basic Plan", "Standard Plan", "Premium Plan", "Services"]

    def __init__(self, username):
        self.username = username
        self.curent_plan = None
        self.duration_plan = None
        self.kode_referral = None

        for key, value in self.data_user.items():
            if value[0] == self.username:
                self.current_plan = value[1]
                self.duration_plan = value[2]
                self.current_plan = value[3]
                break

    def check_all_plan(self):
        """
        Fungsi ini digunakan untuk mencetak plan dan benefit
        
        input: None
        """
        print("List Benefit and Plan from Pacflix")
        print("")
        print(tabulate(self.list_benefit, self.headers))