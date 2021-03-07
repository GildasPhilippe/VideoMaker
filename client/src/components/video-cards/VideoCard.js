import { useEffect, useState } from 'react';
import Thumbnail from "./Thumbnail";
import TimeSlider from "./TimeSlider";


const VideoCard = ({video}) => {
    let title = video.title;
    let location = video.location;
    let video_date = video.video_date;
    const [start_at, setStartAt] = useState(video.start_at);
    const [end_at, setEndAt] = useState(video.end_at);
    
    let timeoutId;
    const autoSave = () => {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(function() {
            fetch(`http://localhost:5001/videos/${video.session_id}/${video.file_hash}`, {
                method: 'PUT',
                headers: {
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    "title": title,
                    "location": location,
                    "video_date": video_date,
                    "start_at": start_at,
                    "end_at": end_at,
                })
            }).then(
                function(response){
                    if(response.status === 200) console.log("Data well updated");
                    else console.log(`[${response.status}] ${response.data["message"]}`)
                }
            ).catch(function(err) {console.log('Fetch Error : ', err);});
        }, 1000);
    }

    const updateTitle = (e) => { title = e.target.value }
    const updateLocation = (e) => { location = e.target.value }
    const updateVideoDate = (e) => { video_date = e.target.value }
    const unescape = (string) => {
        return new DOMParser().parseFromString(string,'text/html').querySelector('html').textContent;
    }


   useEffect(() => {
        let videoCardInputs = document.querySelectorAll(`#video-card-${video.file_hash} input`);
        videoCardInputs.forEach(videoCardInput => {
            videoCardInput.addEventListener('input', function() {autoSave()});
        });
    });  

    // TODO: component for inputs
    return (
        <article className="post" id={`video-card-${video.file_hash}`}>
            <div className="columns">
                <div className="column is-one-third">
                    <Thumbnail thumbnail_url={video.thumbnail_url}/>
                </div>
                <div className="column">
                    <h3 className="is-spaced">{video.filename}</h3>
                    <div className="media columns is-multiline ">

                        <div className="column">
                            <div className="field">
                                <p className="control has-icons-left">
                                <input
                                    className="input is-rounded is-small" 
                                    type="text" placeholder="Title" 
                                    defaultValue={title ? unescape(title) : undefined}
                                    onChange={updateTitle}
                                />
                                    <span className="icon is-small is-left">
                                    <i className="far fa-bookmark"></i>
                                    </span>
                                </p>
                            </div>
                            <div className="columns">
                                <div className="field column is-half">
                                    <p className="control has-icons-left">
                                        <input 
                                            className="input is-rounded is-small" 
                                            type="text" 
                                            placeholder="Location"
                                            defaultValue={location ? unescape(location) : undefined}
                                            onChange={updateLocation}
                                        />
                                        <span className="icon is-small is-left">
                                            <i className="fas fa-map-marker-alt"></i>
                                        </span>
                                    </p>
                                </div>
                                <div className="field column is-half">
                                    <p className="control has-icons-left">
                                        <input 
                                            className="input is-rounded is-small" 
                                            type="datetime-local" 
                                            placeholder="YYY-MM-DD HH:MM:SS"
                                            defaultValue={video_date ? unescape(video_date) : undefined}
                                            onChange={updateVideoDate}
                                        />
                                        <span className="icon is-small is-left">
                                            <i className="far fa-calendar-alt"></i>
                                        </span>
                                    </p>
                                </div>
                            </div>
                        </div>

                        <div className="column is-full">
                            <TimeSlider 
                                start_at={start_at}
                                end_at={end_at}
                                duration={video.duration}
                                setStartAt={setStartAt}
                                setEndAt={setEndAt}
                                autoSave={autoSave}
                            />
                        </div>
                    </div>
                </div>
            </div>
        </article>
    )
};


export default VideoCard;