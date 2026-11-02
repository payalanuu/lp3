// SPDX-License-Identifier: MIT
 pragma solidity 0.8.38;

 contract BankAccount {

     mapping(address => uint256) private balances;

     event Deposited(address indexed user, uint256 amount);
     event Withdrawn(address indexed user, uint256 amount);

     // Deposit Ether into the account
     function deposit() public payable {
         require(msg.value > 0, "Deposit must be positive");

         balances[msg.sender] += msg.value;

         emit Deposited(msg.sender, msg.value);
     }

     // Withdraw Ether from the account
     function withdraw(uint256 amount) public {
         require(amount > 0, "Amount must be positive");
         require(
             balances[msg.sender] >= amount,
             "Insufficient balance"
         );

         balances[msg.sender] -= amount;

         (bool success, ) =
             payable(msg.sender).call{value: amount}("");

         require(success, "Transfer failed");

         emit Withdrawn(msg.sender, amount);
     }

     // Display the caller's balance
     function getBalance() public view returns (uint256) {
         return balances[msg.sender];
     }
 }