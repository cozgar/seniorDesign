<!--Author: W3layouts
Author URL: http://w3layouts.com
License: Creative Commons Attribution 3.0 Unported
License URL: http://creativecommons.org/licenses/by/3.0/
-->
<!DOCTYPE HTML>
<html
    <head>
        <?php include 'view/header.php'; ?>
        <title>iPear Account Creation</title>
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
                    <form action="new_user_user_information.php" method="post">
                    <!-- Temporarily commented out the required tag. -->
                        <ul>
                            <li class="text-info">Username :</li>
                            <li><input type="text" id="username" name="username" placeholder="" ><!---required---></li>
                            <div class="clear"></div>
                        </ul>
                        <ul>
                            <li class="text-info">Password :</li>
                            <li><input type="text" name="password" placeholder="" ><!---required---></li>
                            <div class="clear"></div>
                        </ul>
                        <ul>
                            <li class="text-info">Re-enter Password :</li>
                            <li><input type="text" name="password_check" placeholder="" ><!---required--->></li>
                            <div class="clear"></div>
                        </ul>
                        <ul>
                            <li class="text-info">Phone Number :</li>
                            <li><input type="text" name="phone_number" placeholder="" ><!---required---></li>
                            <div class="clear"></div>
                        </ul>
                        <input type="submit" value="Create And Continue">
                        <div class="clear"></div>
                    </form>
                </div>
            </div>
        </div>
        <?php include 'view/footer.php'; ?>
        <!---main--->
    </body>
</html>
