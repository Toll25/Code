$lehrer= Get-ADUser -Filter * -SearchBase "OU=Lehrer,OU=People,DC=3ahits,DC=at"
$schueler= Get-ADUser -Filter * -SearchBase "OU=Schüler,OU=People,DC=3ahits,DC=at"
$verwaltung= Get-ADUser -Filter * -SearchBase "OU=Verwaltung,OU=People,DC=3ahits,DC=at"

foreach($i in $lehrer){
    $username=$i.Name
    $folderPath= "C:\DATA\homedirectories\Lehrer\"+$username ;
    if (-not (Test-Path -Path $folderPath -PathType Container)) {
        New-Item -Path $folderPath -ItemType Directory | Out-Null
        Write-Host "Folder created: $folderPath"
    } else {
        Write-Host "Folder already exists: $folderPath"
    }
    $acl = Get-Acl -Path $folderPath
    $accessRights = [System.Security.AccessControl.FileSystemRights]::Modify
    $inheritanceFlags = [System.Security.AccessControl.InheritanceFlags]::None
    $propagationFlags = [System.Security.AccessControl.PropagationFlags]::None
    $type = [System.Security.AccessControl.AccessControlType]::Allow
	$newRule = New-Object System.Security.AccessControl.FileSystemAccessRule($i.UserPrincipalName, $accessRights, $inheritanceFlags, $propagationFlags, $type)    
	$acl.SetAccessRule($newRule)
    Set-Acl -Path $folderPath -AclObject $acl
}
foreach($i in $verwaltung){
    $username=$i.Name
    $folderPath= "C:\DATA\homedirectories\Verwaltung\"+$username ;
    if (-not (Test-Path -Path $folderPath -PathType Container)) {
        New-Item -Path $folderPath -ItemType Directory | Out-Null
        Write-Host "Folder created: $folderPath"
    } else {
        Write-Host "Folder already exists: $folderPath"
    }
    $acl = Get-Acl -Path $folderPath
    $accessRights = [System.Security.AccessControl.FileSystemRights]::Modify
    $inheritanceFlags = [System.Security.AccessControl.InheritanceFlags]::None
    $propagationFlags = [System.Security.AccessControl.PropagationFlags]::None
    $type = [System.Security.AccessControl.AccessControlType]::Allow
	$newRule = New-Object System.Security.AccessControl.FileSystemAccessRule($i.UserPrincipalName, $accessRights, $inheritanceFlags, $propagationFlags, $type)    
	$acl.SetAccessRule($newRule)
    Set-Acl -Path $folderPath -AclObject $acl
}
foreach($i in $schueler){
    $username=$i.Name
    $folderPath= "C:\DATA\homedirectories\Schüler\"+$username ;
    if (-not (Test-Path -Path $folderPath -PathType Container)) {
        New-Item -Path $folderPath -ItemType Directory | Out-Null
        Write-Host "Folder created: $folderPath"
    } else {
        Write-Host "Folder already exists: $folderPath"
    }
    $acl = Get-Acl -Path $folderPath
    $accessRights = [System.Security.AccessControl.FileSystemRights]::Modify
    $inheritanceFlags = [System.Security.AccessControl.InheritanceFlags]::None
    $propagationFlags = [System.Security.AccessControl.PropagationFlags]::None
    $type = [System.Security.AccessControl.AccessControlType]::Allow
	$newRule = New-Object System.Security.AccessControl.FileSystemAccessRule($i.UserPrincipalName, $accessRights, $inheritanceFlags, $propagationFlags, $type)    
	$acl.SetAccessRule($newRule)
    Set-Acl -Path $folderPath -AclObject $acl
}