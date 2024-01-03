<html>
    <head>
        <style>
            #reg{
                background-color: aqua;
                width: fit-content;
    height:fit-content ;
    border-style: outset;padding: 20px;
    
            }
</style>
    </head>
    <body><center>
        <div id="reg"><br>
        <h3>ART GALLERY MANAGEMENT</H3><BR><br>
        <form name="form" onsubmit="return validationform()" method="post">
        <label for="name">NAME OF WORK:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="date">CREATED_DATE:</label>
        <input type="date" id="date" name="date"><br><br>
        <label for="type">TYPE OF ART:</label>
        <input type="text" id="type" name="arttype"><br><br>
        <input type="submit" value="submit" name="submit">

</form>
        <script>
        function validationform()
        {
            var name = document.forms["form"]["name"].value;
            var date = document.forms["form"]["date"].value;
            var arttype = document.forms["form"]["arttype"].value;
if (name === "")
{
     alert("Name is required");
    return false;
}
if (date === "")          
{
    alert("date is required ");
     return false;
}
if (arttype === "")
{
    alert("enter type");
    return false;
}
        }
        </script>
<?php
$conn=mysqli_connect("localhost","root","","exam");
if(!$conn)
{
    die("Connection failed: " . mysqli_connect_error());
}
echo"connection sucess";

if (isset($_POST['submit']))
{
    $name=$_POST['name'];
    $date=$_POST['date'];
    $type=$_POST['arttype'];
    echo '<br>';
    echo $name,'<br>';
    echo  $date,'<br>';
    echo $type,'<br>';

$sql="INSERT INTO manage(NAME,DATE_CREATED,TYPE)VALUES('$name','$date','$type')";
if (mysqli_query($conn, $sql)) {

    echo "New record created successfully";
    
    } else {
    
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
    
    }
    
    mysqli_close($conn);
}
?></center>
</div>
</body>
</html>




