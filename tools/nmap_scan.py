import nmap
def run_nmap_scan(target: str, full_scan: bool = False):
    nm = nmap.PortScanner()
    
    # Fast scan or full scan mode
    arguments = "-sV" if not full_scan else "-sV -A -T4"
    
    nm.scan(target, arguments=arguments)
    
    results = []
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                service = nm[host][proto][port]
                results.append({
                    "host": host,
                    "port": port,
                    "state": service["state"],
                    "name": service.get("name", ""),
                    "product": service.get("product", ""),
                    "version": service.get("version", "")
                })
    return results
