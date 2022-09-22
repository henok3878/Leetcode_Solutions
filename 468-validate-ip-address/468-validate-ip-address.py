class Solution:
    def validIPAddress(self, queryIp: str) -> str:
        
        def validateIpv4(ip): 
            parts = ip.split('.')
            if len(parts) < 4 or len(parts) > 4:
                return False
            for part in parts:
                try:
                    if (part[0] == '0' and len(part) > 1) or 0 > int(part) or int(part) > 255:
                        return False
                except:
                    return False
            return True 
        
        def validateIpv6(ip):
            parts = ip.split(':')
            if len(parts) != 8:
                return False
            for part in parts:
                if len(part) < 1 or len(part) > 4:
                    return False
                part = part.lower() 
                for c in part:
                    if c not in "abcdef0123456789":
                        return False 
            return True 
        
        
        if "." in queryIp and validateIpv4(queryIp):
            return "IPv4"
        elif ":" in queryIp and validateIpv6(queryIp):
            return "IPv6"
        return "Neither"