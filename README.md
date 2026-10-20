```markdown
# 🧭 Pathfinding Algorithms Simulation & Visualization

Aplikasi simulasi dan visualisasi interaktif 5 algoritma pencarian rute menggunakan **Python**, **NetworkX**, dan **Matplotlib**.

---

## 🚀 Algoritma yang Diimplementasikan

<table>
  <thead>
    <tr>
      <th>Algoritma</th>
      <th>Jenis</th>
      <th>Fungsi Evaluasi</th>
      <th>Keterangan</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>BFS</b> (Breadth-First Search)</td>
      <td>Uninformed</td>
      <td>-</td>
      <td>Mencari rute dengan jumlah langkah tersingkat.</td>
    </tr>
    <tr>
      <td><b>DFS</b> (Depth-First Search)</td>
      <td>Uninformed</td>
      <td>-</td>
      <td>Menelusuri cabang hingga kedalaman maksimal.</td>
    </tr>
    <tr>
      <td><b>UCS</b> (Uniform Cost Search)</td>
      <td>Uninformed</td>
      <td><code>g(n)</code></td>
      <td>Menjamin rute dengan total biaya aktual termurah.</td>
    </tr>
    <tr>
      <td><b>Greedy</b> Best-First Search</td>
      <td>Informed</td>
      <td><code>h(n)</code></td>
      <td>Memilih node berdasarkan estimasi jarak terdekat ke Goal.</td>
    </tr>
    <tr>
      <td><b>A* Search</b> (A-Star)</td>
      <td>Informed</td>
      <td><code>f(n) = g(n) + h(n)</code></td>
      <td>Menggabungkan biaya aktual dan heuristik untuk rute optimal.</td>
    </tr>
  </tbody>
</table>

---

## 📌 Aturan Penelusuran (Searching Rules)

1. **Prioritas Terkecil:** Selalu memilih kandidat dengan nilai evaluasi/prioritas paling kecil dari Frontier.
2. **Aturan Abjad (Tie-Breaking):** Jika terdapat nilai prioritas yang sama, kandidat dipilih berdasarkan urutan alfabet (A ke Z).
3. **Pemeriksaan Goal:** Pemeriksaan titik tujuan (Goal) dilakukan saat kandidat diekstrak dari Frontier.
4. **Pembaruan A*:** Pada algoritma A*, nilai `g(n)` dan parent diperbarui jika ditemukan rute baru yang lebih murah.

> 💡 **Rumus Heuristik Manhattan Distance:**  
> `h(n) = |xG - xn| + |yG - yn|`

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

```

**Koordinat Node:** `S(0,1)`, `A(1,2)`, `B(1,0)`, `C(2,2)`, `D(2,0)`, `E(3,0)`, `G(4,1)`

---

## 📊 Ringkasan Hasil Perbandingan

---

## 🎮 Cara Menjalankan Program

Instalasi pustaka prasyarat:

```bash
pip install networkx matplotlib

```

Menjalankan skrip Python:

```bash
python astar_search.py

```

```

```
