
## [Computing Basics](https://archive.org/details/computing-basics)  

## App Configuration

* **_MPV_**  

  * **MPV's `portable_config` Directory**  
    
    * **`mpv.conf`**  
          
          no-osc  
          no-border   
          ontop   
          volume=0  
          image-display-duration=10   
          sub-auto=all  
          sub-bold=yes  
          sub-outline-color=1.0/0.0/0.0/0.75  
          sub-scale=1.5  
    
    * **How to Run**  

      For Videos:  
           
          mpv .\<...>.m3u --shuffle --geometry=45%x38%  
     
      For Images:    
        
          mpv .\<...>.m3u --shuffle --geometry=25%x45%  

* **_VSCode_**  
  
  * **VSCode as Terminal**  
    
    1. In `User Settings (JSON)` add the following:
       
           "workbench.panel.opensMaximized": "always"  
           "terminal.integrated.env.windows":{"PSExecutionPolicyPreference":"Bypass"}      

    2. Use `Ctrl + Shift + ~` to open a terminal in an open window 

## Code Snippets

* **_PowerShell_**  
  
  * **PowerShell's Execution Policy**  
    
        Set-ExecutionPolicy Bypass -Scope Process -Force
    
  * **PowerShell's History**  
        
        Set-PSReadLineOption -HistorySaveStyle SaveNothing # disable command history saving for the current session
        
        Clear-History                                      # clear existing command history
        Remove-Item (Get-PSReadLineOption).HistorySavePath # clear existing command history
    
  * **Removing Spaces from File Names**  
    
        Get-ChildItem -File | Rename-Item -NewName {$_.Name -replace ' ','_'}

