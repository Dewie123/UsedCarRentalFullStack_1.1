let selectedSmartRate = 2.48;
let selectedBankRate = 2.48;

function selectRate(useType, smartRate, bankRate) {
    // Set the selected rates
    selectedSmartRate = smartRate;
    selectedBankRate = bankRate;

    // Recalculate loan with the updated rates
    calculateLoan();

    // Highlight the selected option
    const rateOptions = document.querySelectorAll('.rate-option');
    rateOptions.forEach(option => option.classList.remove('active'));
    event.currentTarget.classList.add('active');
}

function calculateLoan() {
    const loanAmount = parseFloat(document.getElementById('loanAmount').value);
    const loanTerm = parseInt(document.getElementById('loanTerm').value);

    // Validate the loan amount and term
    if (!loanAmount || !loanTerm) {
        return;
    }

    // Convert annual interest rates to monthly rates
    const smartLoanMonthlyRate = selectedSmartRate / 100 / 12;
    const bankLoanMonthlyRate = selectedBankRate / 100 / 12;

    // Calculate monthly payments for both loans
    const monthlyPaymentSmartLoan = (loanAmount * smartLoanMonthlyRate) / (1 - Math.pow(1 + smartLoanMonthlyRate, -loanTerm));
    const totalPaidSmartLoan = monthlyPaymentSmartLoan * loanTerm;

    const monthlyPaymentBankLoan = (loanAmount * bankLoanMonthlyRate) / (1 - Math.pow(1 + bankLoanMonthlyRate, -loanTerm));
    const totalPaidBankLoan = monthlyPaymentBankLoan * loanTerm;

    // Calculate potential savings
    const savings = totalPaidBankLoan - totalPaidSmartLoan;

    // Update the UI with the calculated values
    document.getElementById('monthlyInstalment1').innerText = "$" + monthlyPaymentSmartLoan.toFixed(2);
    document.getElementById('totalPaid1').innerText = "Total Paid on Loan: $" + totalPaidSmartLoan.toFixed(2);

    document.getElementById('monthlyInstalment2').innerText = "$" + monthlyPaymentBankLoan.toFixed(2);
    document.getElementById('totalPaid2').innerText = "Total Paid on Loan: $" + totalPaidBankLoan.toFixed(2);

    // Update the savings text
    document.getElementById('savingsText').innerText = savings > 0 
        ? `You will save $${savings.toFixed(2)} with us!` 
        : `You will save $0 with us!`;
}

// Attach input change events to trigger the calculation
document.getElementById('loanAmount').addEventListener('input', calculateLoan);
document.getElementById('loanTerm').addEventListener('change', calculateLoan);