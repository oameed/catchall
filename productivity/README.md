
[**MPV Media Player**](#mpv-media-player)  

[**VLC Media Player**](#vlc-media-player)  

[**Visual Studio Code**](#visual-studio-code)  

[**Snippets**](#snippets)  

---


## <a id="mpv-media-player"></a>[MPV Media Player](https://mpv.io/)  

* **To Play a Playlist**  
  
      mpv .\<filename> --shuffle

* **To Configure**  
  
  1. Create the `portable_config` directory in MPV's main directory.  
    
  2. Create/Edit the `mpv.conf` file and add the following:  
          
         no-osc  
           
         no-border   
           
         ontop   
           
         volume=0  

         image-display-duration=10     

         geometry=5%:15%  
                    
         autofit-larger=65%x65%  
           
         autofit-smaller=35%x35%  
           
         sub-auto=all  
           
         sub-bold=yes  
          
         sub-outline-color=1.0/0.0/0.0/0.75  
           
         sub-scale=0.75  

## <a id="vlc-media-player"></a>[VLC Media Player](https://www.videolan.org/)  

* **Simple Settings**
  
  * **Interface**  
    * **Look and feel**  
      Start in minimal view mode  
      Show systray icon  
      Resize interface to video size  
      Pause playback when minimized  
      Use a dark pallette  
        
    * **Privacy/Network Interaction**  
      Save recently played items  
     
  * **Audio**  
    * **Volume**  
      Always request audio start level to  
 
  * **Subtitle/OSD**  
    * **On Screen Display**  
      show media ttitle on video start  
        
    * **Subtitle Effects**  
      Font (e.g., “Cascadia Code”)  
      Font Size (e.g., “Smaller”)  
      Outline thickness (e.g., “none”)  
      Add a background   
      Subtitle Position (e.g., “-100 px”)  

* **All Settings**  
  
  * **Inputs/Codecs**  
    * **Settings for input, demultiplexing and encoding**  
      * **Advanced**  
        Change title according to current media (e.g., $D)
          
  * **Playlist**  
    * **General playlist behaviour**  
      play and pause
      
  * **Video**  
    * **General Video Settings**  
      Always on top
        
  * **Subtitle/OSD**  
    * **Settings Related to OSD, subtitles and subpictures**  
      Autodetect subtitle files  
      Subtitle autodetection fuzziness (e.g., “1”)  
          
    * **Text Renderer**    
      text opacity (e.g., “158”)  
      Background opacity (e.g., “53”)  

## <a id="visual-studio-code"></a>[Visual Studio Code](https://code.visualstudio.com/)  

* **VSCode as Terminal**  
  
  1. In `User Settings (JSON)` add the following:  
     
         "workbench.panel.opensMaximized": "always"  
         
         "terminal.integrated.env.windows":{"PSExecutionPolicyPreference":"Bypass"}      
  
  2. Use `Ctrl + Shift + ~` to open a terminal in an open window 
  
* **Disable Restricted Mode**  
  
      "security.workspace.trust.enabled": false  

## <a id="snippets"></a>Snippets  

* [**PowerShell**](https://learn.microsoft.com/en-us/powershell/)  

  * **_Execution Policy_**  
    
        Set-ExecutionPolicy Bypass -Scope Process -Force
    
  * **_Removing Spaces from File Names_**  
    
        Get-ChildItem -File | Rename-Item -NewName {$_.Name -replace ' ','_'}  
  
  * **_Shuffling Contents of a Playlist_**  
    
        Get-Content <filename> | Get-Random -Shuffle > <filename>  


