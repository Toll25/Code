$flaeche = {`
    MemberType = "ScriptMethod"`
    Name = "getFlaeche"`
    Value = {`
        return $this.laenge * $this.breite`
    }`
}

$rechteck=[PSCustomObject]@{
    $laenge = 4;
    $breite = 5;
}

Add-Member -InputObject $rechteck $flaeche

$rechteck.getFlaeche()