import re
from collections import Counter

LOG_FILE = "sample_auth.log"

def analyze_logs(file_path):
    failed_attempts = Counter()
    pattern = r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)"

    try:
        with open(file_path, "r") as file:
            for line in file:
                match = re.search(pattern, line)
                if match:
                    ip = match.group(1)
                    failed_attempts[ip] += 1

        print("\n[+] RAPPORT DE SÉCURITÉ - TENTATIVES D'ACCÈS ÉCHOUÉES")
        print("=" * 55)
        for ip, count in failed_attempts.most_common():
            status = "SUSPECT (Alerte Force Brute)" if count >= 3 else "Avertissement"
            print(f"IP: {ip:<15} | Échecs: {count:<2} | Statut: {status}")
        print("=" * 55)

    except FileNotFoundError:
        print(f"[-] Erreur : Le fichier '{file_path}' n'a pas été trouvé.")

if __name__ == "__main__":
    analyze_logs(LOG_FILE)