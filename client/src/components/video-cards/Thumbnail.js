
const Thumbnail = ({thumbnail_url}) => {
    return (
        <figure className="image">
            <img src={`/${thumbnail_url}`} alt="Video Thumbnail" />
        </figure>
    )
};

export default Thumbnail;