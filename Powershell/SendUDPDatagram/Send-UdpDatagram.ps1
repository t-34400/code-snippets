# This code is borrowed from https://gist.github.com/PeteGoo/21a5ab7636786670e47c

function Send-UdpDatagram
{
      Param ([string] $EndPoint, 
      [int] $Port, 
      [string] $Message)

      $IP = [System.Net.Dns]::GetHostAddresses($EndPoint) 
      $Address = [System.Net.IPAddress]::Parse($IP) 
      $EndPoints = New-Object System.Net.IPEndPoint($Address, $Port) 
      $Socket = New-Object System.Net.Sockets.UDPClient 
      $EncodedText = [Text.Encoding]::ASCII.GetBytes($Message) 
      $Socket.Send($EncodedText, $EncodedText.Length, $EndPoints) 
      $Socket.Close() 
}

Send-UdpDatagram -EndPoint "127.0.0.1" -Port 8125 -Message "test.mymetric:0|c"