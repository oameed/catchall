###################################
### My Productivity Scripts     ###
### Copy Media from a Playlist  ### 
### by: Oameed Noakoasteen      ###
###################################

param([Parameter(Mandatory=$true)][string]$pln,
      [Parameter(Mandatory=$true)][string]$dir )

$media         = Get-Content                 $pln
$mediaExisting = Get-ChildItem  -LiteralPath $dir -Name
$mediaExisting = @($existingmedia)


for($i=0; $i -lt $media.Length; $i++){
if (-not $mediaExisting -contains $media[$i]){
  Copy-Item -LiteralPath $media[$i] $dir
  }
}


# .\copyMedia.ps1 -pln <full-path-to-playlist> -dir <full-path-to-destination-directory>
