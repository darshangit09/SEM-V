<?php
$a = "hello world";
$b = str_split($a);
$c = array_unique($b);
$d = implode("", $c);
echo $d;
?>

