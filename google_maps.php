<?php
    if(isset($_POST["submit_address"]))
    {
        $address = $+POST["address"];
        ?>
        <iframe width="100%" height ="500" src="https://maps.google.com/maps?q=<?php echo $address; ?>&"></iframe>
        <?php
    }
?>
<form method="POST">
    <p>
        <input type = "text" name="address" placeholder= "Enter address">
    </p>

    <input type ="submit" name="submit_address">
</form>