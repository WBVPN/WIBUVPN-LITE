import os

replacements = {
    "WBVPN/WIBUVPN-LITE.git": "WBVPN/WIBUVPN-LITE.git",
    "WBVPN/WIBUVPN-LITE": "WBVPN/WIBUVPN-LITE",
    "WBVPN": "WBVPN",
    "wibuvpnstore@gmail.com": "wibuvpnstore@gmail.com",
    "TULIS_TOKEN_GITHUB_DISINI": "TULIS_TOKEN_GITHUB_DISINI",
    "WBVPN/WIBUVPN-LITE/main/ip": "WBVPN/WIBUVPN-LITE/main/ip"
}

for root, dirs, files in os.walk("."):
    if ".git" in root:
        continue
    for file in files:
        if file.endswith((".sh", ".py", "menu", "literegis", "liteextend", "litedelete")):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                changed = False
                for old, new in replacements.items():
                    if old in content:
                        content = content.replace(old, new)
                        changed = True
                
                if changed:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"Fixed {path}")
            except Exception as e:
                pass
