from flask import Flask, render_template, request
from datetime import datetime
import pandas as pd
import os

app = Flask(__name__)

def ping_device(ip):
    # Dummy ping (simulated)
    return True

def scan_ports(ip):
    # Dummy open ports (simulated)
    return [80, 443]

def assign_score(open_port_count):
    if open_port_count == 0:
        return "A (Very Secure)"
    elif open_port_count <= 2:
        return "B (Secure)"
    else:
        return "C (Vulnerable)"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    network_prefix = request.form.get('network', '').strip()
    devices_data = []
    scan_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Simulated scan for demo
    for i in range(1, 6):
        ip = network_prefix + str(i)
        open_ports = scan_ports(ip)
        score = assign_score(len(open_ports))
        devices_data.append({
            "Device IP": ip,
            "Open Ports": ", ".join(map(str, open_ports)),
            "Security Rating": score,
            "Scan Time": scan_time
        })

    # Save Excel report
    df = pd.DataFrame(devices_data)
    filename = f"Smart_IoT_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    df.to_excel(filename, index=False)

    return render_template('result.html', devices=devices_data, file=filename)

if __name__ == '__main__':
    app.run(debug=True)
