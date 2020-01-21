<!DOCTYPE html>
<html>
<head>
	<title>SignUp</title>
</head>
<body>
<h1>URL Discovery</h1>
<form method="post" action="index.php">
	URL: <input type="text" name="url"><br><br>
	<input type="submit" name="send">
</form>

</body>
</html>

<?php

function main(){
	
	if ($_POST['url']) {

		#getting and filtering the user input
		$urlInitial = $_POST['url'];
		$urlFiltered = filter_var($urlInitial, FILTER_SANITIZE_URL);
		#echo $urlFiltered;

		$pathScript = "/home/jsabino/PycharmProjects/urldiscover/urldiscovery.py $urlFiltered";
		echo $pathScript;

		if (function_exists('system')) {
			ob_start();
			system($pathScript, $return);
			$output = ob_get_contents();
			echo $output;
			ob_end_clean();
		}



	}
}

main();



?>