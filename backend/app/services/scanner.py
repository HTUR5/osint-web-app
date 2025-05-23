def run_all_scans(domain: str):
    # תוצאה מזויפת רק לבדיקה
    return {
        "subdomains": [f"sub1.{domain}", f"sub2.{domain}"],
        "emails": [f"admin@{domain}"],
        "ips": ["1.2.3.4"]
    }
