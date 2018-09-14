# Usage
# Test-ADCredential -UserName "jsmith" -Password "passw0rd" -FqdnDomain "corp.company.com"`

function Test-ADCredential {
    [CmdletBinding()]
    Param
    (
        [string]$UserName,
        [string]$Password,
        [string]$FqdnDomain
    )
    if (!($UserName) -or !($Password) -or !($FqdnDomain)) {
        Write-Warning 'Test-ADCredential: Please specify both user name, password, and domain FQDN'
    } else {
        Add-Type -AssemblyName System.DirectoryServices.AccountManagement
        $DS = New-Object System.DirectoryServices.AccountManagement.PrincipalContext('domain', $FqdnDomain)
        $DS.ValidateCredentials($UserName, $Password)
    }
}
