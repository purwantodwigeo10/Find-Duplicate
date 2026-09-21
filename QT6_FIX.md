# Find Duplicate 26.1.0

Revisi atas paket 26.1.1: perbaiki dua temuan QVariant.Type di qt_compat.py.
Perbaikan dari 26.1.1 tetap disertakan.

Perubahan:
- Gunakan enum berkelompok untuk WindowType, AlignmentFlag, TextFormat,
  AspectRatioMode, TransformationMode, ItemFlag dan CheckState.
- Gunakan QNetworkRequest.KnownHeaders dan QNetworkReply.NetworkError.
- Gunakan exec() untuk dialog dan event loop.
- QAction diimpor dari QtGui pada Qt6, dengan dukungan QtWidgets pada Qt5.
- Pilih tipe field QMetaType pada Qt6 dan QVariant.String dan QVariant.Int pada Qt5.
- Gunakan writeAsVectorFormatV3 dan QgsVectorFileWriter.WriterError.NoError.
- Nomor versi metadata dan klien aktivasi menjadi 26.1.0.

Validasi: sintaks semua berkas Python, tidak ada akses QVariant.Type, dan
integritas ZIP. Dua lokasi yang dilaporkan pengguna telah diperbaiki. Pemeriksa resmi server QGIS belum dijalankan terhadap ZIP ini.
Runtime QGIS/Qt5/Qt6 tidak tersedia di lingkungan pengeditan; hasil GUI,
aktivasi dan Shapefile masih perlu diuji langsung. Metadata maksimum QGIS
3.99 dipertahankan, experimental=True; belum mengklaim dukungan QGIS 4 penuh.

Langkah pengguna:
1. Install ZIP 26.1.0 melalui Plugins > Manage and Install Plugins > Install from ZIP.
2. Restart QGIS.
3. Uji membuka dialog utama, Manage Activation, centang/pilih field dan ekspor.
4. Gunakan sample_data/parcels.geojson: key parcel_id. Harus ada dua A-001
   dengan frekuensi 2, dan satu B-002 dengan frekuensi 1.
5. Unggah isi folder find_duplicate_fd ke lokasi source plugin yang sama di
   repository GitHub Find-Duplicate; jangan menumpuk folder tambahan.
6. Unggah ZIP baru sebagai versi 26.1.0 pada plugin Find Duplicate di situs QGIS.
7. Periksa laporan Qt6 versi baru. Laporan versi 26.1.0 tidak berubah dengan
   mengedit GitHub saja. Jika masih ada temuan, kirim laporan versi 26.1.0.

Nomor versi dipertahankan 26.1.0 atas permintaan pengguna. Jika versi ini
sudah terdaftar di situs QGIS, jangan menganggap unggahan baru otomatis
menggantikan paket lama. Periksa opsi pengelolaan versi di situs.
