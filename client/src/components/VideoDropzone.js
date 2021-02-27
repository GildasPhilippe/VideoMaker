
const VideoDropzone = ({id}) => {
    return (
        <div className="container">
            <h1 className="title">File Upload</h1>
            <form action="http://localhost:5001/videos/" className="dropzone">
                <input 
                    type="hidden" 
                    name="session-id" 
                    value={id}
                />
            </form>
        </div>
    )
  }
export default VideoDropzone;