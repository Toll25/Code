$scores=@{}
Import-Csv -Path C:\Users\pauli\Downloads\score_sample.csv | ForEach-Object {
	$vorname = $_."Vorname"
	$nachname = $_."Nachname"
	$score = [int]$_."Scores"
	$fullName = $nachname + " " + $vorname
	
	if($scores.ContainsKey($fullName)){
		$scores.$fullName += $score
	}else{
		$scores.$fullName = @()
		$scores.$fullName += $score
	}
}
echo "Fullname,Score" > results.csv

foreach($key in $scores.Keys){
	$RunningTotal = 0
	
	foreach($i in $scores[$key]){
		$RunningTotal += $i
	}
	
	$result=([decimal]($RunningTotal)/[decimal]($scores[$key].length))
	echo "$key,$result" >> results.csv
}
	