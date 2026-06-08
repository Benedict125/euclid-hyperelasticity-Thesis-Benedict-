import h5py
import numpy as np
import pandas as pd
from scipy.spatial import Delaunay
import os

def run_delaunay_csv_pipeline():
    print("==================================================")
    print("DELAUNAY MESH ENGINE -> CSV EXPORTER")
    print("==================================================")

    # 1. Path Konfigurasi (Sesuaikan dengan direktori Anda)
    base_dir = r"C:\Users\user\Documents\EUCLID_Thesis_Benedict_13622066"
    input_hdf5 = os.path.join(base_dir, r"Data\TPS_2.hdf5")
    output_dir = os.path.join(base_dir, r"EUCLID - Thesis - Dataset\Data_CSV")
    
    os.makedirs(output_dir, exist_ok=True)

    try:
        with h5py.File(input_hdf5, 'r') as f:
            print("[*] Mengekstrak Point Cloud dari HDF5...")
            nodes_data = f['region/nodes'][:]
            
            # Filter titik yang valid (Flag == 1) pada frame 0
            valid_idx = nodes_data[:, 2] == 1
            x_coords = nodes_data[valid_idx, 0]
            y_coords = nodes_data[valid_idx, 1]
            points = np.column_stack((x_coords, y_coords))
            num_nodes = len(points)
            
            print(f"[*] Berhasil mengekstrak {num_nodes} titik valid.")

            # 2. Delaunay Triangulation
            print("[*] Mengeksekusi Delaunay Triangulation...")
            tri = Delaunay(points)
            elements = tri.simplices
            num_elements = len(elements)
            print(f"[+] Jaring terbentuk: {num_elements} Elemen Segitiga.")

            # 3. EXPORT KE FORMAT EUCLID CSV
            print("[*] Menulis output_nodes.csv...")
            # Membuat format identik dengan skema dokumen TA Anda
            df_nodes = pd.DataFrame({
                'id': np.arange(num_nodes),
                'x': points[:, 0],
                'y': points[:, 1],
                'ux': np.zeros(num_nodes), # Akan diisi saat load step berjalan
                'uy': np.zeros(num_nodes),
                'fintx': np.zeros(num_nodes),
                'finty': np.zeros(num_nodes),
                'bcx': np.zeros(num_nodes, dtype=int), # Placeholder Boundary Conditions
                'bcy': np.zeros(num_nodes, dtype=int)
            })
            df_nodes.to_csv(os.path.join(output_dir, 'output_nodes.csv'), index=False)

            print("[*] Menulis output_elements.csv...")
            df_elements = pd.DataFrame({
                'node1': elements[:, 0],
                'node2': elements[:, 1],
                'node3': elements[:, 2],
                'Fxx': np.zeros(num_elements),
                'Fxy': np.zeros(num_elements),
                'Fyx': np.zeros(num_elements),
                'Fyy': np.zeros(num_elements),
                'Pxx': np.zeros(num_elements),
                'Pxy': np.zeros(num_elements),
                'Pyx': np.zeros(num_elements),
                'Pyy': np.zeros(num_elements)
            })
            df_elements.to_csv(os.path.join(output_dir, 'output_elements.csv'), index=False)

            print("\n[SUCCESS] PIPELINE SELESAI.")
            print(f"File CSV standar EUCLID telah dibuat di: {output_dir}")
            print("Langkah selanjutnya: Modifikasi data_loader.py untuk membaca CSV ini.")

    except Exception as e:
        print(f"\n[!] FATAL ERROR: {e}")

if __name__ == "__main__":
    run_delaunay_csv_pipeline()