### Possible Solution

1. Which kind of attack was detected in the network traffic dump?
	- DNS Tunneling or DNS Data Exfiltration or DNS Exfiltration
   
2. Based on what characteristics the attack can be detected?
	- Randomized and long DNS Queries for the domain *.now.isyour.time
	- Non-Unicode characters in DNS Queries (< ?) characters)
	- DNS Server IP (172.182.182.99) different than the local DNS server (192.168.5.12)
	- TXT DNS Type known to be misused for DNS tunnelling
   
3. What is the exact starting point (packet number) of the attack?
	- No. 2599
	- The first DNS packet towards the rogue C2 DNS server was No. 2599 that initiated the tunnel setup.
   
4. What operating system and source IP the attack was originating from?
	- OS: Windows
	- IP: 192.168.5.10
	- By looking at the DNS queries from before the attack we see that the system talks to a legitimate DNS server. It talks to the domain Microsoft.com which indicates the Windows OS. [Another way is looking at an HTTP request from the same IP. Packet 2447 identifies the agent as "User-Agent: Microsoft-CryptoAPI/10.0"]
 
5. What was the obvious motivation for the attack and which goal most likely was to be achieved?
	- Motivation: Espionage or Money
	- Goal: Theft of intellectual property or Data theft and resale
