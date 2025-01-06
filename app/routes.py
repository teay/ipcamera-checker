from flask import render_template
import socket
import requests

# ฟังก์ชันตรวจสอบ IP (เหมือนเดิม)
def check_public_ip():
    ip = requests.get('https://api.ipify.org').text
    return ip

def check_domain_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror as e:
        print(f"Error occurred while resolving {domain}: {e}")
        return None

# สร้าง route สำหรับหน้าแรก
def init_routes(app):
    @app.route('/')
    def index():
        public_ip = check_public_ip()

        domains = { # ใช้ dictionary เก็บข้อมูล domain
                   "google.com": None,
                   "google.co.th": None,
                   "blognone.com": None,
            }
        for domain_name in domains:
            domains[domain_name] = check_domain_ip(domain_name)

        return render_template('index.html', 
                               public_ip=public_ip,
                               domains=domains, # ส่ง dictionary ของ domain
                               ) # ลบ lan_hosts ออก