import VideoCard from "./VideoCard";

const Process = () => {
    const thumbnail_url = "/uploads/thumbnails/my5678super56testide543secret098my5678super56testide543secret999/f6227c6e5587badeebb05df62b27b4855c6c93a33d311f1ea713a7dd.png";
    const filename = "tonus.mp4";
    const title = "";
    const location = "";
    const start_at = 0;
    const end_at = 3;
    const video_date = "2018-12-20 00:56:22";

    return (
        <div className="container">
            <div className="box content">
                <VideoCard 
                    thumbnail_url={thumbnail_url}
                    filename={filename}
                    title={title}
                    location={location}
                    start_at={start_at}
                    end_at={end_at}
                    video_date={video_date}
                />
                <VideoCard 
                    thumbnail_url="/uploads/thumbnails/my5678super56testide543secret098my5678super56testide543secret999/af022125831fb5a308d0e0d343f056339d00d89575a9e3d06f6d685e.png"
                    filename={"concert.mp4"}
                    title={""}
                    location={location}
                    start_at={start_at}
                    end_at={end_at}
                    video_date={video_date}
                />
            </div>
            <div className="container">
                <div className="columns is-centered">
                    <p>
                        <button id="process-btn" className="button is-primary" onClick={process}>
                            Process my videos
                        </button>
                    </p>
                    <p id="process-response"></p>
                </div>
            </div>
        </div>
    )
}
/* https://bulmatemplates.github.io/bulma-templates/templates/forum.html#
 * https://github.com/BulmaTemplates/bulma-templates/blob/master/templates/forum.html

 * potentially : 
 * https://jamstackthemes.dev/theme/jekyll-bulma-theme/
 * */


function process(){
    console.log("processing")
    const url_process = 'http://server/process/my5678super56testide543secret098my5678super56testide543secret098'
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