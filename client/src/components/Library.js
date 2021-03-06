import { useState, useEffect } from 'react';
import fetchVideo from '../models/videos';
import VideoCards from './video-cards/VideoCards';


const Library = ({session_id}) => {
    const [showAddVideo, setShowVideo] = useState(false)
    const [videos, setVideos] = useState([])

    const getVideos = async () => {
        const videosFromServer = await fetchVideo(session_id, "all")
        setVideos(videosFromServer)
    }

    useEffect(() => {
        getVideos()
    }, [])

    const addVideo = async (video_id) => {
        getVideos();
    }

    document.addEventListener('video-upload', function (e) {
        console.log("Hello from Library");
        addVideo(e.detail.video_id)
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
