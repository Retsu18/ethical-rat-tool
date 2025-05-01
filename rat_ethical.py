import socket
import subprocess
import sys
import os
import platform
from datetime import datetime

# Ethical Safeguards
TARGET_IP = "127.0.0.1"  # Only localhost by default - must be explicitly changed
AUTHORIZED_USERS = ["admin"]  # Must be configured for actual use
CONSENT_FILE = "consent.txt"  # File that must exist on target system

class EthicalRAT:
    def __init__(self):
        self.ethical_check()
        
    def ethical_check(self):
        """Verify all ethical requirements are met before proceeding"""
        if not os.path.exists(CONSENT_FILE):
            print("ERROR: No consent file found. Access denied for ethical reasons.")
            sys.exit(1)
            
        if TARGET_IP not in ["127.0.0.1", "localhost"]:
            print("WARNING: You are attempting to connect to a non-local system.")
            print("Ensure you have written permission from the system owner.")
            input("Press Enter to confirm you have authorization, or Ctrl+C to cancel...")
    
    def connect(self):
        """Establish an ethical connection with safeguards"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TARGET_IP, 54321))  # Default port
            
            # Verify authorization
            s.send(b"AUTH_REQUEST")
            response = s.recv(1024).decode()
            
            if response != "AUTH_GRANTED":
                print("Authorization denied by target.")
                return
                
            print(f"Ethical connection established with {TARGET_IP}")
            self.handle_commands(s)
            
        except Exception as e:
            print(f"Connection error: {str(e)}")
        finally:
            s.close()
    
    def handle_commands(self, connection):
        """Process commands with ethical limitations"""
        while True:
            try:
                # Receive command from server
                cmd = connection.recv(1024).decode()
                
                if cmd.lower() == "exit":
                    break
                    
                # Ethical command filter
                if self.is_command_allowed(cmd):
                    output = self.execute_command(cmd)
                    connection.send(output.encode())
                else:
                    connection.send(b"Command not permitted for ethical reasons")
                    
            except Exception as e:
                print(f"Error: {str(e)}")
                break
    
    def is_command_allowed(self, cmd):
        """Check if command is ethically permitted"""
        forbidden = ["rm ", "format", "del ", "shutdown", "reboot", "useradd"]
        return not any(f in cmd.lower() for f in forbidden)
    
    def execute_command(self, cmd):
        """Execute a single command safely"""
        try:
            result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
            return result.decode()
        except subprocess.CalledProcessError as e:
            return e.output.decode()
    
    def generate_report(self):
        """Create ethical usage report"""
        system_info = f"""
        Ethical RAT Usage Report
        Date: {datetime.now()}
        System: {platform.system()} {platform.release()}
        User: {os.getlogin()}
        Commands Executed: (logged here)
        """
        return system_info


# Server-side ethical checks would be similar
if __name__ == "__main__":
    print("""
    ETHICAL REMOTE ADMIN TOOL DEMO
    ------------------------------
    For educational purposes only.
    Unauthorized use is prohibited.
    """)
    
    tool = EthicalRAT()
    tool.connect()