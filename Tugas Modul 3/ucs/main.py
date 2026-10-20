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
    plt.savefig("UCS_" + nama_file_gambar + ".png")
    
    plt.pause(3.0) 

# =====================================================================
# FUNGSI 4: FUNGSI UTAMA UNIFORM COST SEARCH (UCS) VERBOSE
# =====================================================================
def jalankan_algoritma_ucs(graf_rute, node_awal, node_tujuan):
    print("Memulai simulasi UCS dari Node [" + node_awal + "]...\n")
    
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

    # Frontier UCS menggunakan Priority Queue (Antrean Prioritas)
    antrean_prioritas_ucs = []
    
    rute_awal = []
    rute_awal.append(node_awal)
    
    # Format data Frontier UCS: [total_biaya, nama_node, [rute_perjalanan]]
    data_node_awal = [0, node_awal, rute_awal]
    antrean_prioritas_ucs.append(data_node_awal)
    
    node_dikunjungi = [] 
    
    nomor_langkah = 1
    status_ditemukan = False
    hasil_rute_terbaik = []
    hasil_biaya_terbaik = 0

    while len(antrean_prioritas_ucs) > 0:
        
        # ==========================================================
        # [PENERAPAN ATURAN] MENGURUTKAN BERDASARKAN BIAYA & ABJAD
        # ==========================================================
        antrean_prioritas_ucs.sort()
        # ==========================================================
        
        # Mengambil node dengan biaya paling rendah di Frontier
        elemen_teratas = antrean_prioritas_ucs.pop(0)
        
        biaya_saat_ini = elemen_teratas[0]
        node_saat_ini = elemen_teratas[1]
        rute_saat_ini = elemen_teratas[2]
        
        daftar_node_di_antrean = []
        for isi_antrean in antrean_prioritas_ucs:
            nama_node_antrean = isi_antrean[1]
            daftar_node_di_antrean.append(nama_node_antrean)
        
        teks_log_proses = "Langkah " + str(nomor_langkah) + ": Mengevaluasi Node [" + node_saat_ini + "]\n"
        teks_log_proses = teks_log_proses + "  -> Biaya rute dilalui: " + str(biaya_saat_ini) + "\n"
        
        if node_saat_ini in node_dikunjungi:
            teks_log_proses = teks_log_proses + "  -> Melewati node ini (sudah dikunjungi jalur termurah).\n"
            print(teks_log_proses)
            nomor_langkah = nomor_langkah + 1
            continue
            
        node_dikunjungi.append(node_saat_ini)
        
        if node_saat_ini == node_tujuan:
            teks_log_proses = teks_log_proses + "  -> GOAL TERCAPAI! Node [" + node_tujuan + "] ditemukan."
            print(teks_log_proses)
            gambar_visualisasi_tahap(graf_networkx, koordinat_posisi, daftar_node_di_antrean, node_dikunjungi, node_saat_ini, "Tahap " + str(nomor_langkah) + ": Selesai UCS", teks_log_proses)
            status_ditemukan = True
            hasil_rute_terbaik = rute_saat_ini
            hasil_biaya_terbaik = biaya_saat_ini
            break 

        daftar_tetangga = graf_rute[node_saat_ini]
        
        teks_nama_tetangga = "["
        for kunci_tetangga in daftar_tetangga:
            teks_nama_tetangga = teks_nama_tetangga + "'" + kunci_tetangga + "' "
        teks_nama_tetangga = teks_nama_tetangga + "]"
        
        teks_log_proses = teks_log_proses + "  -> Cabang tetangga: " + teks_nama_tetangga + "\n"
        
        for node_tetangga in daftar_tetangga:
            if node_tetangga not in node_dikunjungi:
                bobot_menuju_tetangga = daftar_tetangga[node_tetangga]
                biaya_baru = biaya_saat_ini + bobot_menuju_tetangga
                
                rute_baru = []
                for titik_rute in rute_saat_ini:
                    rute_baru.append(titik_rute)
                rute_baru.append(node_tetangga)
                
                teks_log_proses = teks_log_proses + "     + Masuk Frontier: [" + node_tetangga + "] (Biaya: " + str(biaya_baru) + ")\n"
                
                data_tetangga_baru = [biaya_baru, node_tetangga, rute_baru]
                antrean_prioritas_ucs.append(data_tetangga_baru)
                
        # Menyusun string isi Frontier beserta biayanya
        teks_isi_frontier = "["
        for item_antrean in antrean_prioritas_ucs:
            biayanya = str(item_antrean[0])
            namanya = item_antrean[1]
            teks_isi_frontier = teks_isi_frontier + namanya + "(cost:" + biayanya + ") "
        teks_isi_frontier = teks_isi_frontier + "]"
        
        teks_log_proses = teks_log_proses + "  -> Isi FRONTIER: " + teks_isi_frontier + "\n"
        
        print(teks_log_proses)
        
        gambar_visualisasi_tahap(
            graf_networkx, koordinat_posisi, daftar_node_di_antrean, node_dikunjungi, node_saat_ini, 
            "Tahap " + str(nomor_langkah) + ": Evaluasi Node " + node_saat_ini, teks_log_proses
        )
        nomor_langkah = nomor_langkah + 1

    if status_ditemukan == True:
        teks_rute_panah = ""
        indeks = 0
        for node_rute in hasil_rute_terbaik:
            teks_rute_panah = teks_rute_panah + node_rute
            if indeks < len(hasil_rute_terbaik) - 1:
                teks_rute_panah = teks_rute_panah + " -> "
            indeks = indeks + 1
        
        teks_final_kesimpulan = "HASIL PENCARIAN UCS\n" + "=========================\n"
        teks_final_kesimpulan = teks_final_kesimpulan + "Rute Termurah UCS:\n" + teks_rute_panah + "\n\n"
        teks_final_kesimpulan = teks_final_kesimpulan + "Total Biaya (Cost): " + str(hasil_biaya_terbaik) + "\n\n"
        teks_final_kesimpulan = teks_final_kesimpulan + "Note: UCS menjamin\nrute dengan total\nbobot paling kecil,\nwalaupun langkahnya\nlebih banyak."
        
        plt.clf()
        plt.subplots_adjust(right=0.55)
        nx.draw(graf_networkx, koordinat_posisi, with_labels=True, node_color='lightgreen', node_size=2000, font_size=12, font_weight='bold')
        plt.title("RUTE TERMURAH DITEMUKAN OLEH UCS!", fontsize=14, fontweight='bold', color='green')
        plt.figtext(0.60, 0.5, teks_final_kesimpulan, fontsize=12, va="center", ha="left", family='monospace', bbox=dict(boxstyle="round,pad=1", facecolor="palegreen", edgecolor="green"))
        plt.savefig("UCS_Tahap_Final_Rute_Ditemukan.png")
        plt.pause(5.0)
    else:
        print("\n[!] Maaf, Node tujuan tidak dapat dijangkau dari node awal.")

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    cetak_ascii_art_peta()
    data_graf_rute = inisialisasi_peta_rute()
    jalankan_algoritma_ucs(graf_rute=data_graf_rute, node_awal='S', node_tujuan='G')