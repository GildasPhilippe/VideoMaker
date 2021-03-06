function runProcess(session_id){
    console.log("processing")
    const url_process = `http://server/process/${session_id}`
    var request = new XMLHttpRequest();
    request.open('PUT', url_process, true);
    request.responseType = "json"
    request.onload = function() {
      if (this.status >= 200 && this.status < 400) {
        document.getElementById("process-response").innerHTML = this.response.data
      } else {
        alert('Error ' + this.status)
      }
    };
    request.onerror = function() {
      alert('Failed to process!');
    };
    request.send();
}

export default runProcess;