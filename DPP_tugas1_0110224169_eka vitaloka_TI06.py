#input nama, divisi, agama, dan jabatan
nama_pegawai = input("masukan nama pegawai\t: ")
divisi = input("masukan divisi\t\t: ")
agama = input("masukan agama\t\t: ") .lower()
jabatan = input("masukan jabatan\t\t: ") .lower()

#Gaji pokok berdasarkan jabatan
if jabatan == "staff": 
    gaji_pokok = 4000000
elif jabatan == "kabag":
    gaji_pokok = 7000000
elif jabatan == "manager":
    gaji_pokok = 10000000
else:
    gaji_pokok = 0    

    #Tunjangan jabatan berdasarkan gaji pokok
tunjangan_jabatan = 0.2 * gaji_pokok #20% dari gaji pokok

#Gaji kotor hasil penjumlahan dari gaji pokok dan tunjangan 
gaji_kotor = gaji_pokok + tunjangan_jabatan

#zakat berdasarkan 2,5% gaji kotor
zakat = 0.025 * gaji_kotor if agama == "islam" and gaji_kotor >=7000000 else 0 #2,5% dari gaji kotor

#gaji bersih hasil pengurangan gaji kotor dengan zakat
gaji_bersih = gaji_kotor - zakat

#Output
print("\nNama Pegawai\t\t: %s"
      "\nAgama\t\t\t: %s"
      "\nDivisi\t\t\t: %s"
      "\nJabatan\t\t\t: %s"
      "\nGaji Pokok\t\t: Rp %.2f"
      "\nTunjangan Jabatan\t: Rp. %.2f"
      "\nGaji Kotor\t\t: Rp. %.2f"
      "\nZakat\t\t\t: Rp. %.2f"
      "\nGaji Bersih\t\t: %.2f"
      %(nama_pegawai, agama, divisi, jabatan, gaji_pokok, tunjangan_jabatan, gaji_kotor, zakat, gaji_bersih))
