<!--A Design by W3layouts 
Author: W3layout
Author URL: http://w3layouts.com
License: Creative Commons Attribution 3.0 Unported
License URL: http://creativecommons.org/licenses/by/3.0/
-->
<!doctype html>
<html>
    <head>
        <title>iPear Login</title>
        <?php include 'view/header.php'; ?>
        <script type="application/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false); function hideURLbar(){ window.scrollTo(0,1); } </script>
    </head>
    <body>
        <h1 class="header">iPear</h1>
        <h4 class="subheader">Incident Priority Emergency Area Response</h4>
        <div class="log">
            <div class="content1 agileits">
                    <h2>Login</h2>
                    <form action="#" method="post">
                            <input type="email" name="email" value="Email Address" onfocus="this.value = '';" onblur="if (this.value == '') {this.value = 'Email Address';}">
                            <input type="password" name="psw" value="Password" onfocus="this.value = '';" onblur="if (this.value == '') {this.value = 'Password';}">
                            <div class="button-row">
                                    <input type="submit" class="sign-in" value="Sign In">
                                    <div class="clear"></div>
                            </div>
                    </form>
                    <h3><a href="new_user.php">No account? Create one!</a></h3>
            </div>
        </div>
        <?php include 'view/footer.php'; ?>
    </body>
</html>
