An attacker managed to gain foothold in our network, but we managed to capture the connection to our server.
Analyze the file and identify the tool used to connect, the service it connected to, its IP address, and the shared resources folder.
Flag format: TFCCTF{tool_service_ip_share}
Example: TFCCTF{ntlmrelayx_rdp_192.168.0.1_logs$}


Tool
`wmiexec`

Service 
`smb`


IP
`127.0.0.1`

Shared resource folder
`\\*\ADMIN$`


`TFCCTF{wmiexec_smb_127.0.01_admin$}`
