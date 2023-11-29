 using module .\RechteckObject\RechteckObject.psm1

$rechteck = [Rechteck]::new(8,5);
Write-Output $rechteck.getFlaeche();