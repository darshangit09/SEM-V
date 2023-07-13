<?php
$firstString = "Hello, hello, how are you?";
$secondString = "hello";

$occurrences = substr_count(strtolower($firstString), strtolower($secondString));
echo "Number of occurrences: " . $occurrences;
$a = strpos($firstString,$secondString);
echo "$a";
?>

