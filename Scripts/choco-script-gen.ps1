# Check if Chocolatey is already installed
if (-not (Test-Path "$env:ProgramData\chocolatey\choco.exe")) {
    # Install Chocolatey
    Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
}
else {
    Write-Host "Chocolatey is already installed."
}

# Update all Chocolatey packages
choco upgrade all -y

# Install Notepad++
choco install notepadplusplus -y

# Install 7-Zip
choco install 7zip -y

# Install VLC
choco install vlc -y

# Install Firefox
choco install firefox -y

# Install Discord
choco install discord -y

# Install Steam
choco install steam -y

# Install Spotify
choco install spotify -y

# Install GIMP
choco install gimp -y

# Install Bitwarden
choco install bitwarden -y

# Install ProtonVPN
choco install protonvpn -y

# Install Epic Games Launcher
choco install epicgameslauncher -y

# Install LibreOffice
choco install libreoffice-fresh -y

# Install Minecraft Launcher
choco install minecraft-launcher -y

# Install PowerToys
choco install powertoys -y