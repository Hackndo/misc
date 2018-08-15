param (
    [switch]$decode = $false,
    [string]$inputfile,
    [string]$outputfile
)


IF($decode) {
    IF($inputfile) {
        $Text = get-content $inputfile
    } else {
        $Text= Read-Host -Prompt 'Insert code'
    }
    $ReturnText = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($Text))
} else {
    IF($inputfile) {
        $Text = get-content $inputfile
    } else {
        $Text= Read-Host -Prompt 'Insert code'
    }
    $Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)
    $ReturnText =[Convert]::ToBase64String($Bytes)
}

IF($outputfile) {
    $ReturnText | Out-File $outputfile 
} else {
    Write-Host $ReturnText
}
