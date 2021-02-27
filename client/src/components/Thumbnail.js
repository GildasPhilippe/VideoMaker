
const Thumbnail = ({thumbnail_url}) => {
    console.log("thumbnail_url = " + thumbnail_url)
    return (
        <figure className="image">
            <img src={thumbnail_url} alt="Video Thumbnail" />
        </figure>
    )
};

export default Thumbnail;