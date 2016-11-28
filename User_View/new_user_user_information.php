<!--Author: W3layouts
Author URL: http://w3layouts.com
License: Creative Commons Attribution 3.0 Unported
License URL: http://creativecommons.org/licenses/by/3.0/
-->



<!DOCTYPE HTML>
<html>
    <head>
        <title>iPear Account Creation</title>
        <?php include 'view/header.php'; ?>
    </head>
    <body>
        <div class="header w3ls">
            <h1 class="header">iPear</h1>
        </div>
        <!---main--->
        <div class="main">
            <div class="main-section agile">
                <div class="login-form">
                    <h2>User Information</h2>
                    <p>Please fill out all of the following fields. </p>
                    <form action="new_user_thankyou.php" method="post">
                        <!-- Temporarily commented out the required tag. --> 							
                        <ul>
                            <li class="text-info">First Name :</li>
                            <li><input type="text" name="first_name" placeholder="" ><!---required---></li>
                            <div class="clear"></div>
                        </ul>
                        <ul>
                            <li class="text-info">Last Name :</li>
                            <li><input type="text" name="last_name" placeholder="" ><!---required---></li>
                            <div class="clear"></div>
                        </ul>
                        <ul>
                            <li class="text-info">Age :</li>
                            <li><input type="text" name="age" placeholder="" ><!---required--->></li>
                            <div class="clear"></div>
                        </ul>
                        <ul>
                            <li class="text-info">Gender :</li>
                            <li><input type="text" name="gender" placeholder="" ><!---required---></li>
                            <div class="clear"></div>
                        </ul>
                        <ul>
                            <li class="text-info">Address :</li>
                            <li><input type="text" name="address=" placeholder="" ><!---required---></li>
                            <div class="clear"></div>
                        </ul>
                        <ul>
                            <li class="text-info">Email :</li>
                            <li><input type="text" name="email" placeholder="" ><!---required---></li>
                            <div class="clear"></div>
                        </ul>
                        <ul>
                            <li class="text-info">Allergies :</li>
                            <li><textarea name="allergies" placeholder="" ></textarea></li>
                            <div class="clear"></div>
                        </ul>
                        <ul>
                            <li class="text-info">Pre-Existing Conditions :</li>
                            <li><textarea name="conditions" placeholder="" ></textarea></li>
                            <div class="clear"></div>
                        </ul>
                        <input type="submit" value="Submit">
                        <div class="clear"></div>
                    </form>
                </div>
            </div>
            <?php include 'view/footer.php'; ?>
        </div>
    </body>
</html>
