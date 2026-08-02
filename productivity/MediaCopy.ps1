###############################
### My Productivity Scripts ###
### Copy Media              ### 
### by: Oameed Noakoasteen  ###
###############################

param([Parameter(Mandatory=$true)][string]$pln             ,
      [Parameter(Mandatory=$true)][string]$dir             ,
                                  [string]$ordered = $false, 
                                  [int   ]$digits  = 4      )

$media     = Get-Content $pln

$leaf      = $media | Foreach-Object {Split-Path -LiteralPath $_ -Leaf     }
$stem      = $media | Foreach-Object {Split-Path -LiteralPath $_ -LeafBase }
$extension = $media | Foreach-Object {Split-Path -LiteralPath $_ -Extension}


if ($ordered -eq $true)
{
      $filenames = 0..($media.Length - 1) | ForEach-Object { $dir + ([string]$_).PadLeft($digits,'0') + $extension[$_] }
}
else
{
      $filenames = 0..($media.Length - 1) | ForEach-Object { $dir + $leaf[$_] }
}

for($i=0; $i -lt $media.Length; $i++)
{
      Copy-Item -LiteralPath $media[$i] $filenames[$i]
}


# .\MediaCopy.ps1 -pln <filename> -dir <destination-directory> -ordered true
