Enumerating Security Controls
###############################

Date: 2024-12-22 14:00:03

Status: #new

Tags: :ref:`active directory enumeration attacks`

Description
************

Once you have foothold it is imparative to evaluate the security controls that have been
implemented.  This will help you understand what would be the most effective and viable tools used 
in your testing.

Security controls
*******************

Microsoft Defender
===================

Defender has been greatly improved since 2020, and will activley block tools like :ref:`powerview`. 

To return the status of defender, use the utiity 

.. code-block:: powershell

    PS C:\htb> Get-MpComputerStatus

    AMEngineVersion                 : 1.1.17400.5
    AMProductVersion                : 4.10.14393.0
    AMServiceEnabled                : True
    AMServiceVersion                : 4.10.14393.0
    AntispywareEnabled              : True
    AntispywareSignatureAge         : 1
    AntispywareSignatureLastUpdated : 9/2/2020 11:31:50 AM
    AntispywareSignatureVersion     : 1.323.392.0
    AntivirusEnabled                : True
    AntivirusSignatureAge           : 1
    AntivirusSignatureLastUpdated   : 9/2/2020 11:31:51 AM
    AntivirusSignatureVersion       : 1.323.392.0
    BehaviorMonitorEnabled          : False
    ComputerID                      : 07D23A51-F83F-4651-B9ED-110FF2B83A9C
    ComputerState                   : 0
    FullScanAge                     : 4294967295
    FullScanEndTime                 :
    FullScanStartTime               :
    IoavProtectionEnabled           : False
    LastFullScanSource              : 0
    LastQuickScanSource             : 2
    NISEnabled                      : False
    NISEngineVersion                : 0.0.0.0
    NISSignatureAge                 : 4294967295
    NISSignatureLastUpdated         :
    NISSignatureVersion             : 0.0.0.0
    OnAccessProtectionEnabled       : False
    QuickScanAge                    : 0
    QuickScanEndTime                : 9/3/2020 12:50:45 AM
    QuickScanStartTime              : 9/3/2020 12:49:49 AM
    RealTimeProtectionEnabled       : True
    RealTimeScanDirection           : 0
    PSComputerName                  :


App Locker
============

This application created by Microsoft White/black lists applications.  Most commonly `cmd.exe` and `powershell.exe` are blocked from running, and or 
what folders they can write too.  Even though these are blocked, sometimes alternate locations can be run `%SystemRoot%\SysWOW64\WindowsPowerShell\v1.0\powershell.exe or PowerShell_ISE.exe`

To examine the policy details we can run:

.. code-block:: powershell

    PS C:\htb> Get-AppLockerPolicy -Effective | select -ExpandProperty RuleCollections

    PathConditions      : {%SYSTEM32%\WINDOWSPOWERSHELL\V1.0\POWERSHELL.EXE}
    PathExceptions      : {}
    PublisherExceptions : {}
    HashExceptions      : {}
    Id                  : 3d57af4a-6cf8-4e5b-acfc-c2c2956061fa
    Name                : Block PowerShell
    Description         : Blocks Domain Users from using PowerShell on workstations
    UserOrGroupSid      : S-1-5-21-2974783224-3764228556-2640795941-513
    Action              : Deny

    PathConditions      : {%PROGRAMFILES%\*}
    PathExceptions      : {}
    PublisherExceptions : {}
    HashExceptions      : {}
    Id                  : 921cc481-6e17-4653-8f75-050b80acca20
    Name                : (Default Rule) All files located in the Program Files folder
    Description         : Allows members of the Everyone group to run applications that are located in the Program Files folder.
    UserOrGroupSid      : S-1-1-0
    Action              : Allow

    PathConditions      : {%WINDIR%\*}
    PathExceptions      : {}
    PublisherExceptions : {}
    HashExceptions      : {}
    Id                  : a61c8b2c-a319-4cd0-9690-d2177cad7b51
    Name                : (Default Rule) All files located in the Windows folder
    Description         : Allows members of the Everyone group to run applications that are located in the Windows folder.
    UserOrGroupSid      : S-1-1-0
    Action              : Allow

    PathConditions      : {*}
    PathExceptions      : {}
    PublisherExceptions : {}
    HashExceptions      : {}
    Id                  : fd686d83-a829-4351-8ff4-27c7de5755d2
    Name                : (Default Rule) All files
    Description         : Allows members of the local Administrators group to run all applications.
    UserOrGroupSid      : S-1-5-32-544
    Action              : Allow

PowerShell Constrained Language Mode
=====================================

https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/

This is a mode that restricts the usage of powershell modules (such as COM objects), to see if we are in a restricted mode we 
can run:

.. code-block:: powershell

    PS C:\htb> $ExecutionContext.SessionState.LanguageMode

    ConstrainedLanguage

Local Administrator Password Solution (LAPS)
=============================================

:ref:`laps`


Local Administrator Password Solution (LAPS) toolkit
=====================================================

:ref:`LAPSToolkit`

References
************
https://academy.hackthebox.com/module/143/section/1459