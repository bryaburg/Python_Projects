import subprocess

# Fetch WiFi profiles
meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
data = meta_data.decode('utf-8', errors="backslashreplace")
data = data.split('\n')
profiles = []

# Extract profile names
for i in data:
    if "All User Profile" in i:
        i = i.split(":")
        if len(i) >= 2:
            profile_name = i[1].strip()  # Trim whitespace
            profiles.append(profile_name)

# Display header
print("{:30}| {:<}".format("Wifi Name", "Password"))
print("-------------------------------------------")

# Fetch and display passwords
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear'])
        results = results.decode('utf-8', errors="backslashreplace")
        results = results.split('\n')
        passwords = [b.split(":")[1].strip() for b in results if "Key Content" in b]

        if passwords:
            print("{:<30}| {:<}".format(i, passwords[0]))
        else:
            print("{:<30}| {:<}".format(i, "No password found"))

    except subprocess.CalledProcessError:
        print("Encoding Error Occurred")
