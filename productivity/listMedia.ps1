###################################
### My Productivity Scripts     ###
### Create a Media Playlist     ### 
### by: Oameed Noakoasteen      ###
###################################

param([Parameter(Mandatory=$true)][string  ]$root            ,
      [Parameter(Mandatory=$true)][string[]]$dirs            ,
      [Parameter(Mandatory=$true)][string  ]$pln             ,
                                  [string  ]$vid     = $false,
                                  [string  ]$shuffle = $false )

$paths        = $dirs | ForEach-Object{$root + $_ }
$paths        = @($paths)

$filenames    = @()
for($i=0; $i -lt $paths.Length; $i++){
  if ($vid -eq $true){
    $fns      = Get-ChildItem  -LiteralPath $paths[$i] -Recurse -Name -File -Filter  *.mp4
  } 
  else {
    $fns      = Get-ChildItem  -LiteralPath $paths[$i] -Recurse -Name -File -Exclude *.srt,*.json,*.md 
  }
  $fullfns    = $fns | ForEach-Object{$paths[$i] + $_ }
  $filenames += $fullfns
  }

if ($shuffle -eq $true){
  $filenames    = $filenames | Get-Random -Shuffle
}

echo $filenames > $pln


# .\listMedia.ps1 -root <full-path-to-the-root> -dirs <directory-1>, ..., <directory-n>  -pln <name-of-the-output-file>
