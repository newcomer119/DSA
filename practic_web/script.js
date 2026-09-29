// const count = document.getElementById("count");
// const increaseBtn = document.getElementById("increaseBtn");
// const decreaseBtn = document.getElementById("decreaseBtn");

// let currentCount = 0;
// increaseBtn.addEventListener("click", function (){
//     currentCount = currentCount + 1
//     count.textContent = currentCount
// })

// decreaseBtn.addEventListener("click", function (){
//     currentCount = currentCount - 1
//     count.textContent = currentCount
// })

// const num1 = document.getElementById("num1")
// const num2 = document.getElementById("num2")

// const addBtn = document.getElementById("addBtn")
// const result = document.getElementById("result")

// let total= 0;

// addBtn.addEventListener("click", function(){
//     const firstNumber = Number(num1.value)
//     const SecondNumber = Number(num2.value)
//     total = firstNumber  + SecondNumber
//     result.textContent = total    
// })

// const userName = document.getElementById("username");
// const password = document.getElementById("password");
// const message = document.getElementById("message");
// const loginButton = document.getElementById("loginBtn");

// loginButton.addEventListener("click", function () {
//     if (userName.value === "" || password.value === "") {
//         message.textContent = "Please fill all fields";
//     } else {
//         message.textContent = "Login successful!";
//     }
// });

// const box = document.getElementById("box")
// const toggleBtn = document.getElementById("toggleBtn")

// toggleBtn.addEventListener("click", function() {
//     box.classList.toggle("highlight")
// })

// const message = document.getElementById("message")
// const toggleBtn = document.getElementById("toggleVisibility")

// toggleBtn.addEventListener("click", function() {
//     if(message.style.display === "none"){
//         message.style.display = "block"
//     }else{
//         message.style.display = "none"
//     }
// })

// const textInput = document.getElementById("textInput")
// const upperBtn = document.getElementById("upperBtn")
// const clearBtn = document.getElementById("clearBtn")
// const para = document.getElementById("outputText")

// upperBtn.addEventListener("click", function(){
//     para.textContent = textInput.value.toUpperCase();
// })

// clearBtn.addEventListener("click", function(){
//     textInput.value = ""
//     para.textContent = ""
// })

const celsius = document.getElementById("celsius")
const convertBtn = document.getElementById("convertBtn")
const resetBtn = document.getElementById("resetBtn")
const result = document.getElementById("result")
let farentheit =0 
convertBtn.addEventListener("click", function(){
    // f = (9/5) * C + 32
    farentheit = ((9/5) * celsius.value) + 32
    result.textContent = farentheit
    

})
resetBtn.addEventListener("click", function(){
    celsius.value = ""
    result.value = ""
})