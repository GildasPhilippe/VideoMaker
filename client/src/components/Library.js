import { useState, useEffect } from 'react';
import fetchVideo from '../models/videos';
import VideoCards from './video-cards/VideoCards';


const Library = ({session_id}) => {
    const [videos, setVideos] = useState([])

    const getVideos = async () => {
        const videosFromServer = await fetchVideo(session_id, "all")
        setVideos(videosFromServer)
    }

    useEffect(() => {
        getVideos()
    }, [])

    document.addEventListener('video-upload', function (e) {
        getVideos();
    });

    return (
        <div className="box content">
            {(
                videos.length > 0 ? <VideoCards videos={videos} /> 
                : <div className="has-text-centered is-size-5">No uploaded videos</div>)
            }
        </div>
    )
}
  
export default Library;
