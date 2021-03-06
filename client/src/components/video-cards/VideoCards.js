import VideoCard from "./VideoCard";


const VideoCards = ({videos}) => {
    return (
        <>
            {
                videos.map((video, index) => (
                    <VideoCard 
                        thumbnail_url={video.thumbnail_url}
                        filename={video.filename}
                        title={video.title}
                        location={video.location}
                        start_at={video.start_at}
                        end_at={video.end_at}
                        video_date={video.video_date}
                        key={video.id}
                    />
                ))
            }
        </>
    )
};

export default VideoCards;
