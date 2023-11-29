$folderPath = "C:\Example\Folder"

# Get the current ACL for the folder
$acl = Get-Acl -Path $folderPath

# Find the entry for the user "Lehrer1"
$user = "Lehrer1"
$rule = $acl.Access | Where-Object { $_.IdentityReference -eq $user }

# Modify the user's permissions to be read and execute only
if ($rule) {
    $accessRights = [System.Security.AccessControl.FileSystemRights]::ReadAndExecute
    $inheritanceFlags = [System.Security.AccessControl.InheritanceFlags]::None
    $propagationFlags = [System.Security.AccessControl.PropagationFlags]::None
    $type = [System.Security.AccessControl.AccessControlType]::Allow
    $newRule = New-Object System.Security.AccessControl.FileSystemAccessRule($user, $accessRights, $inheritanceFlags, $propagationFlags, $type)
    $acl.SetAccessRule($newRule)
    Set-Acl -Path $folderPath -AclObject $acl
}
else {
    Write-Error "User $user not found in ACL"
}