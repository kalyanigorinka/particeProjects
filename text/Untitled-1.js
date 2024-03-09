// for each
const arr = ["football","cricket","hpckey"];
arr.forEach((element)=>{
    if(element=="football"){
        arr.push("golf");
    }
});
console.log(arr);
