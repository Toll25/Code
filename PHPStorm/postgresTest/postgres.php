<?php
// Connecting, selecting database
$dbconn = pg_connect("host=localhost dbname=test user=superuser")
or die('Could not connect: ' . pg_last_error());

// Performing SQL query
$query = 'select * from "testTable";';
$result = pg_query($query) or die('Query failed: ' . pg_last_error());

// Printing results in HTML
echo "<table>\n";

// Printing table header with column names
echo "\t<tr>\n";
for ($i = 0; $i < pg_num_fields($result); $i++) {
    $fieldName = pg_field_name($result, $i);
    echo "\t\t<th>$fieldName</th>\n";
}
echo "\t</tr>\n";

// Printing data rows with column values
while ($line = pg_fetch_assoc($result)) {
    echo "\t<tr>\n";
    foreach ($line as $col_name => $col_value) {
        echo "\t\t<td>$col_value</td>\n";
    }
    echo "\t</tr>\n";
}
echo "</table>\n";

// Free resultset
pg_free_result($result);

// Closing connection
pg_close($dbconn);
?>
