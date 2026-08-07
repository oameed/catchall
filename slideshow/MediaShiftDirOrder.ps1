###################################
### My Productivity Scripts     ###
### Shift Media Directory Order ### 
### by: Oameed Noakoasteen      ###
###################################

param([Parameter(Mandatory=$true)][string]$itm            ,
      [Parameter(Mandatory=$true)][int   ]$stt            ,
                                  [string]$up     = $false,
                                  [int   ]$digits = 3      )

$directories = Get-ChildItem -Name -Directory

$index       = $directories.IndexOf($itm)
if ($index -eq -1)
{
      Write-Host "$itm NOT FOUND !!!"
      exit
}
else
{
      $directories = $directories[$index .. ($directories.Length - 1)]
      $dirnames    = $directories | ForEach-Object{$_.Split(' ')[1 .. $($_.Length - 1)] -join ' '}
      $dirnames    = 0 .. ($directories.Length - 1) | ForEach-Object{([string]($_ + $stt)).PadLeft($digits,'0') +  ' ' + $dirnames[$_]}

      if ($up -eq $true)
      {
            $indices = 0 .. ($dirnames.Length - 1)
      }
      else
      {
            $indices = ($dirnames.Length - 1) .. 0
      }

      foreach ($i in $indices)
      {
            mv $directories[$i] $dirnames[$i]
      }

}


# .\shiftDirOrder.ps1 -itm <original directory name> -stt <start value for new numbering>
