import h5py
import os
import numpy as np

def run_extraction_pipeline():
    print("==================================================")
    print("GMAX DATA ENGINE: HDF5 VLEN IMAGE EXTRACTION")
    print("==================================================")

    # 1. Konfigurasi Path
    base_dir = r"C:\Users\user\Documents\EUCLID_Thesis_Benedict_13622066"
    input_hdf5 = os.path.join(base_dir, r"Data\TPS_2.hdf5")
    output_dir = os.path.join(base_dir, r"Data\Foto_Eksperimen")

    os.makedirs(output_dir, exist_ok=True)
    log_file_path = os.path.join(output_dir, 'extraction_log.txt')

    try:
        with h5py.File(input_hdf5, 'r') as f, open(log_file_path, 'w') as log_file:
            log_file.write("LOG EKSTRAKSI DATA DIC (REVISI VLEN ARRAY)\n")
            log_file.write("==============================================\n")
            
            gambar_group = f['images/dsp']
            frames = list(gambar_group.keys())
            
            print(f"[*] Mendeteksi {len(frames)} frame gambar terkompresi.")
            
            for i, nama_file in enumerate(frames):
                dataset = gambar_group[nama_file]
                
                # --- INTI PERBAIKAN BUG (MEMBONGKAR KAPSUL VLEN) ---
                raw_data = dataset[0] # Mengekstrak isi dari dalam kapsul
                
                if isinstance(raw_data, np.ndarray):
                    data_biner = raw_data.tobytes()
                else:
                    data_biner = bytes(raw_data)
                # ----------------------------------------------------
                
                ukuran_kb = len(data_biner) / 1024
                
                # Menyimpan gambar
                file_name = f"frame_{str(i).zfill(3)}.png"
                output_path = os.path.join(output_dir, file_name)
                
                with open(output_path, "wb") as img_file:
                    img_file.write(data_biner)
                
                status = f"[SUCCESS] Ekstraksi {file_name} | Ukuran Asli: {ukuran_kb:.2f} KB"
                print(status)
                log_file.write(status + "\n")

        print("\n[+] EKSTRAKSI SELESAI.")
        print(f"[+] Foto siap diproses di NCORR. Lokasi: {output_dir}")

    except Exception as e:
        print(f"\n[!] FATAL ERROR: {e}")

if __name__ == "__main__":
    run_extraction_pipeline()