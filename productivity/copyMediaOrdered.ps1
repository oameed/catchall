###################################
### My Productivity Scripts     ###
### Copy Media from a Playlist  ### 
### by: Oameed Noakoasteen      ###
###################################

param([Parameter(Mandatory=$true)][string]$pln,
      [Parameter(Mandatory=$true)][string]$dir )

$media     = Get-Content $pln

$media_ext = $media | Foreach-Object {Split-Path $_ -Extension}
$media_ext = @($media_ext)

for($i=0; $i -lt $media.Length; $i++){
  Copy-Item -LiteralPath $media[$i] ($dir+'\'+$i+$media_ext[$i])
}


# root
# |
# |--- <destination directory>
# |
# |--- <...>.m3u
# |
# |--- copyMediaOrdered.ps1 
#
# .\copyMediaOrdered.ps1 -pln <...>.m3u -dir <destination-directory>
