<?php
   $conn = mysqli_connect("localhost","root","","stroke");
   if($conn==FALSE)
   {
	   echo "Connection Failed";
   }

$id=0;
$name="";
$gender ="";
	  $age  = "";
	  $hyp = "";
	  $hd  = "";
	  $em = "";
	  $wtp = "";
	  $rest ="";
      $agl ="";
      $bmi ="";
      $ss ="";
	  $result ="";


   if(isset($_POST['predict']))
   {
    $name=$_POST['name'];
	   $gender = $_POST['gender'];
	  $age  = $_POST['age'];
	  $hyp = $_POST['hyp'];
	  $hd  = $_POST['hd'];
	  $em = $_POST['em'];
      
	  $wtp = $_POST['wtp'];
	  $rest =$_POST['rest'];
      $agl =$_POST['agl'];
      $bmi =$_POST['bmi'];
      $ss =$_POST['ss'];

	  $que = "insert into `data`(`name`, `gender`, `age`, `hypt`, `hd`, `em`, `wt`, `rt`, `agl`, `bmi`, `ss`)values('$name','$gender','$age','$hyp','$hd','$em','$wtp','$rest','$agl','$bmi','$ss')";
	  $res = mysqli_query($conn,$que);
	  if($res)
	  {
		$id = mysqli_insert_id($conn);
	  }
	  else{
		echo '<script> alert("Not Record Inserted Successfully.Tryagain!!!"); </script>';
		echo '<script> location.href="book.html"; </script>';
   }
   $ans =  shell_exec("python C:/xampp/htdocs/marvel/test.py $id");

		if($ans==1 || $ans=='1')
		{
			$result="Stroke";
		}
		else if($ans==0 || $ans=='0'){
			$result="No Stroke";
		}
	}
		?>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>Record Table</title>
			<link rel="stylesheet" type="text/css" href="css/bootstrap.css" />
			<style>
				body{
					padding:50px;
				}
				table {
					width: 100%;
					border-collapse: collapse;
					margin-bottom: 20px;
				}
		
				th, td {
					border: 1px solid #dddddd;
					text-align: left;
					padding: 8px;
				}
		
				th {
					background-color: #f2f2f2;
				}
			</style>
		</head>
		<body>
		
		<?php
			// Assuming you have the variables already defined
		
			echo '<table>';
			echo '<tr><th>Field</th><th>Value</th></tr>';
			echo '<tr><td>Name</td><td>' . $name . '</td></tr>';
			echo '<tr><td>Gender</td><td>' . $gender . '</td></tr>';
			echo '<tr><td>Age</td><td>' . $age . '</td></tr>';
			echo '<tr><td>Hypertension</td><td>' . $hyp . '</td></tr>';
			echo '<tr><td>Heart Disease</td><td>' . $hd . '</td></tr>';
			echo '<tr><td>Ever Married</td><td>' . $em . '</td></tr>';
			echo '<tr><td>Work Type</td><td>' . $wtp . '</td></tr>';
			echo '<tr><td>Residence Type</td><td>' . $rest . '</td></tr>';
			echo '<tr><td>Avg Glucose Level</td><td>' . $agl . '</td></tr>';
			echo '<tr><td>BMI</td><td>' . $bmi . '</td></tr>';
			echo '<tr><td>Smoking Status</td><td>' . $ss . '</td></tr>';
			echo '<tr><td>Result</td><td>' . $result . '</td></tr>';
			echo '</table>';
			echo '<a href="book.html"><button type="submit" class="btn" style="background-color:black;color:white;padding:5px;width: 15%;">Back</button></a>';
		?>
		
		</body>
		</html>
		

