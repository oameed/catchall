###################################
### My Productivity Scripts     ###
### Convert Media               ###
###     X to JPG                ###
###     X to MP4                ### 
### by: Oameed Noakoasteen      ###
###################################

param([Parameter(Mandatory=$true)][string]$m)

$ExtensionsInclude = @{img = @('*.heic','*.png')        
                       vid = @('*.MOV' ,'*.mov')}

$ExtensionsOutput  = @{img = '.jpg'
                       vid = '.mp4'}

$media     = Get-ChildItem  -File -Name -Recurse -Include $ExtensionsInclude[$m]
$media     = @($media)

$parent    = $media | Foreach-Object {Split-Path -Path $_ -Parent   }
$parent    = @($parent)
$stem      = $media | Foreach-Object {Split-Path -Path $_ -LeafBase }
$stem      = @($stem)

$filenames = 0..($media.Length - 1) | ForEach-Object { $parent[$_] + "\" + $stem[$_] + $ExtensionsOutput[$m]} 
$filenames = @($filenames)

if ($m -eq "img")
{
    for ($i = 0; $i -lt $media.Length; $i++)
    {
        magick $media[$i] $filenames[$i]
    }
}
elseif ($m -eq "vid")
{
    for ($i = 0; $i -lt $media.Length; $i++)
    {
        ffmpeg -hide_banner -loglevel error -i $media[$i] -c:v mpeg4 -c:a aac $filenames[$i] # -q:v 3
    }
}

rm $media

# .\MediaList.ps1 -m <vid/img>
