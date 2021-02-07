const Dropzone = () => {
    return (
        <div className="container">
            <h1 className="title">File Upload</h1>
            <form action="http://localhost:5001/videos/" className="dropzone">
                <input 
                    type="hidden" 
                    name="session-id" 
                    value="my5678super56testide543secret098my5678super56testide543secret098" 
                />
            </form>
        </div>
    )
  }
  
export default Dropzone;