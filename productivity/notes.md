
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

* **_VLC_**  

  * **Simple Settings**

    * Interface  
      
      * Look and feel  
        Start in minimal view mode  
        Pause playback when minimized  
        Show systray icon  
        Resize interface to video size  
        
      * Privacy/Network Interaction  
        Save recently played items  
     
    * Audio  
           
      * Volume  
        Always request audio start level to  
 
    * Subtitle/OSD  

      * Subtitle Effects  
        Font (e.g., “Cascadia Code”)  
        Font Size (e.g., “Smaller”)  
        Outline thickness (e.g., “none”)  
        Add a background   
        Subtitle Position (e.g., “-100 px”)  

  * **All Settings**   

    * Video

      * General Video Settings  

        Always on top
        
      * Subtitle/OSD

        * Settings Related to OSD, subtitles and subpictures
     
          Autodetect subtitle files
          Subtitle autodetection fuzziness (e.g., “1”)
          
        * Text Renderer  

          text opacity (e.g., “158”)
          Background opacity (e.g., “53”)

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

