import h5py

def inspect_hdf5_structure(file_path):
    with h5py.File(file_path, 'r') as f:
        print(f"--- Struktur Utama File: {file_path} ---")
        
        # Fungsi untuk menelusuri semua folder di dalam
        def print_structure(name, obj):
            indent = "  " * name.count('/')
            if isinstance(obj, h5py.Group):
                print(f"{indent}[Folder] {name}")
            else:
                print(f"{indent}[Data  ] {name} | Shape: {obj.shape} | Type: {obj.dtype}")

        f.visititems(print_structure)

# Jalankan kode ini
inspect_hdf5_structure(r'C:\Users\user\Documents\Data\TPS_2.hdf5')