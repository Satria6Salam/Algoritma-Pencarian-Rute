🗺️ Pathfinding Search Algorithms Visualizer

Simulasi & Visualisasi Algoritma Pencarian Rute (BFS, DFS, UCS, Greedy, A)*

📌 Daftar Isi

Tentang Proyek

Aturan Penelusuran (Search Rules)

Representasi Graf & Peta

Algoritma yang Diimplementasikan

Tabel Perbandingan Hasil

Panduan Instalasi & Penggunaan

Struktur Proyek

Lisensi

📖 Tentang Proyek

Proyek ini bertujuan untuk mensimulasikan, membandingkan, dan memvisualisasikan performa 5 algoritma pencarian rute populer dalam ranah kecerdasan buatan (Uninformed dan Informed Search).

Setiap eksekusi algoritma akan menghasilkan:

Log Terminal Rinci: Menampilkan tahapan evaluasi node, biaya kumulatif, dan isi Frontier pada setiap step.

Visualisasi Gambar Grafik (PNG): Gambar graf otomatis disimpan pada setiap tahap eksekusi menggunakan NetworkX dan Matplotlib.

Peta ASCII Art: Ditampilkan di terminal sebagai referensi visual awal.

🎯 Aturan Penelusuran (Search Rules)

Seluruh algoritma yang dikembangkan mematuhi 4 aturan dasar pencarian berikut:

🥇 Prioritas Terkecil: Pilih kandidat dengan nilai prioritas paling kecil ($f(n)$, $g(n)$, atau $h(n)$).

🔤 Tie-Breaking Abjad: Jika terdapat nilai prioritas yang sama, pilih node berdasarkan urutan abjad/alfabet (A-Z).

🏁 Goal Test saat Ekstraksi: Pemeriksaan titik tujuan (Goal Check) dilakukan setelah kandidat diekstrak dari Frontier, bukan saat dimasukkan.

🔄 Update $g(n)$ & Parent: Khusus untuk $A^*$, perbarui nilai $g(n)$ dan parent node jika ditemukan jalur baru yang lebih murah.

🗺️ Representasi Graf & Peta

Graf rute terdiri dari 7 node (S hingga G) dengan bobot ruas jalan (edge weights) dan koordinat posisi $(X, Y)$ sebagai berikut:

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


📏 Rumus Heuristik: Manhattan Distance

Untuk algoritma Informed Search (Greedy & $A^*$), fungsi heuristik dihitung secara dinamis terhadap Goal $G(4,1)$:

$$h(n) = \vert{}x_G - x_n\vert{} + \vert{}y_G - y_n\vert{}$$

Node $n$

Koordinat $(X, Y)$

$h(n)$ Ke Goal $G(4,1)$

S

$(0, 1)$

$\vert{}4-0\vert{} + \vert{}1-1\vert{} = \mathbf{4}$

A

$(1, 2)$

$\vert{}4-1\vert{} + \vert{}1-2\vert{} = \mathbf{4}$

B

$(1, 0)$

$\vert{}4-1\vert{} + \vert{}1-0\vert{} = \mathbf{4}$

C

$(2, 2)$

$\vert{}4-2\vert{} + \vert{}1-2\vert{} = \mathbf{3}$

D

$(2, 0)$

$\vert{}4-2\vert{} + \vert{}1-0\vert{} = \mathbf{3}$

E

$(3, 0)$

$\vert{}4-3\vert{} + \vert{}1-0\vert{} = \mathbf{2}$

G

$(4, 1)$

$\vert{}4-4\vert{} + \vert{}1-1\vert{} = \mathbf{0}$

🚀 Algoritma yang Diimplementasikan

1. 🔵 Breadth-First Search (BFS)

Struktur Data: Queue (FIFO)

Fokus: Menjelajah secara melebar level demi level untuk mencari jumlah langkah (edge) tersingkat.

2. 🟢 Depth-First Search (DFS)

Struktur Data: Stack (LIFO)

Fokus: Menjelajah sedalam mungkin pada satu cabang sebelum melakukan backtracking.

3. 🟡 Uniform Cost Search (UCS)

Struktur Data: Priority Queue (Berdasarkan $g(n)$)

Fokus: Mengeksplorasi rute berdasarkan total akumulasi biaya termurah dari titik awal.

4. 🟠 Greedy Best-First Search

Struktur Data: Priority Queue (Berdasarkan $h(n)$)

Fokus: Memilih langkah yang 'terlihat' paling dekat dengan Goal berdasarkan nilai heuristik.

5. 🟣 A* (A-Star) Search

Struktur Data: Priority Queue (Berdasarkan $f(n) = g(n) + h(n)$)

Fokus: Menggabungkan biaya aktual $g(n)$ dan perkiraan heuristik $h(n)$ untuk menjamin pencarian yang optimal dan efisien.

📊 Tabel Perbandingan Hasil

Algoritma

Rute Ditemukan

Total Langkah

Biaya Aktual ($g$)

Optimal?

Complete?

BFS

S -> A -> C -> G

3

7

❌

✅

DFS

S -> A -> C -> G

3

7

❌

❌

UCS

S -> B -> D -> E -> G

4

4

✅

✅

Greedy BFS

S -> A -> C -> G

3

7

❌

❌

A Search*

S -> B -> D -> E -> G

4

4

✅

✅

💻 Panduan Instalasi & Penggunaan

Prerequisites

Pastikan Python versi 3.10 atau lebih baru sudah terinstal di komputer Anda.

1. Clone & Setup Repository

git clone https://github.com/username/pathfinding-ai-simulation.git
cd pathfinding-ai-simulation


2. Install Dependency

Instal pustaka pustaka pendukung networkx dan matplotlib:

pip install networkx matplotlib


3. Jalankan Program

Jalankan skrip algoritma yang ingin Anda simulasikan:

# Menjalankan BFS
python bfs_search.py

# Menjalankan DFS
python dfs_search.py

# Menjalankan UCS
python ucs_search.py

# Menjalankan Greedy Best-First
python greedy_search.py

# Menjalankan A* Search
python astar_search.py


📁 Struktur Proyek

├── src/
│   ├── bfs_search.py        # Implementation of BFS Algorithm
│   ├── dfs_search.py        # Implementation of DFS Algorithm
│   ├── ucs_search.py        # Implementation of UCS Algorithm
│   ├── greedy_search.py     # Implementation of Greedy Best-First
│   └── astar_search.py      # Implementation of A* Search
└── README.md                # Project documentation


📜 Lisensi

Proyek ini dibuat untuk keperluan akademik dan didistribusikan di bawah MIT License. Silakan gunakan dan kembangkan kodenya secara bebas.
