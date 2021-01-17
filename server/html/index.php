<html>
<head>

<?php

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ERROR);

$input_state_file_location = "/srv/input_state.json";

function setBotControlValue($bot_id, $control, $new_val) {
    global $input_state_file_location;
    
    $old_input_state_encoded = file_get_contents($input_state_file_location);
    
    $mutable_input_state = json_decode($old_input_state_encoded, true);

    settype($new_val, gettype($mutable_input_state[$bot_id][$control]));
    $mutable_input_state[$bot_id][$control] = $new_val;
    // print_r($mutable_input_state);
    $new_encoded = json_encode($mutable_input_state);
    // echo $new_encoded;
    
    $write_file = fopen($input_state_file_location, "w");
    fwrite($write_file, $new_encoded);
    fclose($write_file);
}

$bot_id = $_POST["id"];
$bot_control = $_POST["control"];
$value = $_POST["value"];

?>

</head>
<body>

<!-- <div id="elm"></div> -->

<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
    bot: <input type="text" name="id"><br>
    control: <input type="text" name="control"><br>
    value: <input type="text" name="value"><br>
    <input type="submit" name="Go!">
</form>
<br><br>

<?php

if (isset($bot_id) && isset($bot_control) && isset($value)) {
    if (setBotControlValue($bot_id, $bot_control, $value)) {
        echo "Values set.";
    }
}
else {
    // echo "error: not all values found.";
}
?>

</body>
</html> 