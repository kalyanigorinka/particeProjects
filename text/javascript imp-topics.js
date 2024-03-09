//variabale
var Name = "kalyani";
console.log(Name);

// data types
var a ="kalyani";
console.log(typeof a);

var b =5;
console.log(typeof b);

var c =true;
console.log(typeof c);

var d = 
console.log(typeof (d));

//array
var a = [1,2,3,4,5]
console.log(a);
//object
var data = {
    name : "kalyani",
    age : 21
}
console.log(data.name,data.age);

//functions
function user(num2){
    return num2+10 
}
 var output = user(10);
//functions-2
function user(num){
    console.log(num);
}
user(124);

//conditional statement
var ganga = "gangabhavani";
if(ganga=="gangabhavani"){
    console.log("bhavani");
}else{
    console.log("gorinkagangabhavani");
}

//looping concept







//array features

//isArray
var a = [1,2,3,4,5]
console.log(Array.isArray(a));

//map 
var a = [1,2,3,4,5]
a.map(
  function(element){
    console.log(element);
  }  
);

//map_return values
var a = [1,2,3,4,5]
var output = a.map(
  function(element){
    return element+2
  }  
)
console.log(output);

//filter
var a = [1,2,3,4,5]
var output = a.filter(
  function(element){
    return element>2
  }  
)
console.log(output);

//forEach
var a = [1,2,3,4,5]
a.forEach(
  function(element){
    console.log(element);
  }  
)

//every
var a = [1,2,3,4,5]
var output = a.every(
  function(element){
    return element>2
  }  
)
console.log(output)

//some
var a = [1,2,3,4,5]
var output = a.some(
  function(element){
    return element+2
  }  
)
console.log(output)

//indexof
var a = [1,2,3,4,5]
console.log(a.indexOf(5));


//lastindexof
var a = [1,2,3,4,5,3,6,8]
console.log(a.lastIndexOf(3));

//stringify
var data = {
    name : "ammu",
    age : 21
}
var json = JSON.stringify(data);
console.log(data);

//valueof
var date = new Date();
console.log(date.valueOf());

//object.keys(): a simpel way to iterate over an object and return all of the object.keys()
var employee = {
  name:"ranga",
  age:21,
  role:"node.js",
  level:1
  };
  console.log(Object.keys(employee));
  //output:[ 'name', 'age', 'role', 'level' ]
  
  //object.values: iterate over the object and return the object.values
  var employee ={
      name : "ammu",
      age:21,
      role: "express.js",
      level:"1"
  };
  console.log(Object.values(employee));
  
  //object.entries
  
  var drinks ={
      mango:"out of stock",
      apple:3.5
  }
  
  for(const[name,cost]of
      Object.entries(drinks)){
          console.log(`${name}:${cost}`);
      }
      //object.create
      var student={
          name:"ranju",
          display(){
              console.log("name",this.name);
          }
      };
      let std1 = Object.create(student);
  
      std1.name="ammu";
      std1.display();
  
      //object.asign()
      var target={a:1,b:7};
      var source={b:0,c:5};
  
      var returnTarget=Object.assign(target,source);
  
      console.log(target);
      console.log(returnTarget);
  
      //object.seal()
  var bike = {
      price:20000
  };
  
  Object.seal(bike);
  bike.price=30000
  console.log(bike.price);
  
  delete bike.price;
  console.log(bike.price);

  //even and odd functions
  function user(num1){
    if(num1%2==0){
        return "even"
    }else{
        return "odd"
    }
}
var output=user(21);
console.log(output)
