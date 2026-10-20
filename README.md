# 🧭 Pathfinding Algorithms Simulation & Visualization

Aplikasi simulasi dan visualisasi interaktif untuk algoritma pencarian rute berbasis **Python**, **NetworkX**, dan **Matplotlib**. Proyek ini mengimplementasikan 5 algoritma pencarian kecerdasan buatan (*Artificial Intelligence*) lengkap dengan visualisasi *graph* langkah demi langkah, pencatatan status *Frontier*, dan kalkulasi biaya perjalanan secara *real-time*.

---

## 🚀 Algoritma yang Diimplementasikan

| Algoritma | Jenis Pencarian | Fungsi Evaluasi | Keterangan |
| :--- | :--- | :--- | :--- |
| **BFS** *(Breadth-First Search)* | Uninformed | - | Mencari jalur dengan jumlah langkah (*edge*) tersingkat. |
| **DFS** *(Depth-First Search)* | Uninformed | - | Menelusuri cabang hingga kedalaman maksimal (*backtracking*). |
| **UCS** *(Uniform Cost Search)* | Uninformed | $g(n)$ | Menjamin rute dengan total biaya (*cost*) aktual paling murah. |
| **Greedy** *(Best-First Search)* | Informed | $h(n)$ | Memilih *node* berdasarkan estimasi jarak terdekat ke Goal. |
| **A\* Search** *(A-Star)* | Informed | $f(n) = g(n) + h(n)$ | Menggabungkan biaya aktual dan heuristik untuk rute paling optimal. |

---

## 📌 Aturan Penelusuran (Searching Rules)

Seluruh algoritma dalam proyek ini mematuhi 4 aturan dasar pencarian berikut:
1. **Prioritas Terkecil:** Selalu memilih kandidat dengan nilai evaluasi/prioritas paling kecil dari *Frontier*.
2. **Aturan Abjad (Tie-Breaking):** Jika terdapat nilai prioritas yang sama, kandidat dipilih berdasarkan urutan alfabet (A ke Z).
3. **Pemeriksaan Goal:** Pemeriksaan titik tujuan (*Goal*) dilakukan saat kandidat diekstrak dari *Frontier* (bukan saat pertama kali dimasukkan).
4. **Pembaruan A\*:** Pada algoritma $A^*$, nilai $g(n)$ dan *parent* diperbarui jika ditemukan rute baru yang lebih murah ke *node* tersebut.

> 💡 **Heuristik:** Fungsi $h(n)$ pada algoritma *Greedy* dan $A^*$ dihitung secara otomatis menggunakan **Manhattan Distance**:
> $$h(n) = \vert{}x_G - x_n\vert{} + \vert{}y_G - y_n\vert{}$$

---

## 🗺️ Peta Graf & Koordinat Grid

```text
==================================================
      PETA RUTE GRID DI TERMINAL (ASCII ART)      
==================================================
             (Bobot 1)    (Bobot 2)     (Bobot 4) 
           .-----> [A] --------> [C] --------.    
          /                                   \   
 Start  [S]                                   [G] Goal 
          \                                   /   
           '-----> [B] --> [D] --> [E] ------'    
             (1)       (1)     (1)      (1)       
==================================================

**Titik Koordinat $(X, Y)$ Node:**

`S(0,1)`, `A(1,2)`, `B(1,0)`, `C(2,2)`, `D(2,0)`, `E(3,0)`, `G(4,1)`

---

## 📊 Ringkasan Hasil Perbandingan

| Parameter | BFS | DFS | UCS | Greedy | A* Search |
| --- | --- | --- | --- | --- | --- |
| **Rute Ditemukan** | `S->A->C->G` | `S->A->C->G` | `S->B->D->E->G` | `S->A->C->G` | `S->B->D->E->G` |
| **Total Langkah** | 3 | 3 | 4 | 3 | 4 |
| **Total Biaya Aktual $g(n)$** | 7 | 7 | **4** | 7 | **4** |
| **Struktur Data Utama** | Queue (FIFO) | Stack (LIFO) | Priority Queue | Priority Queue | Priority Queue |
| **Sifat Optimalitas** | Langkah | Tidak | Biaya | Tidak | **Langkah & Biaya** |

---

## 🛠️ Prasyarat & Instalasi

Pastikan Python 3.x sudah terinstal di komputer Anda.

1. **Clone atau Unduh Repositori Ini:**
```bash
git clone [https://github.com/username/pathfinding-simulation.git](https://github.com/username/pathfinding-simulation.git)
cd pathfinding-simulation

```


2. **Instal Library yang Dibutuhkan:**
```bash
pip install networkx matplotlib

```



---

## 🎮 Cara Menjalankan Program

Jalankan skrip Python untuk algoritma yang ingin disimulasikan:

```bash
# Menjalankan BFS
python bfs_search.py

# Menjalankan DFS
python dfs_search.py

# Menjalankan UCS
python ucs_search.py

# Menjalankan Greedy Best-First Search
python greedy_search.py

# Menjalankan A* Search
python astar_search.py

```

Setiap eksekusi program akan menampilkan:

1. Peta ASCII art di terminal.
2. Log eksekusi *step-by-step* (proses evaluasi, status *Frontier*, dan biaya).
3. Visualisasi interaktif grafik *Matplotlib* dan otomatis menyimpan tangkapan layar gambar hasil (.png).

---

## 📁 Struktur Repositori

```text
├── bfs_search.py         # Kode simulasi Breadth-First Search
├── dfs_search.py         # Kode simulasi Depth-First Search
├── ucs_search.py         # Kode simulasi Uniform Cost Search
├── greedy_search.py      # Kode simulasi Greedy Best-First Search
├── astar_search.py       # Kode simulasi A* Search
└── README.md             # Dokumentasi proyek

```

---

## 📝 Lisensi

Proyek ini dibuat untuk keperluan akademik dan tugas mata kuliah Kecerdasan Buatan (AI). Bebas digunakan dan dimodifikasi untuk tujuan pembelajaran.

```

```
