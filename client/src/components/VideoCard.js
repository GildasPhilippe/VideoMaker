import Thumbnail from "./Thumbnail";
import TimeSlider from "./TimeSlider";

const VideoCard = ({thumbnail_url, filename, title, location, start_at, end_at, video_date}) => {
    console.log("title = " + title)
    console.log("location = " + location)
    console.log("video_date = " + video_date)
    return (
        <article className="post">
            <div className="columns">
                <div className="column is-one-third">
                    <Thumbnail thumbnail_url={thumbnail_url}/>
                </div>
                <div className="column">
                    <h3 className="is-spaced">{filename}</h3>
                    <div className="media columns is-multiline ">

                        <div className="column">
                            <div className="field">
                                <p className="control has-icons-left">
                                <input className="input is-rounded is-small" type="text" placeholder="Title"/>
                                    <span className="icon is-small is-left">
                                    <i className="far fa-bookmark"></i>
                                    </span>
                                </p>
                            </div>
                            <div className="columns">
                                <div className="field column is-half">
                                    <p className="control has-icons-left">
                                        <input className="input is-rounded is-small" type="text" placeholder="Location"/>
                                        <span className="icon is-small is-left">
                                            <i className="fas fa-map-marker-alt"></i>
                                        </span>
                                    </p>
                                </div>
                                <div className="field column is-half">
                                    <p className="control has-icons-left">
                                        <input className="input is-rounded is-small" type="date" placeholder="Date"/>
                                        <span className="icon is-small is-left">
                                            <i className="far fa-calendar-alt"></i>
                                        </span>
                                    </p>
                                </div>
                            </div>
                        </div>

                        <div className="column is-full">
                            <TimeSlider start_at={start_at} end_at={end_at}/>
                        </div>
                    </div>
                </div>
            </div>
        </article>
    )
};

/*
- date
- titre
- lieu
- début + fin
*/

export default VideoCard;