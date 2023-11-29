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

choco install bitwarden notepadplusplus vscode 7zip git tortoisegit obsidian putty python vlc firefox discord steam spotify gimp protonvpn epicgameslauncher jdk8 libreoffice-fresh minecraft-launcher powertoys wsl microsoft-windows-terminal vortex windirstat cura audacity obs-studio scenebuilder intellijidea-ultimate phpstorm pycharm virtualbox xampp-80 -y