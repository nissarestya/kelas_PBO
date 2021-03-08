class student():
    
    def nama(self):
        print("Nama   :", self.full_name)
    def get_age (self):
        print("Usia   :", self.age)
    def get_alamat (self):
        print("Alamat :", self.alamat)
    def get_status (self):
        print("Status :", self.status)
nissa = student()

nissa.full_name = "Nissa Restyasari"
nissa.age = "20"
nissa.alamat = "Cimahi"
nissa.status = "Mahasiswa"

nissa.nama()
nissa.get_age()
nissa.get_alamat()
nissa.get_status()