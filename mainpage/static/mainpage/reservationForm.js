const setOption = (content) => {
    let newOption = document.createElement("option");
    var newContent = document.createTextNode(content);
    newOption.appendChild(newContent);
    document.getElementById('time').appendChild(newOption)
}

const changeTimes = () => {
    document.getElementById('time').innerHTML = '';
    selected_day = document.getElementById('day').value
    if(js_days_dic){
        js_days_dic[selected_day].map(time => setOption(time))
    }
   
}

document.body.onload = changeTimes(); 