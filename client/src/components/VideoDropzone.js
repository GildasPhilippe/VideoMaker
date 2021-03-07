import Dropzone from 'react-dropzone-uploader';


const VideoDropzone = ({session_id}) => {
    const getUploadParams = () => {
        return { url: `http://localhost:5001/videos/${session_id}` }
    }
    
    const handleChangeStatus = ({ xhr }, status) => {
        if (status === 'done'){
            let response = JSON.parse(xhr.response);
            console.log(response.data)
            const video_id = response.data.file_hash;
            console.log(video_id);
            let event = new CustomEvent('video-upload', { detail:{'video_id': video_id }});
            console.log("dispatching event")
            document.dispatchEvent(event);
        }  
    }
    
    const handleSubmit = (files, allFiles) => {
        console.log("Files upladed : " + files)
    }
    
    return (
        <div className="container">
            <div className="card">
                <Dropzone
                    getUploadParams={getUploadParams}
                    onChangeStatus={handleChangeStatus}
                    onSubmit={handleSubmit}
                    styles={{ dropzone: { minHeight: 200, maxHeight: 250 } }}
                    accept="image/*,audio/*,video/*"
                    SubmitButtonComponent={null}
                />
            </div>
        </div>
    )
  };

export default VideoDropzone;