# DevOps Homelab – Baseline & Docker App Stack

## Ziel
Aufbau einer reproduzierbaren DevOps-Baseline auf einem Ubuntu-Host,  
um praxisnah Container-, Git- und Ops-Konzepte zu lernen.

Fokus:
- saubere Bestandsaufnahme
- keine Blindinstallationen
- reproduzierbare Infrastruktur
- Fehler analysieren statt „neu starten“

---

## 1. System-Bestand (Initial State)

**Host:**
- Hardware: ACEMAGICIAN AM06Pro (Ryzen 5, 16 GB RAM)
- OS: Ubuntu 24.04 LTS
- Zugriff: SSH
- Netzwerk: LAN (IPv4 + IPv6)

**Überprüfte Punkte:**
- Kernel & OS-Version
- Speicher & CPU
- Platten
- Netzwerkinterfaces

Beispiel:
```bash
uname -a
lsb_release -a
df -h
free -h
ip a
