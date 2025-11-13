###########################################################
### My Productivity Scripts                             ###
### Convert HEIC Image to JPG Image Using "ImageMagick" ### 
### by: Oameed Noakoasteen                              ###
###########################################################

$fns_input         = Get-ChildItem  ".\"  -Recurse -Name -File -Filter *.heic
$fns_input         = @($fns_input)

$fns_output_parent = $fns_input | Foreach-Object {Split-Path $_ -Parent  }
$fns_output_parent = @($fns_output_parent)

$fns_output_base   = $fns_input | Foreach-Object {Split-Path $_ -LeafBase}
$fns_output_base   = @($fns_output_base)

for ($i = 0; $i -lt $fns_input.Length; $i++){
    $fn_output     = $path+$fns_output_parent[$i]+"\"+$fns_output_base[$i]+".jpg"
    magick $fns_input[$i] $fn_output
    }

rm $fns_input


# root
# |
# |--- <directory_1 containing images>
# |--- ...
# |--- <directory_n containing images>
# |
# |--- convertHEICtoJPG.ps1
