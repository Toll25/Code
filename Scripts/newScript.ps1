$average = {`
    MemberType = "ScriptMethod"`
    Name = "getAverage"`
    Value = {`
        return [decimal]($this.sumOfScores / $this.numberOfScores)`
    }`
}

$scores=@{}
Import-Csv -Path C:\Users\pauli\Downloads\score_sample.csv | ForEach-Object {
    $vorname = $_."Vorname"
	$nachname = $_."Nachname"
	$score = [int]$_."Scores"

    $fullname = $vorname + " " + $nachname

    if($scores.ContainsKey($fullName)){
		$scores[$fullName].sumOfScores += $score
        $scores[$fullName].numberOfScores++
	}else{
		$scores.$fullName = [PSCustomObject]@{
            sumOfScores = $score
            numberOfScores = [int]'1'
        }
        Add-Member -InputObject $scores.$fullName $average
	}
    
} 
Write-Output "Fullname,Score" > results.csv
foreach($key in $scores.Keys){
    $averageScore = $scores[$key].getAverage()
    Write-Host $averageScore
	Write-Output "$key,$averageScore" >> results.csv
}