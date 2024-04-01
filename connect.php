<?php
$rating = $_POST['rating'];
$date = $_POST['date'];
$variation = $_POST['variation'];
$verified_reviews = $_POST['verified_reviews'];
$feedback = $_POST['feedback'];

$csvData = "$rating,$date,$variation,$verified_reviews,$feedback\n";

$csvFile = 'output.csv';
$file = fopen($csvFile, 'a'); 
fwrite($file, $csvData);
fclose($file);

// Echo JavaScript to show alert after PHP processing
echo '<script>alert("Recorded Inserted");</script>';
// Redirect after a slight delay to allow the alert to display
echo '<script>window.setTimeout(function(){ window.location.href = "home.html"; }, 1000);</script>';
?>
