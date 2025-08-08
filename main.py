import subprocess
import time
import webbrowser

def start_backend():
    return subprocess.Popen(["uvicorn", "api.backend:app", "--port", "9999", "--reload"])

def start_frontend():
    return subprocess.Popen([
        "streamlit", "run", "frontend/frontend.py",
        "--server.headless=true",
        "--browser.gatherUsageStats=false"
    ])

if __name__ == "__main__":
    # Start FastAPI
    print("[INFO] Starting backend (FastAPI)...")
    backend_process = start_backend()

    # Give backend time to initialize
    time.sleep(3)

    # Start Streamlit frontend
    print("[INFO] Starting frontend (Streamlit)...")
    frontend_process = start_frontend()

    # Give frontend time to start, then open browser
    time.sleep(5)
    webbrowser.open("http://localhost:8501")  # or 8503 if streamlit defaults to that

    # Wait for both processes
    try:
        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        print("\n[INFO] Shutting down...")
        backend_process.terminate()
        frontend_process.terminate()
