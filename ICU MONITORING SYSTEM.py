import random
import time
beds = [f"ICU_BED_{i}" for i in range(1, 100)]
while True:
    print("\n--- ICU MONITORING DASHBOARD ---")
    for bed in beds:
        hr = random.randint(45, 140)           # heart rate
        bp = random.randint(90, 190)           # systolic BP
        temp = round(random.uniform(34, 40),1) # temperature
        rbs = round(random.uniform(3, 20),1)   # glucose
        alerts = []
        # Heart Rate
        if hr < 50:
            alerts.append("Bradycardia")
        elif hr > 120:
            alerts.append("Tachycardia")
        # Blood Pressure
        if bp > 160:
            alerts.append("Hypertension")
        elif bp < 90:
            alerts.append("Hypotension")
        # Temperature
        if temp >= 38:
            alerts.append("Fever")
        elif temp <= 35:
            alerts.append("Hypothermia")
        # Glucose
        if rbs < 4:
            alerts.append("Hypoglycemia")
        elif rbs > 11:
            alerts.append("Hyperglycemia")
        print(f"{bed} | HR:{hr} BP:{bp} TEMP:{temp} RBS:{rbs}") 
        if alerts: 
            print(f"⚠ ALERT → {', '.join(alerts)}")
        
            
    time.sleep(3)  # pauses 3 seconds