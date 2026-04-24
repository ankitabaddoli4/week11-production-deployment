from flask import Blueprint, Response, jsonify, redirect
import psutil
import time

main_bp = Blueprint("main", __name__)


# -----------------------------
# HOME ROUTE
# -----------------------------
@main_bp.route("/")
def home():
    return redirect("/dashboard")


# -----------------------------
# LIVE SYSTEM METRICS API
# -----------------------------
@main_bp.route("/api/metrics")
def metrics():

    # ✅ REAL UPTIME FIX
    uptime_seconds = int(time.time() - psutil.boot_time())

    def format_uptime(seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f"{hours}h {minutes}m"

    return jsonify({
        # CPU
        "cpu_usage": psutil.cpu_percent(interval=1),

        # MEMORY
        "memory_usage": psutil.virtual_memory().percent,
        "memory_available_gb": round(psutil.virtual_memory().available / (1024**3), 2),

        # DISK
        "disk_usage": psutil.disk_usage('/').percent,
        "disk_free_gb": round(psutil.disk_usage('/').free / (1024**3), 2),

        # UPTIME (FIXED)
        "uptime": format_uptime(uptime_seconds)
    })


# -----------------------------
# DASHBOARD UI
# -----------------------------
@main_bp.route("/dashboard")
def dashboard():
    return Response("""
<!DOCTYPE html>
<html>
<head>
<title>Live Monitoring Dashboard</title>

<style>
body {
    font-family: Arial;
    background: #0f172a;
    color: white;
    padding: 30px;
}

h1 {
    text-align: center;
    color: #22c55e;
}

.container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.card {
    background: #1e293b;
    padding: 20px;
    margin: 15px;
    border-radius: 12px;
    width: 250px;
    text-align: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.4);
}

.value {
    font-size: 22px;
    color: #38bdf8;
    margin-top: 10px;
    font-weight: bold;
}
</style>

<script>
async function loadMetrics() {
    const res = await fetch('/api/metrics');
    const data = await res.json();

    document.getElementById("cpu").innerText = data.cpu_usage + "%";
    document.getElementById("mem").innerText = data.memory_usage + "%";
    document.getElementById("mem_avail").innerText = data.memory_available_gb + " GB";
    document.getElementById("disk").innerText = data.disk_usage + "%";
    document.getElementById("disk_free").innerText = data.disk_free_gb + " GB";
    document.getElementById("uptime").innerText = data.uptime;
}

setInterval(loadMetrics, 2000);
</script>

</head>

<body onload="loadMetrics()">

<h1>🚀 LIVE PRODUCTION MONITORING DASHBOARD</h1>

<div class="container">

<div class="card">
<h3>CPU Usage</h3>
<div class="value" id="cpu">Loading...</div>
</div>

<div class="card">
<h3>Memory Usage</h3>
<div class="value" id="mem">Loading...</div>
</div>

<div class="card">
<h3>Memory Available</h3>
<div class="value" id="mem_avail">Loading...</div>
</div>

<div class="card">
<h3>Disk Usage</h3>
<div class="value" id="disk">Loading...</div>
</div>

<div class="card">
<h3>Disk Free</h3>
<div class="value" id="disk_free">Loading...</div>
</div>

<div class="card">
<h3>Uptime</h3>
<div class="value" id="uptime">Loading...</div>
</div>

</div>

</body>
</html>
""", mimetype="text/html")