#####################################################
### My Productivity Scripts                       ###
### Convert MOV Video to MP4 Video Using "ffmpeg" ### 
### by: Oameed Noakoasteen                        ###
#####################################################

$fns_input         = Get-ChildItem  ".\"  -Recurse -Name -File -Filter *.MOV
$fns_input         = @($fns_input)

$fns_output_parent = $fns_input | Foreach-Object {Split-Path $_ -Parent  }
$fns_output_parent = @($fns_output_parent)

$fns_output_base   = $fns_input | Foreach-Object {Split-Path $_ -LeafBase}
$fns_output_base   = @($fns_output_base)

for ($i = 0; $i -lt $fns_input.Length; $i++){
    $fn_output     = $path+$fns_output_parent[$i]+"\"+$fns_output_base[$i]+".mp4"
    ffmpeg -hide_banner -loglevel error -i $fns_input[$i] -c:v mpeg4 -c:a aac $fn_output 
    }

rm $fns_input


# root
# |
# |--- <directory containing all videos>
# |
# |--- convertMOVtoMP4.ps1
