<!DOCTYPE html>
<html>
<head>
    <title>Simple Interest Calculator</title>
</head>
<body>
    <h1>Simple Interest Calculator</h1>
    <form method="post">
        Loan Amount: <input type="number" name="loan_amount" required><br>
        Rate of Interest (%): <input type="number" name="interest_rate" required><br>
        Years: <input type="number" name="years" required><br>
        <input type="submit" name="calculate" value="Calculate">
    </form>

    <?php
    function calculateSimpleInterest($loan_amount, $interest_rate, $years) {
        $simple_interest = ($loan_amount * $interest_rate * $years) / 100;
      
        echo "<p>Loan Amount: $loan_amount</p>";
        echo "<p>Rate of Interest: $interest_rate%</p>";
        echo "<p>Years: $years</p>";
        echo "<p>Simple Interest: $simple_interest</p>";
      }
      
    if(isset($_POST['calculate'])) {
        $loan_amount = $_POST['loan_amount'];
        $interest_rate = $_POST['interest_rate'];
        $years = $_POST['years'];

        calculateSimpleInterest($loan_amount, $interest_rate, $years);
    }
    ?>
</body>
</html>
