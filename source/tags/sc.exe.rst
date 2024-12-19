sc.exe
######

Description
###########
Service Control - Create, Start, Stop, Query or Delete any Windows SERVICE. The command options for SC are case sensitive

Usage
#####

.. code-block:: console

    SC GetKeyName "task scheduler"
    SC GetDisplayName schedule 
    SC start schedule
    SC QUERY schedule
    SC CONFIG "Schedule" start= disabled
    SC QUERY type= driver
    SC QUERY state= all |findstr "DISPLAY_NAME STATE" >svc_installed.txt 
    SC \\myServer CONFIG myService obj= LocalSystem password= mypassword
    SC CONFIG MyService binPath=c:\myprogram.exe obj=".\LocalSystem" password=""


References
**********
https://ss64.com/nt/sc.html
