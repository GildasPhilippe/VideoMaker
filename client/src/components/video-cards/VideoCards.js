import VideoCard from "./VideoCard";


const VideoCards = ({videos}) => {    
    return (
        <div id="video-cards">
            {
                videos.map((video, index) => (
                    <VideoCard 
                        video={video}
                        key={`${video.id}-${index}`}
                    />
                ))
            }
        </div>
    )
};

export default VideoCards;
