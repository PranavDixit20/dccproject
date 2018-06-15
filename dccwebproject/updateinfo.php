<?php
$user_name = "root";
$user_pass = "";
$host_name = "localhost";
$db_name = "djangodatabase";

$con = mysql_connect($host_name,$user_name,$user_pass,$db_name);

if($con)
{
	$image = $_POST["image"];
	$image_name = $_POST["image_name"];
	$engg_name = $_POST["engg_name"];
	$sql = "update loginapp_engg set engg_pic = '$image_name'  where engg_name = '$engg_name' ";
	$upload_path = "dccproject/dccwebproject/dccwebproject/loginapp/media/co_pic/$image_name.jpg";
	
	if(mysql_query($con,$sql))
	{
		file_put_contents($upload_path,base64_decode($image));
		echo json_encode(array('response'->'Image Uploaded Successfully'));
		
	}
	else
	{
		echo json_encode(array('response'->'Image upload failed'));
	}
}
else
{
	echo json_encode(array('response'->'Image Upload Failed'));
}

mysql_close($con);

?>
