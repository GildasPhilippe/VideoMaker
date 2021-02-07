const Process = () => {
    return (
        <div className="container">
            <h1 className="title">Processing</h1>
            <div className="columns is-centered">
                <p>
                    <button id="process-btn" className="button is-primary" onClick={process}>
                        Process my videos
                    </button>
                </p>
                <p id="process-response"></p>
            </div>
        </div>
    )
  }


function process(){
    console.log("processing")
    const url_process = 'http://localhost:5001/process/my5678super56testide543secret098my5678super56testide543secret098'
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
  
export default Process;