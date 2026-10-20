<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pathfinding Algorithms Simulation & Visualization</title>
    <style>
        :root {
            --primary: #2563eb;
            --primary-dark: #1d4ed8;
            --bg-body: #f8fafc;
            --bg-card: #ffffff;
            --text-main: #0f172a;
            --text-muted: #475569;
            --border: #e2e8f0;
            --code-bg: #0f172a;
            --code-text: #f8fafc;
            --accent: #10b981;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg-body);
            color: var(--text-main);
            line-height: 1.6;
            padding: 40px 20px;
        }

        .container {
            max-width: 920px;
            margin: 0 auto;
        }

        header {
            background: linear-gradient(135deg, #1e293b, #0f172a);
            color: #ffffff;
            padding: 40px;
            border-radius: 16px;
            margin-bottom: 32px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }

        header h1 {
            font-size: 2.2rem;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        header p {
            color: #94a3b8;
            font-size: 1.05rem;
        }

        .card {
            background-color: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 28px;
            margin-bottom: 28px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        }

        h2 {
            font-size: 1.4rem;
            color: var(--text-main);
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
            border-bottom: 2px solid var(--border);
            padding-bottom: 10px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 16px 0;
            font-size: 0.95rem;
        }

        th, td {
            padding: 12px 16px;
            text-align: left;
            border-bottom: 1px solid var(--border);
        }

        th {
            background-color: #f1f5f9;
            color: var(--text-main);
            font-weight: 600;
        }

        tr:hover {
            background-color: #f8fafc;
        }

        .badge {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: 600;
            text-transform: uppercase;
        }

        .badge-uninformed {
            background-color: #e0f2fe;
            color: #0369a1;
        }

        .badge-informed {
            background-color: #dcfce7;
            color: #15803d;
        }

        ol, ul {
            padding-left: 24px;
            margin-bottom: 16px;
        }

        li {
            margin-bottom: 8px;
        }

        pre {
            background-color: var(--code-bg);
            color: var(--code-text);
            padding: 18px;
            border-radius: 8px;
            overflow-x: auto;
            font-family: "Courier New", Courier, monospace;
            font-size: 0.9rem;
            margin: 16px 0;
            line-height: 1.5;
        }

        code {
            background-color: #f1f5f9;
            color: #0f172a;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: monospace;
            font-size: 0.9em;
        }

        pre code {
            background-color: transparent;
            color: inherit;
            padding: 0;
        }

        .formula-box {
            background-color: #eff6ff;
            border-left: 4px solid var(--primary);
            padding: 16px;
            border-radius: 0 8px 8px 0;
            margin: 16px 0;
            color: #1e40af;
        }

        footer {
            text-align: center;
            padding: 20px;
            color: var(--text-muted);
            font-size: 0.9rem;
        }
    </style>
</head>
<body>

<div class="container">

    <header>
        <h1>🧭 Pathfinding Algorithms Simulation</h1>
        <p>Aplikasi simulasi dan visualisasi interaktif 5 algoritma pencarian rute menggunakan Python, NetworkX, dan Matplotlib.</p>
    </header>

    <!-- SECTION 1: ALGORITMA -->
    <div class="card">
        <h2>🚀 Algoritma yang Diimplementasikan</h2>
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
                    <td><strong>BFS</strong> (Breadth-First Search)</td>
                    <td><span class="badge badge-uninformed">Uninformed</span></td>
                    <td>-</td>
                    <td>Mencari rute dengan jumlah langkah (edge) tersingkat.</td>
                </tr>
                <tr>
                    <td><strong>DFS</strong> (Depth-First Search)</td>
                    <td><span class="badge badge-uninformed">Uninformed</span></td>
                    <td>-</td>
                    <td>Menelusuri cabang hingga kedalaman maksimal (backtracking).</td>
                </tr>
                <tr>
                    <td><strong>UCS</strong> (Uniform Cost Search)</td>
                    <td><span class="badge badge-uninformed">Uninformed</span></td>
                    <td><code>g(n)</code></td>
                    <td>Menjamin rute dengan total biaya (cost) aktual paling murah.</td>
                </tr>
                <tr>
                    <td><strong>Greedy</strong> Best-First Search</td>
                    <td><span class="badge badge-informed">Informed</span></td>
                    <td><code>h(n)</code></td>
                    <td>Memilih node berdasarkan estimasi jarak terdekat ke Goal.</td>
                </tr>
                <tr>
                    <td><strong>A* Search</strong> (A-Star)</td>
                    <td><span class="badge badge-informed">Informed</span></td>
                    <td><code>f(n) = g(n) + h(n)</code></td>
                    <td>Menggabungkan biaya aktual dan heuristik untuk rute optimal.</td>
                </tr>
            </tbody>
        </table>
    </div>

    <!-- SECTION 2: ATURAN PENELUSURAN -->
    <div class="card">
        <h2>📌 Aturan Penelusuran (Searching Rules)</h2>
        <ol>
            <li><strong>Prioritas Terkecil:</strong> Selalu memilih kandidat dengan nilai evaluasi/prioritas paling kecil dari Frontier.</li>
            <li><strong>Aturan Abjad (Tie-Breaking):</strong> Jika terdapat nilai prioritas yang sama, kandidat dipilih berdasarkan urutan alfabet (A ke Z).</li>
            <li><strong>Pemeriksaan Goal:</strong> Pemeriksaan titik tujuan (Goal) dilakukan saat kandidat diekstrak dari Frontier.</li>
            <li><strong>Pembaruan A*:</strong> Pada algoritma A*, nilai <code>g(n)</code> dan parent diperbarui jika ditemukan rute baru yang lebih murah.</li>
        </ol>

        <div class="formula-box">
            <strong>💡 Rumus Heuristik Manhattan Distance:</strong><br>
            <code>h(n) = |x<sub>G</sub> - x<sub>n</sub>| + |y<sub>G</sub> - y<sub>n</sub>|</code>
        </div>
    </div>

    <!-- SECTION 3: PETA GRAF -->
    <div class="card">
        <h2>🗺️ Peta Graf & Koordinat Grid</h2>
        <pre>
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
==================================================</pre>
        <p><strong>Koordinat (X, Y) Node:</strong> <code>S(0,1)</code>, <code>A(1,2)</code>, <code>B(1,0)</code>, <code>C(2,2)</code>, <code>D(2,0)</code>, <code>E(3,0)</code>, <code>G(4,1)</code></p>
    </div>

    <!-- SECTION 4: RINGKASAN HASIL -->
    <div class="card">
        <h2>📊 Ringkasan Hasil Perbandingan</h2>
        <table>
            <thead>
                <tr>
                    <th>Parameter</th>
                    <th>BFS</th>
                    <th>DFS</th>
                    <th>UCS</th>
                    <th>Greedy</th>
                    <th>A* Search</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Rute Ditemukan</strong></td>
                    <td>S->A->C->G</td>
                    <td>S->A->C->G</td>
                    <td>S->B->D->E->G</td>
                    <td>S->A->C->G</td>
                    <td>S->B->D->E->G</td>
                </tr>
                <tr>
                    <td><strong>Total Langkah</strong></td>
                    <td>3</td>
                    <td>3</td>
                    <td>4</td>
                    <td>3</td>
                    <td>4</td>
                </tr>
                <tr>
                    <td><strong>Total Biaya g(n)</strong></td>
                    <td>7</td>
                    <td>7</td>
                    <td><strong>4</strong></td>
                    <td>7</td>
                    <td><strong>4</strong></td>
                </tr>
                <tr>
                    <td><strong>Struktur Data</strong></td>
                    <td>Queue (FIFO)</td>
                    <td>Stack (LIFO)</td>
                    <td>Priority Queue</td>
                    <td>Priority Queue</td>
                    <td>Priority Queue</td>
                </tr>
                <tr>
                    <td><strong>Optimalitas</strong></td>
                    <td>Langkah</td>
                    <td>Tidak</td>
                    <td>Biaya</td>
                    <td>Tidak</td>
                    <td><strong>Langkah & Biaya</strong></td>
                </tr>
            </tbody>
        </table>
    </div>

    <!-- SECTION 5: CARA MENJALANKAN -->
    <div class="card">
        <h2>🎮 Cara Menjalankan Program</h2>
        <p>Instalasi pustaka prasyarat:</p>
        <pre>pip install networkx matplotlib</pre>
        <p>Menjalankan skrip Python:</p>
        <pre>
# Jalankan simulasi A* Search
python astar_search.py

# Jalankan simulasi Greedy Best-First Search
python greedy_search.py

# Jalankan simulasi UCS
python ucs_search.py</pre>
    </div>

    <footer>
        <p>Proyek Simulasi Algoritma Pencarian Rute &copy; 2026 — Kecerdasan Buatan (AI)</p>
    </footer>

</div>

</body>
</html>
