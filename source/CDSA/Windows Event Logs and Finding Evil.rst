Windows Event Logs and Finding Evil
######################################

Sysmon (system monitor)
**************************

compose of: 1. A service 2. A device driver 3. event log

This can be downloaded and installed from the official MS page

https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon

and installed with:

.. code-block:: console

   C:\Tools\Sysmon> sysmon.exe -i -accepteula -h md5,sha256,imphash -l -n

To use a custom configuration, point the following at your custom.xml
file

.. code-block:: console

   C:\Tools\Sysmon> sysmon.exe -c filename.xml

Example files for configuration can be downloaded from:

https://github.com/SwiftOnSecurity/sysmon-config

C# injections can be detected using “Process Hacker”
https://processhacker.sourceforge.io/

MimiKatz is a tool used to dump credentials
https://github.com/gentilkiwi/mimikatz
