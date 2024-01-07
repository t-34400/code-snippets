# This code is borrowed from https://gist.github.com/PeteGoo/21a5ab7636786670e47c

function Send-UdpDatagram
{
      Param ([string] $endPoint, 
      [int] $port, 
      [string] $message)

      $ip = [System.Net.Dns]::GetHostAddresses($endPoint) 
      $address = [System.Net.IPAddress]::Parse($ip) 
      $endPoints = New-Object System.Net.IPEndPoint($address, $port) 
      $socket = New-Object System.Net.Sockets.UDPClient 
      $encodedText = [Text.Encoding]::ASCII.GetBytes($message) 
      $socket.Send($encodedText, $encodedText.Length, $endPoints) 
      $socket.Close() 
}

function Send-UdpDatagram_Float {
      Param ([string] $endPoint, 
            [int] $port, 
            [System.Object[]] $dataToSend)

      $ip = [System.Net.Dns]::GetHostAddresses($endPoint) 
      $address = [System.Net.IPAddress]::Parse($ip) 
      $endPoints = New-Object System.Net.IPEndPoint($address, $Port) 
      $socket = New-Object System.Net.Sockets.UDPClient 
      $binaryData = $dataToSend | ForEach-Object { [BitConverter]::GetBytes($_) }
      $socket.Send($binaryData, $binaryData.Length, $endPoints) 
      $socket.Close() 
}

# Send-UdpDatagram -endPoint "127.0.0.1" -port 5005 -message "test.mymetric:0|c"
Send-UdpDatagram_Float -endPoint "127.0.0.1" -port 5005 -dataToSend @(1.23, 4.56, 7.89)
