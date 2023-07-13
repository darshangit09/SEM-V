<?php
$a = array("Sophia" => "31","Jacob" => "41","William" => "39","Ramesh" => "40");
asort($a);
echo "<table>";
echo "<tr><th>Name</th><th>Age</th></tr>";
foreach ($a as $name => $age) 
{
    echo "<tr><td>$name</td><td>$age</td></tr>";
}
echo "</table>";
?>
