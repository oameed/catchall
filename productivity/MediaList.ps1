###################################
### My Productivity Scripts     ###
### List Media                  ### 
### by: Oameed Noakoasteen      ###
###################################

param([string]$m       = "all" ,
      [string]$shuffle = $false )

$PlaylistName      = 'playlist.m3u'

$ExtensionsExclude = @('ps1','srt','json','md')

$ExtensionsInclude = @{ all = '*'
                        vid = @('*.MP4','*.mp4','*.MOV','*.mov')
                        img = @('*.heic','*.jpg','*.png')        }

$filenames         = Get-ChildItem  -File -Name -Recurse -Include $ExtensionsInclude[$m]
$filenames         = $filenames | Where-Object {$_.Split('.')[-1] -notin $ExtensionsExclude}

if ($shuffle -eq $true)
{
      $filenames   = $filenames | Get-Random -Shuffle
}

echo $filenames > $PlaylistName

# .\MediaList.ps1 -m <vid/img> -shuffle
