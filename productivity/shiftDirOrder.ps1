param([Parameter(Mandatory=$true)][string]$itm       ,
      [Parameter(Mandatory=$true)][int   ]$stt       ,
                                  [int   ]$digits = 3 )

$dir = Get-ChildItem -Name -Directory
$idx = $dir.IndexOf($itm)

if ($idx -eq -1){
Write-Host "$itm NOT FOUND !!!"
exit
} 
else {
$dir = $dir[$idx .. ($dir.Length-1)]
$ord = @(0 .. ($dir.Length-1))
$ord = $ord | ForEach-Object {$_ + $stt}

$drn = $dir | ForEach-Object{$_.Split(' ')[1 .. $($_.Length-1)] -join ' '}

$dn  = @()
for($i=0; $i -lt $drn.Length; $i++){
$index = $ord[$i]
$dn   += ([string]$index).PadLeft($digits,'0') + ' ' + $drn[$i]
}

for($i=0; $i -lt $dir.Length; $i++){
mv $dir[$i] $dn[$i]
}

}


# root
# |
# |--- <directories>
# |
# |--- shiftDirOrder.ps1 
# 
# .\shiftDirOrder.ps1 -itm <original directory name> -stt <start value for new numbering>