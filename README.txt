1. File generate.py berfungsi untuk melakukan generate data
2. File filter1.py file untuk menampilkan data sesuai dengan ketentuan yg telah diberikan,
   kemudian hasilnya akan di export ke csv file.

Struktur data dari generate data
1. Id : object
2. device_id : object
3. username : object
4. lokasi : object
5. amount : uint32
6. timestamp : float64

File yang dihasilkan dari hasil generate di export ke file data.csv

File data.csv akan dibaca oleh file filter1.py untuk dilakukan seleksi data berdasarkan kriteria
yang telah ditentukan

Pada saat pembacaan data, data yang mempunya type object diubah terlebih dahulu menjadi data type category
agas bisa dilakukan grouping data.


