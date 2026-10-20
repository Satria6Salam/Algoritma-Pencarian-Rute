import networkx as nx
import matplotlib.pyplot as plt

# =====================================================================
# FUNGSI 1: MENDAPATKAN DATA GRAF (INPUT JALUR RUTE)
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
def gambar_visualisasi_tahap(graf_networkx, posisi_node, tumpukan_dfs, node_dikunjungi, node_saat_ini, judul_tahap, teks_log_terminal):
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
        elif node in tumpukan_dfs:
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
    plt.savefig("DFS_" + nama_file_gambar + ".png")
    
    # Waktu jeda diperlama menjadi 3 detik agar log biaya sempat terbaca
    plt.pause(3.0)

# =====================================================================
# FUNGSI 4: FUNGSI UTAMA DFS DENGAN FRONTIER DAN BIAYA
# =====================================================================
def jalankan_algoritma_dfs(graf_rute, node_awal, node_tujuan):
    print("Memulai simulasi DFS dari Node [" + node_awal + "]...\n")
    
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

    tumpukan_dfs = []
    node_dikunjungi = [] 
    kamus_jejak_parent = {}
    
    # Menambahkan kamus untuk melacak total biaya dari Start ke node tertentu
    kamus_biaya_rute = {}
    kamus_biaya_rute[node_awal] = 0 # Biaya di titik awal adalah 0
    
    tumpukan_dfs.append(node_awal)
    node_dikunjungi.append(node_awal)
    
    nomor_langkah = 1
    status_ditemukan = False

    while len(tumpukan_dfs) > 0:
        # DFS menggunakan prinsip LIFO (Last In, First Out)
        node_saat_ini = tumpukan_dfs.pop(-1)
        
        # Mengambil biaya kumulatif node saat ini dari kamus
        biaya_saat_ini = kamus_biaya_rute[node_saat_ini]
        
        teks_log_proses = "Langkah " + str(nomor_langkah) + ": Mengevaluasi Node [" + node_saat_ini + "]\n"
        teks_log_proses = teks_log_proses + "  -> Biaya rute dilalui: " + str(biaya_saat_ini) + "\n"
        
        if node_saat_ini == node_tujuan:
            teks_log_proses = teks_log_proses + "  -> GOAL TERCAPAI! Node [" + node_tujuan + "] berhasil ditemukan."
            print(teks_log_proses)
            gambar_visualisasi_tahap(graf_networkx, koordinat_posisi, tumpukan_dfs, node_dikunjungi, node_saat_ini, "Tahap " + str(nomor_langkah) + ": Selesai DFS", teks_log_proses)
            status_ditemukan = True
            break 

        daftar_tetangga = graf_rute[node_saat_ini]
        
        # ==========================================================
        # MENGURUTKAN CABANG SESUAI ABJAD
        # ==========================================================
        list_nama_tetangga = []
        for kunci_tetangga in daftar_tetangga:
            list_nama_tetangga.append(kunci_tetangga)
            
        # Mengurutkan dari A ke Z
        list_nama_tetangga.sort()
        
        # PENTING UNTUK DFS: Karena menggunakan tumpukan (Stack), yang masuk
        # paling akhir akan diproses paling awal. Agar abjad 'A' diproses duluan, 
        # maka harus membalik urutan list menjadi Z ke A sebelum memasukannya.
        list_nama_tetangga.reverse()
        
        teks_nama_tetangga = "["
        for nama in list_nama_tetangga:
            teks_nama_tetangga = teks_nama_tetangga + "'" + nama + "' "
        teks_nama_tetangga = teks_nama_tetangga + "]"
        
        teks_log_proses = teks_log_proses + "  -> Mengambil cabang: " + teks_nama_tetangga + "\n"
        
        for node_tetangga in list_nama_tetangga:
            if node_tetangga not in node_dikunjungi:
                
                # Menghitung biaya perjalanan ke node tetangga
                bobot_langkah = daftar_tetangga[node_tetangga]
                biaya_baru = biaya_saat_ini + bobot_langkah
                
                # Simpan biaya baru ke dalam kamus
                kamus_biaya_rute[node_tetangga] = biaya_baru
                
                teks_log_proses = teks_log_proses + "     + Masuk Frontier (Stack): [" + node_tetangga + "] (Biaya: " + str(biaya_baru) + ")\n"
                
                node_dikunjungi.append(node_tetangga)
                tumpukan_dfs.append(node_tetangga)
                kamus_jejak_parent[node_tetangga] = node_saat_ini
                
        # Menyusun string isi Frontier beserta biayanya
        teks_isi_frontier = "["
        for node_frontier in tumpukan_dfs:
            biaya_frontier = kamus_biaya_rute[node_frontier]
            teks_isi_frontier = teks_isi_frontier + node_frontier + "(cost:" + str(biaya_frontier) + ") "
        teks_isi_frontier = teks_isi_frontier + "]"
        
        teks_log_proses = teks_log_proses + "  -> Isi FRONTIER: " + teks_isi_frontier + "\n"
        
        print(teks_log_proses)
        
        gambar_visualisasi_tahap(
            graf_networkx, koordinat_posisi, tumpukan_dfs, node_dikunjungi, node_saat_ini, 
            "Tahap " + str(nomor_langkah) + ": Evaluasi Node " + node_saat_ini, teks_log_proses
        )
        nomor_langkah = nomor_langkah + 1

    if status_ditemukan == True:
        rute_akhir_dfs = []
        node_mundur = node_tujuan
        while node_mundur != node_awal:
            rute_akhir_dfs.append(node_mundur)
            node_mundur = kamus_jejak_parent[node_mundur]
        rute_akhir_dfs.append(node_awal)
        rute_akhir_dfs.reverse()
        
        teks_rute_panah = ""
        indeks = 0
        for node_rute in rute_akhir_dfs:
            teks_rute_panah = teks_rute_panah + node_rute
            if indeks < len(rute_akhir_dfs) - 1:
                teks_rute_panah = teks_rute_panah + " -> "
            indeks = indeks + 1
            
        biaya_total_akhir = kamus_biaya_rute[node_tujuan]
        
        teks_final_kesimpulan = "HASIL PENCARIAN DFS\n" + "=========================\n"
        teks_final_kesimpulan = teks_final_kesimpulan + "Rute Ditemukan DFS:\n" + teks_rute_panah + "\n\n"
        jumlah_langkah = len(rute_akhir_dfs) - 1
        teks_final_kesimpulan = teks_final_kesimpulan + "Total Langkah Edge: " + str(jumlah_langkah) + " langkah\n"
        teks_final_kesimpulan = teks_final_kesimpulan + "Total Biaya (Cost): " + str(biaya_total_akhir) + "\n"
        
        plt.clf()
        plt.subplots_adjust(right=0.55)
        nx.draw(graf_networkx, koordinat_posisi, with_labels=True, node_color='lightgreen', node_size=2000, font_size=12, font_weight='bold')
        plt.title("RUTE BERHASIL DITEMUKAN OLEH DFS!", fontsize=16, fontweight='bold', color='green')
        plt.figtext(0.60, 0.5, teks_final_kesimpulan, fontsize=12, va="center", ha="left", family='monospace', bbox=dict(boxstyle="round,pad=1", facecolor="palegreen", edgecolor="green"))
        plt.savefig("DFS_Tahap_Final_Rute_Ditemukan.png")
        plt.pause(5.0)
    else:
        print("\n[!] Maaf, Node tujuan tidak dapat dijangkau dari node awal.")

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    cetak_ascii_art_peta()
    data_graf_rute = inisialisasi_peta_rute()
    jalankan_algoritma_dfs(graf_rute=data_graf_rute, node_awal='S', node_tujuan='G')