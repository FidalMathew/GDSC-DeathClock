
async function sendData(inputValues) {

  console.log(parseInt(inputValues[0]))

  try {
    let res = await fetch("http://localhost:5000/", {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ "data1": parseInt(inputValues[0]) })
    })
    res = await res.text()
    res = JSON.parse(res)
    console.log(res)
    return res

  } catch (error) {
    console.log(error)
  }


}


let data1 = document.getElementById("data1")
let data2 = document.getElementById("data2")
let data3 = document.getElementById("data3")


let result = document.getElementById("result")

let btn = document.getElementById("btn")

let inputValues = []

btn.addEventListener("click", async () => {

  inputValues.push(data1.value)
  inputValues.push(data2.value)
  console.log(inputValues)

  rex = await sendData(inputValues)
  result.innerText = rex.pred
})
