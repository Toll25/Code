class Rechteck {
	[float] $laenge
	[float] $breite

	Rechteck( [float] $laenge, [float] $breite) {
		$this.laenge=$laenge
		$this.breite=$breite
	}
	[float] getFlaeche() {
		return($this.laenge*$this.breite)
	}
}