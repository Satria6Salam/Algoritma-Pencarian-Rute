import networkx as nx
import matplotlib.pyplot as plt

# =====================================================================
# ATURAN PENELUSURAN (SEARCHING RULES)
# =====================================================================
# 1. Ambil kandidat dengan nilai prioritas f(n) = g(n) + h(n) paling kecil.
# 2. Jika nilainya sama, pilih label menurut alfabet.
# 3. Periksa tujuan setelah kandidat diambil dari frontier.
# 4. Untuk A*, perbarui g dan parent jika rute baru lebih murah.
# =====================================================================

# =====================================================================
# FUNGSI 1: MENDAPATKAN DATA GRAF DAN RUMUS MANHATTAN
# =====================================================================
def inisialisasi_peta_rute():
    graf_rute = {
        'S': {'B': 1, 'A': 1}, 
        'A': {'C': 2},
        'B': {'D': 1},
        'C': {'G': 4},
        'D': {'E': 1},
        'E': {'G': 1},
        'G': {} 
    }
    return graf_rute

def inisialisasi_koordinat_node():
    # Koordinat (X, Y) untuk setiap titik pada graf
    koordinat = {
        'S': [0, 1],
        'A': [1, 2],
        'B': [1, 0],
        'C': [2, 2],
        'D': [2, 0],
        'E': [3, 0],
        'G': [4, 1]
    }
    return koordinat

def hitung_semua_heuristik_manhattan(koordinat, node_tujuan):
    koordinat_goal = koordinat[node_tujuan]
    x_goal = koordinat_goal[0]
    y_goal = koordinat_goal[1]
    
    kamus_heuristik = {}
    
    # Rumus Manhattan Distance: h(n) = |xG - xn| + |yG - yn|
    for nama_node in koordinat:
        koordinat_node_ini = koordinat[nama_node]
        x_node = koordinat_node_ini[0]
        y_node = koordinat_node_ini[1]
        
        selisih_x = abs(x_goal - x_node)
        selisih_y = abs(y_goal - y_node)
        
        nilai_h = selisih_x + selisih_y
        kamus_heuristik[nama_node] = nilai_h
        
    return kamus_heuristik

# =====================================================================
# FUNGSI 2: MENCETAK GRID ASCII ART KE TERMINAL
# =====================================================================
def cetak_ascii_art_peta():
    print("\n==================================================")
    print("      PETA RUTE GRID DI TERMINAL (ASCII ART)      ")
    print("==================================================")
    print("             (Bobot 1)    (Bobot 2)     (Bobot 4) ")
    print("           .-----> [A] --------> [C] --------.    ")
    print("          /                                   \\   ")
    print(" Start  [S]                                   [G] Goal ")
    print("          \\                                   /   ")
    print("           '-----> [B] --> [D] --> [E] ------'    ")
    print("             (1)       (1)     (1)      (1)       ")
    print("==================================================\n")

# =====================================================================
# FUNGSI 3: MENGGAMBAR VISUALISASI GRAFIS + TEKS LOG DI SAMPING
# =====================================================================
def gambar_visualisasi_tahap(graf_networkx, posisi_node, daftar_node_di_antrean, node_dikunjungi, node_saat_ini, judul_tahap, teks_log_terminal):
    plt.clf()
    plt.subplots_adjust(right=0.55)
    plt.title(judul_tahap, fontsize=14, fontweight='bold')
    
    daftar_warna_node = []
    semua_node = graf_networkx.nodes()
    
    for node in semua_node:
        if node == node_saat_ini:
            daftar_warna_node.append('yellow')
        elif node in node_dikunjungi:
            daftar_warna_node.append('lightblue')
        elif node in daftar_node_di_antrean:
            daftar_warna_node.append('lightgrey')
        else:
            daftar_warna_node.append('white')

    nx.draw(
        graf_networkx, posisi_node, with_labels=True, 
        node_color=daftar_warna_node, node_size=2000, 
        edgecolors='black', font_size=12, font_weight='bold'
    )
    
    label_bobot_garis = nx.get_edge_attributes(graf_networkx, 'weight')
    nx.draw_networkx_edge_labels(graf_networkx, posisi_node, edge_labels=label_bobot_garis, font_size=10)
    
    plt.figtext(
        0.58, 0.5, teks_log_terminal, fontsize=10, va="center", ha="left", family='monospace',
        bbox=dict(boxstyle="round,pad=0.8", facecolor="lightyellow", edgecolor="gray")
    )

    nama_file_gambar = judul_tahap.replace(":", "")
    nama_file_gambar = nama_file_gambar.replace(" ", "_")
    nama_file_gambar = nama_file_gambar.replace("*", "Star")  # <--- Tambahkan baris ini
    plt.savefig("ASTAR_" + nama_file_gambar + ".png")
    
    plt.pause(3.0) 

# =====================================================================
# FUNGSI 4: FUNGSI UTAMA ALGORITMA A* (A-STAR)
# =====================================================================
def jalankan_algoritma_astar(graf_rute, nilai_heuristik, node_awal, node_tujuan):
    print("Memulai simulasi A* (A-Star Search) dari Node [" + node_awal + "]...\n")
    
    graf_networkx = nx.DiGraph() 
    
    daftar_semua_asal = graf_rute.keys()
    for node_asal in daftar_semua_asal:
        data_tetangga = graf_rute[node_asal]
        daftar_semua_tujuan = data_tetangga.keys()
        for node_tujuan_tetangga in daftar_semua_tujuan:
            nilai_bobot = data_tetangga[node_tujuan_tetangga]
            graf_networkx.add_edge(node_asal, node_tujuan_tetangga, weight=nilai_bobot)
            
    koordinat_posisi = {
        'S': (0, 1), 'A': (1, 2), 'B': (1, 0), 
        'C': (2, 2), 'D': (2, 0), 'E': (3, 0), 'G': (4, 1)
    }

    plt.ion()
    plt.figure(figsize=(12, 6))

    # Format elemen Frontier A*: [f_score, nama_node, g_score, h_score, rute_perjalanan]
    antrean_prioritas_astar = []
    
    rute_awal = [node_awal]
    g_awal = 0
    h_awal = nilai_heuristik[node_awal]
    f_awal = g_awal + h_awal
    
    data_node_awal = [f_awal, node_awal, g_awal, h_awal, rute_awal]
    antrean_prioritas_astar.append(data_node_awal)
    
    # Kamus pelacak biaya g(n) terbaik yang pernah ditemukan untuk setiap node (Aturan 4)
    kamus_g_terbaik = {node_awal: 0}
    node_dikunjungi = [] 
    
    nomor_langkah = 1
    status_ditemukan = False
    hasil_rute_terbaik = []
    hasil_biaya_terbaik = 0

    while len(antrean_prioritas_astar) > 0:
        
        # ==========================================================
        # [ATURAN 1 & 2] SORTING BERDASARKAN NILAI F(N) DAHULU, 
        # JIKA F(N) SAMA MAKA DIURUTKAN BERDASARKAN ABJAD (A-Z)
        # ==========================================================
        antrean_prioritas_astar.sort()
        
        # Mengambil (Pop) kandidat dengan f(n) terkecil dari Frontier
        elemen_teratas = antrean_prioritas_astar.pop(0)
        
        f_saat_ini = elemen_teratas[0]
        node_saat_ini = elemen_teratas[1]
        g_saat_ini = elemen_teratas[2]
        h_saat_ini = elemen_teratas[3]
        rute_saat_ini = elemen_teratas[4]
        
        daftar_node_di_antrean = [item[1] for item in antrean_prioritas_astar]
        
        teks_log_proses = "Langkah " + str(nomor_langkah) + ": Mengevaluasi Node [" + node_saat_ini + "]\n"
        teks_log_proses += "  -> g(n)=" + str(g_saat_ini) + ", h(n)=" + str(h_saat_ini) + " => f(n)=" + str(f_saat_ini) + "\n"
        
        if node_saat_ini in node_dikunjungi:
            teks_log_proses += "  -> Melewati node ini (sudah dikunjungi jalur yang lebih optimal).\n"
            print(teks_log_proses)
            nomor_langkah += 1
            continue
            
        node_dikunjungi.append(node_saat_ini)
        
        # ==========================================================
        # [ATURAN 3] PERIKSA GOAL SETELAH KANDIDAT DIAMBIL DARI FRONTIER
        # ==========================================================
        if node_saat_ini == node_tujuan:
            teks_log_proses += "  -> GOAL TERCAPAI! Node [" + node_tujuan + "] berhasil ditemukan."
            print(teks_log_proses)
            gambar_visualisasi_tahap(
                graf_networkx, koordinat_posisi, daftar_node_di_antrean, 
                node_dikunjungi, node_saat_ini, "Tahap " + str(nomor_langkah) + ": Selesai A*", teks_log_proses
            )
            status_ditemukan = True
            hasil_rute_terbaik = rute_saat_ini
            hasil_biaya_terbaik = g_saat_ini
            break 

        daftar_tetangga = graf_rute[node_saat_ini]
        
        teks_nama_tetangga = "[" + " ".join(["'" + k + "'" for k in daftar_tetangga]) + "]"
        teks_log_proses += "  -> Cabang tetangga: " + teks_nama_tetangga + "\n"
        
        for node_tetangga in daftar_tetangga:
            bobot_edge = daftar_tetangga[node_tetangga]
            g_baru = g_saat_ini + bobot_edge
            
            # ==========================================================
            # [ATURAN 4] PERBARUI G DAN PARENT JIKA RUTE BARU LEBIH MURAH
            # ==========================================================
            if (node_tetangga not in kamus_g_terbaik) or (g_baru < kamus_g_terbaik[node_tetangga]):
                kamus_g_terbaik[node_tetangga] = g_baru
                h_tetangga = nilai_heuristik[node_tetangga]
                f_baru = g_baru + h_tetangga
                
                rute_baru = list(rute_saat_ini)
                rute_baru.append(node_tetangga)
                
                teks_log_proses += "     + Masuk Frontier: [" + node_tetangga + "] (g=" + str(g_baru) + ", h=" + str(h_tetangga) + " => f=" + str(f_baru) + ")\n"
                
                data_tetangga_baru = [f_baru, node_tetangga, g_baru, h_tetangga, rute_baru]
                antrean_prioritas_astar.append(data_tetangga_baru)
                
        # Format teks status Frontier: NamaNode(f:nilai_f)
        teks_isi_frontier = "["
        for item in antrean_prioritas_astar:
            teks_isi_frontier += item[1] + "(f:" + str(item[0]) + ") "
        teks_isi_frontier += "]"
        
        teks_log_proses += "  -> Isi FRONTIER: " + teks_isi_frontier + "\n"
        print(teks_log_proses)
        
        gambar_visualisasi_tahap(
            graf_networkx, koordinat_posisi, daftar_node_di_antrean, 
            node_dikunjungi, node_saat_ini, "Tahap " + str(nomor_langkah) + ": Evaluasi Node " + node_saat_ini, teks_log_proses
        )
        nomor_langkah += 1

    if status_ditemukan:
        teks_rute_panah = " -> ".join(hasil_rute_terbaik)
        
        teks_final_kesimpulan = "HASIL PENCARIAN A* (A-STAR)\n=========================\n"
        teks_final_kesimpulan += "Rute Optimal A*:\n" + teks_rute_panah + "\n\n"
        teks_final_kesimpulan += "Total Biaya g(G): " + str(hasil_biaya_terbaik) + "\n\n"
        teks_final_kesimpulan += "A* menggabungkan:\n- g(n): Biaya Aktual\n- h(n): Manhattan Distance\nmenjamin rute termurah!"
        
        plt.clf()
        plt.subplots_adjust(right=0.55)
        nx.draw(graf_networkx, koordinat_posisi, with_labels=True, node_color='lightgreen', node_size=2000, font_size=12, font_weight='bold')
        plt.title("RUTE OPTIMAL DITEMUKAN OLEH A*!", fontsize=14, fontweight='bold', color='green')
        plt.figtext(0.60, 0.5, teks_final_kesimpulan, fontsize=12, va="center", ha="left", family='monospace', bbox=dict(boxstyle="round,pad=1", facecolor="palegreen", edgecolor="green"))
        plt.savefig("ASTAR_Tahap_Final_Rute_Ditemukan.png")
        plt.pause(5.0)
    else:
        print("\n[!] Maaf, Node tujuan tidak dapat dijangkau dari node awal.")

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    cetak_ascii_art_peta()
    data_graf_rute = inisialisasi_peta_rute()
    data_koordinat = inisialisasi_koordinat_node()
    
    # Hitung nilai h(n) Manhattan Distance secara otomatis
    data_heuristik = hitung_semua_heuristik_manhattan(data_koordinat, node_tujuan='G')
    
    jalankan_algoritma_astar(graf_rute=data_graf_rute, nilai_heuristik=data_heuristik, node_awal='S', node_tujuan='G')