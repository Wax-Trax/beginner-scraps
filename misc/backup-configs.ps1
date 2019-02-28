#---------------------------------------------------------------------------
# # ATTENTION: Module SSH-Sessions must be in the Default System32
# Location: Windows\system32\WindowsPowerShell\v1.0\Modules
# MORE INFORMATION: http://www.powershelladmin.com/wiki/SSH_from_PowerShell_using_the_SSH.NET_library
#---------------------------------------------------------------------------
$ErrorActionPreference ="Inquire"
Import-Module SSH-Sessions

New-Item -Force -ItemType directory -Path "C:\Users\$env:username\Desktop\CfgExports\"
clear

$time ="$(get-date -f yyyy-MM-dd_HH.mm.ss)"
$ext =".txt"
$filepath ="C:\Users\$env:username\Desktop\CfgExports\"

$inputfile = Read-Host 'Please enter the input filename (must be in same folder as script): ' 

$user = Read-Host 'Please enter your username: '
$pass = Read-Host 'Please enter your password: ' 
clear
 
Get-Content $inputfile | Foreach-Object {
	New-SshSession $_ -Username $user -Password $pass
	$Results = Invoke-Sshcommand -ComputerName $_ -Command "sh run" -Quiet | Out-file "$filepath$_-$time$ext"
	Remove-SshSession -RemoveAll 
	}

exit
