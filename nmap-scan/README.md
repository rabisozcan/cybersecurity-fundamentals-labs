# Nmap Scan Lab - Rabia Özcan

Bu lab’da nmap kullanarak belirli portların taramasını yaptım.

## Hedef
- Localhost (127.0.0.1)

## Tarama
- Portlar: 22, 80, 443
- Komut: `nmap -p 22,80,443 127.0.0.1 -oN nmap_results.txt`

## Sonuçlar
- Tüm portların durumu `nmap_results.txt` dosyasında.
- Örneğin:
PORT STATE SERVICE
22/tcp closed ssh
80/tcp closed http
443/tcp closed https  
- Bu deney, sistemde açık portları kontrol ederek temel ağ güvenliği pratiği sağlar.

