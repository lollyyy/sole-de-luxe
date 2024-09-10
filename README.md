# Tugas 2: Implementasi Model-View-Template (MVT) pada Django
Link applikasi PWS: http://aliya-zahira-soledeluxe.pbp.cs.ui.ac.id

## Langkah-langkah pembuatan project
Berikut adalah beberapa langkah-langkah yang saya lakukan untuk membuat project ini
- Melakukan instalasi python, django, dan github.
- Mengaktifkan virtual environment
- Menambahkan beberapa dependencies pada requirements dan juga melakukan instalasi requirements itu sendiri serta membuat projek Django
- Melakukan konfigurasi server dan menjalankan server itu sendiri lalu menonaktifkan server dan virtual environment
- Mengunggah projek ke github dengan melakukan command push
- Membuat project dan aplikasi dengan startapp serta mendaftarkan applikasi main ke dalam project
- Mengganti isian dari berkas models.py dengan atribut yang sesuai, setelah itu melakukan migrasi model
- Menambahkan data-data yang diperlukan pada berkas views.py
- Membuat berkas main.html yang berisi kustomisasi tampilan sesuai yang diinginkan, lalu membuat konfigurasi routing URL
- Melakukan pembaruan/update pada github dan melakukan deployment hasil ke PWS

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Flow Diagram](diagram.jpeg)
- urls.py: untuk menerima request yang sesuai dan menghubungkan pola request tersebut ke views
- template: menyusun tampilan akhir dari aplikasi
- views.py: mengelola logika dari aplikasi
- models.py: berisi skema yang telah dimodifikasi tentang data

## Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git membantu programmer melacak perubahan basis kode, sehingga dapat memudahkan programmer dalam mengelola dan berkolaborasi dalam pembuatan project. Git membantu programmer untuk mengerjakan project yang sama secara bersamaan. Selain itu, git juga sangat membantu dalam pengembangan program karena menyediakan riwayat perubahan dan memungkinkan programmer uuntuk melakukan pengembalian project ke versi sebelumnya.

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django dipilih karena kelengkapan fitur yang dimiliki karena Django telah menyediakan banyak fitur bawaan yang dapat memudahkan pengembangan aplikasi. Selanjutnya, Django memiliki dokumentasi yang lengkap sehingga dapat membantu programmer pemula untuk mengatasi masalah dan belajar lebih cepat.

## Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut ORM (Object-Relational Mapping) karena ORM menghubungkan objek Python dengan tabel dalam database relasional. Dengan ORM, pengembang dapat berinteraksi dengan database menggunakan kode Python, menghindari penulisan SQL secara langsung, dan memungkinkan pengelolaan data yang efisien melalui pemetaan objek ke format tabel.