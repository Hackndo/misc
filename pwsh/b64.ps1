Function Base64{
	<#
	.SYNOPSIS
	  Encode and decode powershell commands
	.DESCRIPTION
	  Encode and decode powershell commands using input strings or files
	  
	.PARAMETER decode
	
	  If set, decode provided encoded command. Else, encode provided command
	
	.PARAMETER inputfile
	
	  If set, read command from file $InputFile. Else, read from STDIN
	
	.PARAMETER outputfile
	
	  If set, output result to file $OutputFile. Else, output to STDOUT
	
	.INPUTS
	  Encoded or decoded powershell command (STDIN or file)
	  
	.OUTPUTS
	  Encoded or decoded powershell command (STDOUT or file)
	
	.EXAMPLE
	  Base64
	  Insert code: pixis
	  cABpAHgAaQBzAA==
	  
	.EXAMPLE
	  Base64 -Decode
	  Insert code: cABpAHgAaQBzAA==
	  pixis
	  
	.EXAMPLE
	  Base64 -Decode -InputFile encodedCommand.txt
	  pixis
	  
	.EXAMPLE
	  Base64 -InputFile encodedCommand.txt -OutputFile decodedOutput.txt
	#>

	param (
		[Switch] $Decode = $false,
		[String] $InputFile,
		[String] $OutputFile
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
}
