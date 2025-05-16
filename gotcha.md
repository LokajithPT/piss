# GILMA – Git-Like Memory Access

## Overview

**GILMA (Git-Like Memory Access)** is a lightweight, self-hosted version control and file management system designed specifically for secure internal networks. It provides Git-style push/pull capabilities via a custom CLI tool and a streamlined web dashboard with intuitive commands. GILMA is optimized for environments like mesh networks (e.g., Tailscale), offering strict access control and seamless private collaboration across trusted systems.

---

## Key Features

### 🔒 Authentication & Session Management
- Secure login system tailored for single-user environments.
- Flask-based session management with a fixed 2-hour expiration window for the web UI.

### 📁 Repository Management
- Upload entire folders as "repositories."
- List and preview stored folders and files.
- Download individual files or entire directories.
- Remove outdated or unused folders using a single command.

### 🖥️ Web Dashboard
- Minimalistic and clean user interface.
- Real-time display of all uploaded repositories.
- One-click access to download or view files.
- Built-in logout functionality and session timeout alerts.

### 💻 CLI Tool – `gilma`
The command-line utility is designed to be both intuitive and powerful:

- `gilma vechuko <folder>` – Uploads a folder to the server.
- `gilma vangiko <folder>` – Downloads a folder from the server.
- `gilma sethupo <folder>` – Deletes a folder from the server.
- `gilma kaami` – Lists all folders available on the server.

### 🔐 Private Network Security
- Server runs within a mesh VPN (e.g., Tailscale) to ensure secure peer-to-peer connectivity.
- Inaccessible from the public internet.
- Operates solely within trusted, authenticated devices on the same network.

---

## System Requirements

### Minimum Hardware
- Old Macintosh or eMachines system (Pentium Dual Core)
- 4 GB RAM
- 250 GB Disk Space

> Note: Any setup meeting or exceeding these specifications will run GILMA reliably.

---

## Dependencies

### Server (`gilmaserv`)
- Python 3.8+
- Flask (`pip install flask`)
- Tailscale or equivalent mesh VPN setup (recommended)

### Client (`gilma`)
- Python 3.8+
- POSIX-compliant shell or terminal
- Git (for cloning the repo)
- Optional: `curl` or `wget` for API testing

---

## Installation & Usage

### Server Setup

1. **Install Flask**:
   ```bash
   pip install flask
   ```

2. **Run the Server**:
   ```bash
   python3 gilmaserv.py
   ```

3. **Access the Web UI**:
   Navigate to:
   ```
   http://<internal_ip>:5000
   ```

4. **(Optional) Tailscale Setup**:
   - Install Tailscale on both server and client systems.
   - Log in and verify that peers can see each other.
   - Use Tailscale IP/domain in place of internal IPs for improved reliability and security.

---

### Client Setup

1. **Clone the Repository**:
   ```bash
   git clone <repo_url>
   cd gilma-client
   ```

2. **Make CLI Executable**:
   ```bash
   chmod +x gilma
   ```

3. **Use Commands**:
   ```bash
   gilma vechuko <folder>     # Upload
   gilma vangiko <folder>     # Download
   gilma sethupo <folder>     # Delete
   gilma kaami                # List all folders
   ```

---

## API Endpoints

| Endpoint                 | Method | Purpose                                 |
|--------------------------|--------|-----------------------------------------|
| `/login`                 | POST   | Authenticates the user                  |
| `/dashboard`             | GET    | Displays uploaded repositories          |
| `/upload`                | POST   | Handles folder uploads                  |
| `/download/<folder>`     | GET    | Downloads all contents from a folder    |
| `/file/<folder>/<file>`  | GET    | Downloads a specific file               |
| `/delete-file`           | POST   | Deletes a selected folder               |
| `/list`                  | GET    | Returns JSON list of available folders  |

---

## Security Highlights

- Web routes protected using authenticated Flask sessions.
- Upload, download, and deletion actions restricted to logged-in users.
- Sessions expire after two hours for enhanced security.
- Full deployment assumed to be behind a mesh VPN like Tailscale.
- Files stored in an isolated, safe directory on the server.

---

## Use Cases

- Secure collaboration on internal development files.
- Sharing config files and scripts across trusted systems.
- Lightweight Git-style alternative for closed environments.
- Storage and version tracking in air-gapped or restricted setups.

---

## Planned Enhancements

- Role-based access control (RBAC)
- User-specific folder visibility
- Versioning system for uploaded files
- Activity logging and audit trails
- RESTful API tokens for automation pipelines
- Cross-platform desktop GUI client

---

## License

This project is proprietary software intended strictly for internal or private use. Licensing terms may be revised with future distribution or open-sourcing strategies.

---

## Maintainer

**Project Lead**: Loki  
**Contact**: [Insert your preferred internal email or communication handle]  
**GitHub Repository**: [https://github.com/LokajithPT/gilma](https://github.com/LokajithPT/gilma)

---

## Notes & Best Practices

- Folder names and paths are case-sensitive.
- For optimal performance, avoid uploading excessively large directories.
- Mesh network access should be limited to trusted devices only.

---

**GILMA** is built for environments that demand reliability, privacy, and performance — delivering a Git-like experience with total internal control.

